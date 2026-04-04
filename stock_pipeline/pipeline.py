import logging
import sqlite3

import pandas as pd
import yfinance as yf

try:
    from .config import DB_PATH, DEFAULT_INTERVAL, DEFAULT_PERIOD, LOG_FORMAT, LOG_LEVEL, TICKER_SYMBOLS
except ImportError:
    from config import DB_PATH, DEFAULT_INTERVAL, DEFAULT_PERIOD, LOG_FORMAT, LOG_LEVEL, TICKER_SYMBOLS

logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL)
logger = logging.getLogger(__name__)


def extract(symbol, period=DEFAULT_PERIOD, interval=DEFAULT_INTERVAL):
    logger.info("Extracting data for %s (period=%s, interval=%s)", symbol, period, interval)
    stock = yf.Ticker(symbol)
    data = stock.history(period=period, interval=interval)
    logger.info("Fetched %d rows for %s.", len(data), symbol)
    return data


def transform(raw_data):
    clean = raw_data[["Open", "High", "Low", "Close", "Volume"]].copy()
    clean["Spread"] = clean["High"] - clean["Low"]
    logger.info("Transformed — %d rows, %d columns.", len(clean), len(clean.columns))
    return clean


def load(data, symbol):
    table_name = f"{symbol.lower()}_prices"
    conn = sqlite3.connect(str(DB_PATH))
    try:
        data.to_sql(table_name, conn, if_exists="replace", index=True)
        logger.info("Loaded %d rows into '%s'.", len(data), table_name)
    finally:
        conn.close()


def run_pipeline(symbol):
    logger.info("Starting pipeline for %s", symbol)
    raw_data = extract(symbol)
    clean_data = transform(raw_data)
    load(clean_data, symbol)
    logger.info("Pipeline complete for %s! Data stored in %s", symbol, DB_PATH)


def main():
    for symbol in TICKER_SYMBOLS:
        run_pipeline(symbol)


if __name__ == "__main__":
    main()

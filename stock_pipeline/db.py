import logging
import sqlite3
from datetime import date

import matplotlib.pyplot as plt
import yfinance as yf

try:
    from .config import DB_PATH, LOG_FORMAT, LOG_LEVEL
except ImportError:
    from config import DB_PATH, LOG_FORMAT, LOG_LEVEL

logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL)
logger = logging.getLogger(__name__)


def get_connection():
    return sqlite3.connect(str(DB_PATH))


def create_table(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS stock_prices (
            Date   TEXT,
            Symbol TEXT,
            Price  REAL
        )
    """)
    conn.commit()
    logger.info("Table 'stock_prices' is ready.")


def insert_price(conn, symbol, price, record_date=None):
    record_date = record_date or str(date.today())
    conn.execute(
        "INSERT INTO stock_prices (Date, Symbol, Price) VALUES (?, ?, ?)",
        (record_date, symbol, price),
    )
    conn.commit()
    logger.info("Inserted %s price: $%.2f on %s", symbol, price, record_date)


def fetch_prices(conn, symbol=None):
    if symbol:
        cursor = conn.execute(
            "SELECT * FROM stock_prices WHERE Symbol = ? ORDER BY Date",
            (symbol,),
        )
    else:
        cursor = conn.execute("SELECT * FROM stock_prices ORDER BY Date")
    return cursor.fetchall()


def plot_prices(records, title="Stock Price History"):
    if not records:
        logger.warning("No records to plot.")
        return

    dates = [row[0] for row in records]
    prices = [row[2] for row in records]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, prices, marker="o", linewidth=2, color="#2196F3")
    plt.fill_between(dates, prices, alpha=0.1, color="#2196F3")
    plt.title(title, fontsize=14, fontweight="bold")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True, alpha=0.3)
    plt.show()


def fetch_live_price(symbol):
    logger.info("Downloading live data for %s ...", symbol)
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1d")

    if data.empty:
        raise ValueError(f"No data returned for symbol '{symbol}'")

    price = data["Close"].iloc[0]
    logger.info("Fetched %s closing price: $%.2f", symbol, price)
    return float(price)


def main():
    conn = get_connection()
    try:
        create_table(conn)
        price = fetch_live_price("AAPL")
        insert_price(conn, "AAPL", price)
        records = fetch_prices(conn, symbol="AAPL")
        plot_prices(records, title="AAPL Price History")
    except Exception:
        logger.exception("An error occurred during DB operations.")
    finally:
        conn.close()
        logger.info("Database connection closed.")


if __name__ == "__main__":
    main()

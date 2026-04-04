from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "market_data.db"

TICKER_SYMBOLS = ["AAPL"]

DEFAULT_PERIOD = "1d"
DEFAULT_INTERVAL = "1m"

LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(message)s"
LOG_LEVEL = "INFO"

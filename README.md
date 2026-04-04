# 🚀 DSA Journey + Stock Pipeline

A dual-purpose Python repository:
1. **DSA Practice** — Clean, documented LeetCode solutions with complexity analysis.
2. **Stock Pipeline** — A lightweight ETL pipeline that fetches live market data, stores it in SQLite, and visualizes price trends.

---

## 📁 Project Structure

```
DSA--Journney/
├── dsa/                              # LeetCode solutions
│   ├── two_sum.py                    # #1   – Two Sum
│   ├── valid_palindrome.py           # #125 – Valid Palindrome
│   └── maximum_average_subarray.py   # #643 – Maximum Average Subarray I
│
├── stock_pipeline/                   # Stock market ETL pipeline
│   ├── config.py                     # Centralized settings
│   ├── pipeline.py                   # Extract → Transform → Load
│   └── db.py                         # DB operations & visualization
│
├── requirements.txt                  # Python dependencies
├── Makefile                          # Handy shortcuts
└── README.md
```

---

## ⚡ Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/your-username/DSA--Journney.git
cd DSA--Journney

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
make install
# or: pip install -r requirements.txt
```

---

## 📊 Stock Pipeline

Fetch live intraday stock data, clean it, and store it locally.

```bash
# Run the full ETL pipeline
make pipeline

# Or fetch a single price and plot history
make db
```

**What it does:**

| Stage       | Description                                        |
|-------------|----------------------------------------------------|
| **Extract** | Pulls intraday OHLCV data from Yahoo Finance       |
| **Transform** | Cleans columns, adds `Spread` (High − Low)       |
| **Load**    | Writes to a local SQLite database (`market_data.db`) |

> **Tip:** Edit `stock_pipeline/config.py` to change tickers, periods, or intervals — no need to touch the pipeline code.

---

## 🧠 DSA Solutions

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | 🟢 Easy | Hash Map | O(n) | O(n) |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | 🟢 Easy | Two Pointers | O(n) | O(n) |
| 643 | [Max Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | 🟢 Easy | Sliding Window | O(n) | O(1) |

```bash
# Quick-run all solutions
make dsa-test
```

---

## 🛠️ Tech Stack

- **Python 3.12+**
- **yfinance** — Yahoo Finance market data API
- **matplotlib** — Data visualization
- **pandas** — Data manipulation
- **SQLite** — Lightweight local database

---

## 📝 License

This project is for personal learning and practice.
import sqlite3
import yfinance as yf
import matplotlib.pyplot as plt

connection = sqlite3.connect('market_data.db')
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS stock_prices (
    Date TEXT,
    Symbol TEXT,
    Price REAL
)
"""
cursor.execute(create_table_query)

try:
    print("Downloading live data...")
    apple_stock = yf.Ticker("AAPL")
    todays_data = apple_stock.history(period="1d")
    apple_current_price = todays_data['Close'].iloc[0]

    insert_query = """
    INSERT INTO stock_prices (Date, Symbol, Price)
    VALUES (?, ?, ?)
    """
    cursor.execute(insert_query, ('2026-03-31', 'AAPL', apple_current_price))
    connection.commit()
    print(f"Successfully saved AAPL price: {apple_current_price}")

except Exception as e:
    print("Uh oh, something went wrong!")
    print(e)



cursor.execute("SELECT * FROM stock_prices")
all_results = cursor.fetchall()


dates = []
prices = []

for row in all_results:
    dates.append(row[0])  
    prices.append(row[2]) 


plt.plot(dates, prices)
plt.title("Stock Price History")
plt.show()


connection.close()
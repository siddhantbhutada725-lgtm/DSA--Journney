import yfinance as yf 
import sqlite3
ticker_symbol="AAPL"
stock = yf.Ticker(ticker_symbol)
data=stock.history(period="1d",interval="1m")
print(f"Succesfully fetched{len(data)} rows of data for{ticker_symbol}!")

clean_data=data[['Open','High','Low','Close','Volume']].copy()
clean_data['Spread'] = clean_data['High'] - clean_data['Low']
print("Data succesfully transformed")

conn=sqlite3.connect("market_data.db")
clean_data.to_sql("apple_prices",conn,if_exists="replace",index=True)
conn.close()

print("\n pipeline complete! data safely stored in market_data.db")


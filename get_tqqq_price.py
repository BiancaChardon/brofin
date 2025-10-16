import yfinance as yf

# Get TQQQ stock data
ticker = yf.Ticker("TQQQ")

# Get current stock info
info = ticker.info

# Get the most recent price
current_price = info.get('currentPrice') or info.get('regularMarketPrice')

print(f"TQQQ Stock Price Information:")
print(f"=" * 40)
print(f"Current Price: ${current_price:.2f}")
print(f"Previous Close: ${info.get('previousClose', 'N/A'):.2f}")
print(f"Open: ${info.get('open', 'N/A'):.2f}")
print(f"Day High: ${info.get('dayHigh', 'N/A'):.2f}")
print(f"Day Low: ${info.get('dayLow', 'N/A'):.2f}")
print(f"Volume: {info.get('volume', 'N/A'):,}")

# Alternative method: Get latest data from history
print(f"\n" + "=" * 40)
print("Latest Trading Data:")
hist = ticker.history(period="1d")
if not hist.empty:
    latest_close = hist['Close'].iloc[-1]
    print(f"Latest Close: ${latest_close:.2f}")
    print(f"Latest High: ${hist['High'].iloc[-1]:.2f}")
    print(f"Latest Low: ${hist['Low'].iloc[-1]:.2f}")
    print(f"Latest Volume: {int(hist['Volume'].iloc[-1]):,}")

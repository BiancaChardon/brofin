import yfinance as yf

# Get TQQQ stock data
ticker = yf.Ticker("TQQQ")

print(f"TQQQ Stock Price Information:")
print(f"=" * 40)

# Get latest data from history (more reliable than .info)
hist = ticker.history(period="5d")
if not hist.empty:
    latest_close = hist['Close'].iloc[-1]
    latest_open = hist['Open'].iloc[-1]
    latest_high = hist['High'].iloc[-1]
    latest_low = hist['Low'].iloc[-1]
    latest_volume = hist['Volume'].iloc[-1]

    print(f"Latest Close: ${latest_close:.2f}")
    print(f"Open: ${latest_open:.2f}")
    print(f"Day High: ${latest_high:.2f}")
    print(f"Day Low: ${latest_low:.2f}")
    print(f"Volume: {int(latest_volume):,}")

    if len(hist) > 1:
        previous_close = hist['Close'].iloc[-2]
        price_change = latest_close - previous_close
        percent_change = (price_change / previous_close) * 100
        print(f"Previous Close: ${previous_close:.2f}")
        print(f"Change: ${price_change:.2f} ({percent_change:+.2f}%)")
else:
    print("No data available")

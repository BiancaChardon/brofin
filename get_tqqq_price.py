import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Get TQQQ stock data
ticker = yf.Ticker("TQQQ")

print(f"TQQQ - Last 5 Minutes (1-minute intervals)")
print(f"=" * 60)

# Get 1-minute interval data for the last 5 minutes
hist = ticker.history(period="1d", interval="1m")

if not hist.empty:
    # Get the last 5 minutes
    last_5_min = hist.tail(5)

    print(f"{'Time':<20} {'Close':<10} {'Volume':<15} {'Change %':<10}")
    print(f"-" * 60)

    for i, (timestamp, row) in enumerate(last_5_min.iterrows()):
        close_price = row['Close']
        volume = int(row['Volume'])

        # Calculate change from previous minute
        if i > 0:
            prev_close = last_5_min.iloc[i-1]['Close']
            change_pct = ((close_price - prev_close) / prev_close) * 100
            change_str = f"{change_pct:+.2f}%"
        else:
            change_str = "-"

        time_str = timestamp.strftime("%Y-%m-%d %H:%M")
        print(f"{time_str:<20} ${close_price:<9.2f} {volume:<14,} {change_str:<10}")

    print(f"\n" + "=" * 60)
    print(f"Latest Price: ${last_5_min['Close'].iloc[-1]:.2f}")

    # Overall change across the 5 minutes
    if len(last_5_min) > 1:
        first_price = last_5_min['Close'].iloc[0]
        last_price = last_5_min['Close'].iloc[-1]
        total_change = last_price - first_price
        total_change_pct = (total_change / first_price) * 100
        print(f"5-Minute Change: ${total_change:.2f} ({total_change_pct:+.2f}%)")

    # Create Plotly visualization
    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=('TQQQ Price (Last 5 Minutes)', 'Volume'),
        vertical_spacing=0.15,
        row_heights=[0.7, 0.3]
    )

    # Add price line chart
    fig.add_trace(
        go.Scatter(
            x=last_5_min.index,
            y=last_5_min['Close'],
            mode='lines+markers',
            name='Close Price',
            line=dict(color='#00ff00', width=2),
            marker=dict(size=8)
        ),
        row=1, col=1
    )

    # Add volume bar chart
    fig.add_trace(
        go.Bar(
            x=last_5_min.index,
            y=last_5_min['Volume'],
            name='Volume',
            marker=dict(color='#1f77b4')
        ),
        row=2, col=1
    )

    # Update layout
    fig.update_layout(
        title=f'TQQQ - Last 5 Minutes | Latest: ${last_5_min["Close"].iloc[-1]:.2f}',
        showlegend=True,
        height=700,
        template='plotly_dark'
    )

    fig.update_xaxes(title_text="Time", row=2, col=1)
    fig.update_yaxes(title_text="Price ($)", row=1, col=1)
    fig.update_yaxes(title_text="Volume", row=2, col=1)

    # Show the plot
    fig.show()
    print("\nOpening interactive chart in browser...")

else:
    print("No data available")

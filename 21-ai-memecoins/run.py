import requests
import time
import pandas as pd

# Constants
API_URL = "https://api.coingecko.com/api/v3"
CATEGORY = "ai-meme-coins"  # Category slug from Coingecko
TOP_N = 10  # Number of top coins to track
BREAKOUT_THRESHOLD = 0.05  # 5% price change within a minute (example)

def fetch_top_coins(category, top_n):
    """Fetch top coins by market cap in the specified category."""
    response = requests.get(f"{API_URL}/coins/markets", params={
        "vs_currency": "usd",
        "category": category,
        "order": "market_cap_desc",
        "per_page": top_n,
        "page": 1
    })
    response.raise_for_status()
    return response.json()

def track_prices(coins):
    """Track price changes and detect breakouts."""
    # Initialize previous prices
    prices = {coin['id']: coin['current_price'] for coin in coins}
    print(f"Tracking coins: {', '.join(prices.keys())}")

    while True:
        time.sleep(60)  # Wait for one minute between checks

        # Fetch latest prices
        response = requests.get(f"{API_URL}/simple/price", params={
            "ids": ",".join(prices.keys()),
            "vs_currencies": "usd"
        })
        response.raise_for_status()
        new_prices = response.json()

        # Check for breakouts
        for coin_id, old_price in prices.items():
            new_price = new_prices[coin_id]['usd']
            change = (new_price - old_price) / old_price

            if abs(change) >= BREAKOUT_THRESHOLD:
                print(f"🚨 Breakout detected for {coin_id}! Change: {change:.2%}")
                # You can add further actions here (e.g., send notifications)

            # Update price
            prices[coin_id] = new_price

if __name__ == "__main__":
    try:
        # Step 1: Fetch top N coins by market cap in the AI meme coins category
        top_coins = fetch_top_coins(CATEGORY, TOP_N)

        # Step 2: Start tracking prices for breakouts
        track_prices(top_coins)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

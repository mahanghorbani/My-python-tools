import requests

def get_market_data(symbol="BTC"):
    """
    دریافت قیمت لحظه‌ای یک دارایی دیجیتال از طریق API
    """
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT"
    try:
        response = requests.get(url)
        data = response.json()
        print(f"Current price of {symbol}: {data['price']} USDT")
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    print("Market Monitor Initialized...")
    get_market_data("BTC")

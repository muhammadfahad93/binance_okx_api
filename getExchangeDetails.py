import json
import ccxt
# Open and read the JSON configuration file
with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)

# Access individual configuration settings
binance_api_key = config_data['binance_api_key']
binance_secret_key = config_data['binance_secret_key']
okex_api_key = config_data['okex_api_key']
okex_secret_key = config_data['okex_secret_key']


# Initialize the Binance exchange
binance_exchange = ccxt.binance({
    'apiKey': binance_api_key,
    'secret': binance_secret_key,
})

# Initialize the OKEx exchange
okex_exchange = ccxt.okex({
    'apiKey': okex_api_key,
    'secret': okex_secret_key,
})

# Fetch open orders on Binance
def get_binance_open_orders():
    try:
        open_orders = binance_exchange.fetch_open_orders()
        if open_orders:
            print("Open Orders on Binance:")
            for order in open_orders:
                print(f"Symbol: {order['symbol']}, Type: {order['side']}, Price: {order['price']}, Quantity: {order['amount']}, Order ID: {order['id']}")
        else:
            print("No open orders found on Binance.")
    except ccxt.NetworkError as e:
        print(f"Binance Network error: {e}")
    except ccxt.ExchangeError as e:
        print(f"Binance Exchange error: {e}")
    except Exception as e:
        print(f"An error occurred on Binance: {e}")

# Fetch open orders on OKEx
def get_okex_open_orders():
    try:
        open_orders = okex_exchange.fetch_open_orders()
        if open_orders:
            print("Open Orders on OKEx:")
            for order in open_orders:
                print(f"Symbol: {order['symbol']}, Type: {order['side']}, Price: {order['price']}, Quantity: {order['amount']}, Order ID: {order['id']}")
        else:
            print("No open orders found on OKEx.")
    except ccxt.NetworkError as e:
        print(f"OKEx Network error: {e}")
    except ccxt.ExchangeError as e:
        print(f"OKEx Exchange error: {e}")
    except Exception as e:
        print(f"An error occurred on OKEx: {e}")

# Fetch margin balance on Binance
def get_binance_margin_balance():
    try:
        margin_balance = binance_exchange.fetch_balance({'type': 'margin'})
        if 'total' in margin_balance:
            print("Margin Balance on Binance:")
            for asset, balance in margin_balance['total'].items():
                print(f"{asset}: {balance}")
        else:
            print("No margin balance data available on Binance.")
    except ccxt.NetworkError as e:
        print(f"Binance Network error: {e}")
    except ccxt.ExchangeError as e:
        print(f"Binance Exchange error: {e}")
    except Exception as e:
        print(f"An error occurred on Binance: {e}")

# Fetch margin balance on OKEx
def get_okex_margin_balance():
    try:
        margin_balance = okex_exchange.fetch_balance({'type': 'margin'})
        if 'total' in margin_balance:
            print("Margin Balance on OKEx:")
            for asset, balance in margin_balance['total'].items():
                print(f"{asset}: {balance}")
        else:
            print("No margin balance data available on OKEx.")
    except ccxt.NetworkError as e:
        print(f"OKEx Network error: {e}")
    except ccxt.ExchangeError as e:
        print(f"OKEx Exchange error: {e}")
    except Exception as e:
        print(f"An error occurred on OKEx: {e}")

if __name__ == "__main__":
    get_binance_open_orders()
    get_binance_margin_balance()
    get_okex_open_orders()
    get_okex_margin_balance()
"""
The Proxy Pattern is a structural design pattern that provides a surrogate or placeholder for another object to control access to it.
The proxy object acts as an intermediary between the client and the real object, allowing for additional functionality like lazy initialization, access control, logging, or caching.

*** Purpose ***
The primary purpose of the Proxy Pattern is to control access to an object.
This control can be for various reasons, such as adding security, reducing the cost of object creation, or handling remote requests.

*** Intuition ***
Imagine you have a financial system that retrieves and processes large datasets from a remote server.
Directly accessing the remote server every time you need the data can be inefficient and slow.
Instead, you can use a proxy to manage the data retrieval, caching, and access control.

*** Structure ***
1. Subject Interface: Declares common interface for RealSubject and Proxy.
2. RealSubject: The actual object that the proxy represents.
3. Proxy: Controls access to the RealSubject, may add additional functionality.

*** Example: Financial Data Access ***
Let's consider an example where we need to access financial market data from a remote server.
We'll use the Proxy Pattern to control access to this data, adding caching to improve performance.

"""

#======================= Subject Interface =======================

# Define the interface for accessing market data

from abc import ABC, abstractmethod

class MarketData(ABC):
    @abstractmethod
    def get_data(self, symbol: str) -> dict:
        pass

#======================= RealSubject =======================

# Implement the real object that retrieves market data from a remote server

class RealMarketData(MarketData):
    def get_data(self, symbol: str) -> dict:
        print(f"Fetching market data for {symbol} from remote server")
        # Simulate fetching data from a remote server
        return {'price': 100, 'volume': 1000}

#======================= Proxy =======================

# Implement the proxy that controls access to the RealMarketData object

class MarketDataProxy(MarketData):
    def __init__(self):
        self.real_market_data = RealMarketData()
        self.cache = {}

    def get_data(self, symbol: str) -> dict:
        if symbol in self.cache:
            print(f"Returning cached data for {symbol}")
            return self.cache[symbol]
        else:
            print(f"Cache miss for {symbol}. Fetching data...")
            data = self.real_market_data.get_data(symbol)
            self.cache[symbol] = data
            return data

#======================= Client Code =======================

# Use the proxy in the client code to access market data

if __name__ == "__main__":
    market_data_proxy = MarketDataProxy()

    # First access, data will be fetched from the remote server
    data1 = market_data_proxy.get_data("AAPL")
    print(f"Data for AAPL: {data1}")

    # Second access, data will be returned from the cache
    data2 = market_data_proxy.get_data("AAPL")
    print(f"Data for AAPL: {data2}")

    # Accessing different symbol, data will be fetched from the remote server
    data3 = market_data_proxy.get_data("TSLA")
    print(f"Data for TSLA: {data3}")


#======================= How It Works =======================

"""
1. Subject Interface
MarketData is the interface that declares the get_data method.

2. RealSubject
RealMarketData implements the MarketData interface and simulates fetching market data from a remote server.

3. Proxy
MarketDataProxy also implements the MarketData interface and adds caching functionality. It controls access to the RealMarketData object, checking the cache before fetching data.

4. Client Code
The client interacts with the MarketDataProxy to access market data. The proxy handles caching and only fetches data from the remote server when necessary.

"""
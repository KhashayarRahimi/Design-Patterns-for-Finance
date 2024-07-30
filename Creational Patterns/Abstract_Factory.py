"""
*** Purpose ***
The Abstract Factory Pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes. It is used when a system needs to be independent of how its products are created, composed, and represented. It ensures that objects created within a family are compatible with each other and promotes a high level of consistency.

*** Intuition ***
Imagine you have a financial backtesting module that needs to handle different types of financial instruments (e.g., Options and Futures) along with their associated market data fetchers. Instead of creating these instruments and fetchers directly in your main code, you use an abstract factory to create them. This way, if you need to add new types of instruments or change existing ones, you only need to modify or add a new factory and not the main code.

*** Structure ***
Abstract Factory: Declares an interface for creating abstract products.
Concrete Factory: Implements the interface to create concrete product objects.
Abstract Product: Declares an interface for a type of product.
Concrete Product: Implements the abstract product interface.
Client: Uses only the interfaces declared by the abstract factory and abstract product classes.

Example: Financial Backtest Module for Derivatives
In this example, we need to handle different types of derivatives and their market data fetchers. We will use the Abstract Factory Pattern to create these derivatives and fetchers, ensuring that they are compatible and work together seamlessly.
"""

from abc import ABC, abstractmethod

# Abstract Products
class Derivative(ABC):
    @abstractmethod
    def get_price(self, market_data):
        pass

class MarketDataFetcher(ABC):
    @abstractmethod
    def fetch(self):
        pass

# Concrete Products
class Option(Derivative):
    def __init__(self, strike_price, expiry_date):
        self.strike_price = strike_price
        self.expiry_date = expiry_date
    
    def get_price(self, market_data):
        return market_data['current_price'] - self.strike_price

class Future(Derivative):
    def __init__(self, expiry_date):
        self.expiry_date = expiry_date
    
    def get_price(self, market_data):
        return market_data['future_price']

class OptionMarketDataFetcher(MarketDataFetcher):
    def fetch(self):
        return {'current_price': 100}

class FutureMarketDataFetcher(MarketDataFetcher):
    def fetch(self):
        return {'future_price': 105}

# Abstract Factory
class FinancialInstrumentFactory(ABC):
    @abstractmethod
    def create_derivative(self, **kwargs):
        pass
    
    @abstractmethod
    def create_market_data_fetcher(self):
        pass

# Concrete Factories
class OptionFactory(FinancialInstrumentFactory):
    def create_derivative(self, **kwargs):
        return Option(kwargs['strike_price'], kwargs['expiry_date'])
    
    def create_market_data_fetcher(self):
        return OptionMarketDataFetcher()

class FutureFactory(FinancialInstrumentFactory):
    def create_derivative(self, **kwargs):
        return Future(kwargs['expiry_date'])
    
    def create_market_data_fetcher(self):
        return FutureMarketDataFetcher()

def get_financial_instrument_details(factory: FinancialInstrumentFactory, **kwargs):
    derivative = factory.create_derivative(**kwargs)
    market_data_fetcher = factory.create_market_data_fetcher()
    market_data = market_data_fetcher.fetch()
    return derivative.get_price(market_data)

# Using the Option Factory
option_factory = OptionFactory()
option_price = get_financial_instrument_details(option_factory, strike_price=90, expiry_date='2024-12-31')
print(f"Option Price: {option_price}")  # Output: Option Price: 10

# Using the Future Factory
future_factory = FutureFactory()
future_price = get_financial_instrument_details(future_factory, expiry_date='2024-12-31')
print(f"Future Price: {future_price}")  # Output: Future Price: 105


#===================== Factory Method vs Abstract Factory Pattern =====================

"""
*** Factory Method Pattern ***
Single Responsibility: Each factory (subclass) creates a single type of product.
Single Method: Typically involves a single method (create_product or similar) that subclasses override to create instances of specific products.
Example Context: Creating a single type of financial derivative, like either an option or a future.

*** Abstract Factory Pattern ***
Multiple Responsibilities: Each factory creates multiple related products (a family of products) that are designed to be used together.
Multiple Methods: Involves multiple methods to create different products that belong to the same family.
Example Context: Creating a set of related products like both an option and its corresponding market data fetcher.
"""
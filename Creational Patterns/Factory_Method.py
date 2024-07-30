""" 
*** Purpose ***
The Factory Method Pattern defines an interface for creating an object, but lets subclasses alter the type of objects that will be created.
It promotes loose coupling by eliminating the need to bind application-specific classes into the code.

*** Intuition ***
Imagine you have a financial backtesting module where you need to handle different types of derivatives (options, futures, etc.).
Instead of creating these derivative objects directly in your main code, you use a factory to create them.
This way, if you need to add new derivative types or change existing ones, you only need to modify the factory and not the main code.

*** Structure ***
1. Product Interface: Defines the interface of the objects the factory method creates.
2. Concrete Products: Implementations of the product interface.
3. Creator (Factory): Declares the factory method, which returns an object of type Product.
4. Concrete Creators: Override the factory method to return an instance of a Concrete Product.

Example: Financial Backtest Module for Derivatives
Let's say we have different types of derivatives we want to backtest: Options and Futures. We will create a factory method to handle the creation of these derivatives.

"""
from abc import ABC, abstractmethod

class Derivative(ABC):
    @abstractmethod
    def get_price(self, market_data):
        pass

class Option(Derivative):
    def __init__(self, strike_price, expiry_date):
        self.strike_price = strike_price
        self.expiry_date = expiry_date
    
    def get_price(self, market_data):
        # Simplified option pricing logic
        return market_data['current_price'] - self.strike_price

class Future(Derivative):
    def __init__(self, expiry_date):
        self.expiry_date = expiry_date
    
    def get_price(self, market_data):
        # Simplified future pricing logic
        return market_data['future_price']

"""  
# Market data example
market_data = {
    'current_price': 100,
    'future_price': 105
}

# Create an Option
option_factory = OptionFactory()
option = option_factory.create_derivative(strike_price=90, expiry_date='2024-12-31')
print(f"Option Price: {option.get_price(market_data)}")  # Output: Option Price: 10

# Create a Future
future_factory = FutureFactory()
future = future_factory.create_derivative(expiry_date='2024-12-31')
print(f"Future Price: {future.get_price(market_data)}")  # Output: Future Price: 105

"""

#============================================= Abstract Base Class =============================================

"""
*** abc module ***
The abc module stands for "Abstract Base Classes" in Python.
It is used to define abstract base classes, which are classes that cannot be instantiated directly and are meant to be subclasses.
They often contain abstract methods that must be implemented by any concrete (non-abstract) subclasses.

*** ABC (Abstract Base Class) ***
This is a class from which other classes can inherit.
It is provided by the abc module and is used to define abstract base classes.
You cannot create an instance of an abstract base class.

*** abstractmethod ***
This is a decorator used to declare methods as abstract.
An abstract method is one that must be implemented by any concrete subclass of the abstract base class.
If a subclass does not implement the abstract method, an error will be raised when trying to instantiate the subclass.

"""

#============================================= Why Abstract Base Class? =============================================

"""
*** Ensures a Common Interface ***
By declaring get_price as an abstract method in the Derivative class, you are enforcing that all subclasses of Derivative must implement this method.
This guarantees that any object that is a subclass of Derivative will have a get_price method, ensuring a common interface for all derivatives.

*** NOTE ***
If a subclass does not implement the get_price method, it will raise an error at instantiation time, ensuring that the subclass is not incomplete.]
"""

#============================================= Benefits =============================================

"""  
*** Uniformity ***
All derivative types (options, futures, etc.) will have a consistent method to retrieve their price.

*** Extensibility ***
Adding new types of derivatives is straightforward. Just create a new subclass and implement the get_price method.

*** Error Prevention ***
The abstract base class enforces that all necessary methods are implemented, reducing the risk of missing method errors at runtime.

*** Polymorphism ***
Polymorphism is enforced, making it easier to write flexible and interchangeable code.


Polymorphism is a fundamental concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass.
It enables a single interface to represent different underlying forms (data types).
"""
"""
The Decorator Pattern is a structural design pattern that allows behavior to be added to individual objects, either statically or dynamically,
without affecting the behavior of other objects from the same class. This pattern is useful when you want to add responsibilities to objects without modifying their code.

*** Decorator Pattern Explained Intuitively ***
Imagine a Coffee Shop

1. Basic Coffee:

Base Object: Think of a plain cup of coffee.

2.Add-ons:

Dynamic Behavior: You might want to add milk, sugar, or whipped cream to your coffee. Instead of creating a new class for every possible combination of coffee and add-ons, you can dynamically add these features.

*** Structure ***

Component: The interface for objects that can have responsibilities added to them.
Concrete Component: The base implementation of the Component interface.
Decorator: Maintains a reference to a Component object and defines an interface that conforms to the Component’s interface.
Concrete Decorators: Extend the functionality of the component by adding new behavior.

*** Example: Financial Trade Orders ***

In this example, we'll have a basic financial instrument pricing system.
We'll use decorators to add various features to the pricing calculation, such as risk assessment, logging, and commission fees.
"""

#============================ Component ============================

# Define the base interface for financial instruments

from abc import ABC, abstractmethod

class FinancialInstrument(ABC):
    @abstractmethod
    def calculate_price(self, market_data) -> float:
        pass

    @abstractmethod
    def describe(self) -> str:
        pass

#============================ Concrete Component ============================

# Implement basic financial instruments

class Stock(FinancialInstrument):
    def __init__(self, ticker: str):
        self.ticker = ticker

    def calculate_price(self, market_data) -> float:
        return market_data[self.ticker]

    def describe(self) -> str:
        return f"Stock: {self.ticker}"

class Bond(FinancialInstrument):
    def __init__(self, face_value: float, interest_rate: float):
        self.face_value = face_value
        self.interest_rate = interest_rate

    def calculate_price(self, market_data) -> float:
        # Simplified bond pricing logic
        return self.face_value * (1 + self.interest_rate)

    def describe(self) -> str:
        return f"Bond: Face Value = {self.face_value}, Interest Rate = {self.interest_rate * 100}%"

#============================ Decorator ============================

# Create a base decorator class

class FinancialInstrumentDecorator(FinancialInstrument):
    def __init__(self, instrument: FinancialInstrument):
        self._instrument = instrument

    def calculate_price(self, market_data) -> float:
        return self._instrument.calculate_price(market_data)

    def describe(self) -> str:
        return self._instrument.describe()
    

#============================ Concrete Decorators ============================

# Add specific features

class RiskAssessmentDecorator(FinancialInstrumentDecorator):
    def __init__(self, instrument: FinancialInstrument, risk_factor: float):
        super().__init__(instrument)
        self.risk_factor = risk_factor

    def calculate_price(self, market_data) -> float:
        price = super().calculate_price(market_data)
        # Adjust price based on risk factor
        return price * (1 - self.risk_factor)

    def describe(self) -> str:
        return f"{super().describe()} with Risk Factor = {self.risk_factor * 100}%"

class LoggingDecorator(FinancialInstrumentDecorator):
    def calculate_price(self, market_data) -> float:
        price = super().calculate_price(market_data)
        print(f"Logging: Calculating price for {super().describe()} - Price: {price}")
        return price

class CommissionDecorator(FinancialInstrumentDecorator):
    def __init__(self, instrument: FinancialInstrument, commission_rate: float):
        super().__init__(instrument)
        self.commission_rate = commission_rate

    def calculate_price(self, market_data) -> float:
        price = super().calculate_price(market_data)
        # Apply commission fee
        return price + (price * self.commission_rate)

    def describe(self) -> str:
        return f"{super().describe()} with Commission Rate = {self.commission_rate * 100}%"

#============================ Client Code ============================

# Use the decorators to add features to the financial instrument pricing

# Client Code
if __name__ == "__main__":
    # Market data example
    market_data = {
        'AAPL': 150.0,
        'TSLA': 650.0
    }

    # Create a basic stock
    apple_stock = Stock(ticker='AAPL')
    print(f"Original: {apple_stock.describe()} - Price: ${apple_stock.calculate_price(market_data)}")

    # Decorate the stock with logging
    logged_stock = LoggingDecorator(apple_stock)
    print(f"With Logging: {logged_stock.describe()} - Price: ${logged_stock.calculate_price(market_data)}")

    # Add risk assessment to the logged stock
    risk_assessed_stock = RiskAssessmentDecorator(logged_stock, risk_factor=0.05)
    print(f"With Risk Assessment: {risk_assessed_stock.describe()} - Price: ${risk_assessed_stock.calculate_price(market_data)}")

    # Add commission to the risk assessed and logged stock
    commissioned_stock = CommissionDecorator(risk_assessed_stock, commission_rate=0.02)
    print(f"With Commission: {commissioned_stock.describe()} - Price: ${commissioned_stock.calculate_price(market_data)}")

    # Create a basic bond
    bond = Bond(face_value=1000.0, interest_rate=0.05)
    print(f"Original: {bond.describe()} - Price: ${bond.calculate_price(market_data)}")

    # Decorate the bond with logging and risk assessment
    logged_bond = LoggingDecorator(bond)
    risk_assessed_bond = RiskAssessmentDecorator(logged_bond, risk_factor=0.03)
    print(f"With Risk Assessment and Logging: {risk_assessed_bond.describe()} - Price: ${risk_assessed_bond.calculate_price(market_data)}")

#======================= How It Works =======================

"""
*** Component ***
FinancialInstrument is the base interface for financial instruments, declaring calculate_price and describe methods.

*** Concrete Component ***
Stock and Bond implement the base financial instrument functionality, providing specific pricing logic.

*** Decorator ***
FinancialInstrumentDecorator is the base decorator class that wraps a FinancialInstrument and delegates the calculate_price and describe methods to the wrapped instrument.

*** Concrete Decorators ***
RiskAssessmentDecorator adjusts the price based on a risk factor.
LoggingDecorator logs the pricing calculation.
CommissionDecorator adds a commission fee to the price.

"""
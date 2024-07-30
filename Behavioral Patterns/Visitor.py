"""
The Visitor Pattern is a behavioral design pattern that lets you define new operations on a set of objects without changing the objects themselves.
It involves adding a new visitor class that can operate on elements of a data structure, making it easier to add new functionalities to existing code without modifying it.

*** Purpose ***
The primary purpose of the Visitor Pattern is to separate algorithms from the objects on which they operate.
This is useful when you need to perform different operations on a set of objects that are part of a complex structure, and you want to add new operations without changing the object classes.

*** Intuition ***
Imagine you have a set of financial instruments, such as stocks and bonds, and you want to perform various operations like calculating tax, generating reports, or applying discount rates.
Instead of modifying the classes for each financial instrument every time a new operation is needed, you can use the Visitor Pattern to create separate visitor classes for each operation.
This way, you can add new operations by creating new visitor classes without altering the existing instrument classes.

*** Structure ***
1. Element: Defines an interface for accepting a visitor.
2. ConcreteElement: Implements the Element interface and defines specific behaviors.
3. Visitor: Declares a visit method for each type of ConcreteElement.
4. ConcreteVisitor: Implements the visit methods and defines specific operations for each ConcreteElement.

*** Example: Financial Instruments ***
Let's consider an example where we have different financial instruments (stocks and bonds) and we want to perform various operations such as calculating taxes and generating reports.
"""

#============================================= Element Interface =============================================

# Define the element interface

from abc import ABC, abstractmethod

class FinancialInstrument(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

#============================================= Concrete Elements =============================================

# Implement concrete elements for different financial instruments

class Stock(FinancialInstrument):
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

    def accept(self, visitor):
        visitor.visit_stock(self)

class Bond(FinancialInstrument):
    def __init__(self, issuer, face_value):
        self.issuer = issuer
        self.face_value = face_value

    def accept(self, visitor):
        visitor.visit_bond(self)

#============================================= Visitor Interface =============================================

# Define the visitor interface

class FinancialVisitor(ABC):
    @abstractmethod
    def visit_stock(self, stock):
        pass

    @abstractmethod
    def visit_bond(self, bond):
        pass

#============================================= Concrete Visitors =============================================

# Implement concrete visitors for different operations

class TaxCalculator(FinancialVisitor):
    def visit_stock(self, stock):
        tax = stock.price * 0.15  # 15% tax
        print(f"Tax for stock {stock.symbol}: ${tax}")

    def visit_bond(self, bond):
        tax = bond.face_value * 0.10  # 10% tax
        print(f"Tax for bond {bond.issuer}: ${tax}")

class ReportGenerator(FinancialVisitor):
    def visit_stock(self, stock):
        print(f"Generating report for stock {stock.symbol} with price ${stock.price}")

    def visit_bond(self, bond):
        print(f"Generating report for bond {bond.issuer} with face value ${bond.face_value}")

#============================================= Client Code =============================================

# Use the visitor pattern in the client code to perform operations

if __name__ == "__main__":
    stock = Stock(symbol="AAPL", price=150)
    bond = Bond(issuer="US Treasury", face_value=1000)

    tax_calculator = TaxCalculator()
    report_generator = ReportGenerator()

    stock.accept(tax_calculator)  # Output: Tax for stock AAPL: $22.5
    bond.accept(tax_calculator)   # Output: Tax for bond US Treasury: $100

    stock.accept(report_generator)  # Output: Generating report for stock AAPL with price $150
    bond.accept(report_generator)   # Output: Generating report for bond US Treasury with face value $1000

#============================================= How It Works =============================================

"""
1. Element Interface
FinancialInstrument defines the accept method that accepts a visitor.

2. Concrete Elements
Stock and Bond implement the FinancialInstrument interface and provide their specific implementations of the accept method, which calls the visitor's methods.

3. Visitor Interface
FinancialVisitor declares visit methods for each type of FinancialInstrument. Each visit method is meant to handle a specific type of element.

4. Concrete Visitors
TaxCalculator and ReportGenerator implement the FinancialVisitor interface and provide specific operations for each type of element.

5. Client Code
The client creates instances of elements and visitors, and then uses the accept method of the elements to perform operations defined in the visitors.
"""
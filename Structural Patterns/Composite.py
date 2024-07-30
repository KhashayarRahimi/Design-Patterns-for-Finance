"""
The Composite Pattern is a structural design pattern that allows you to compose objects into tree-like structures to represent part-whole hierarchies.
This pattern lets clients treat individual objects and compositions of objects uniformly.

*** Composite Pattern Explained Intuitively ***
Imagine a Filesystem

1. Part-Whole Hierarchy

Folders and Files: Think of a filesystem where you have files and folders. A folder can contain multiple files and other folders, forming a tree-like structure.
Both files and folders should be treated the same way when performing operations like size calculation or listing contents.

2. Uniform Treatment

By using the Composite Pattern, you can treat files and folders uniformly, performing operations on them without knowing if they are individual files or compositions of files (folders).

*** Structure ***
Component: The base interface for all objects in the composition, declaring common operations.
Leaf: Represents individual objects in the composition. Implements the Component interface.
Composite: Represents a composition of objects (can contain Leaf or other Composite objects). Implements the Component interface and defines methods to manage child components.

*** Example: Financial Portfolio Management ***
Let’s use the Composite Pattern in the context of financial portfolio management, where we might want to represent a portfolio of investments,
which can include individual investments and groups of investments.

"""

#========================= Component =========================

# Define the base interface for all objects in the composition

from abc import ABC, abstractmethod

class Investment(ABC):
    @abstractmethod
    def get_value(self) -> float:
        pass

#========================= Leaf =========================

# Represent individual investments

class Stock(Investment):
    def __init__(self, name: str, value: float):
        self.name = name
        self.value = value

    def get_value(self) -> float:
        return self.value

class Bond(Investment):
    def __init__(self, name: str, value: float):
        self.name = name
        self.value = value

    def get_value(self) -> float:
        return self.value

#========================= Composite =========================

# Represent groups of investments

class Portfolio(Investment):
    def __init__(self, name: str):
        self.name = name
        self._investments = []

    def add_investment(self, investment: Investment):
        self._investments.append(investment)

    def remove_investment(self, investment: Investment):
        self._investments.remove(investment)

    def get_value(self) -> float:
        total_value = sum(investment.get_value() for investment in self._investments)
        return total_value

#========================= Client Code =========================

# Use the composite structure to manage the portfolio

# Client Code
if __name__ == "__main__":
    # Create individual investments
    stock1 = Stock("AAPL", 150.0)
    stock2 = Stock("GOOGL", 200.0)
    bond1 = Bond("US Treasury", 100.0)

    # Create a portfolio and add investments
    tech_portfolio = Portfolio("Tech Portfolio")
    tech_portfolio.add_investment(stock1)
    tech_portfolio.add_investment(stock2)

    # Create another portfolio
    main_portfolio = Portfolio("Main Portfolio")
    main_portfolio.add_investment(tech_portfolio)
    main_portfolio.add_investment(bond1)

    # Calculate the total value of the main portfolio
    total_value = main_portfolio.get_value()
    print(f"Total value of the main portfolio: {total_value}")  # Output: Total value of the main portfolio: 450.0

#======================= How It Works =======================

"""
*** Component ***
Investment is the abstract base class that declares the common operation get_value.

*** Leaf ***
Stock and Bond are leaf classes representing individual investments. They implement the get_value method.

*** Composite ***
Portfolio is the composite class that can contain multiple Investment objects (both leaf and composite). It implements the get_value method by summing the values of its child investments.

"""
"""
The Flyweight Pattern is a structural design pattern that aims to minimize memory usage by sharing as much data as possible with similar objects.
It is particularly useful when dealing with a large number of similar objects, where many of them can share common data to save memory.

*** Purpose ***
The primary purpose of the Flyweight Pattern is to reduce memory usage and improve performance by sharing common parts of the object state among multiple objects.

*** Intuition ***
Imagine you are developing a financial trading application that handles a large number of transactions.
Each transaction has common data (e.g., trade type, symbol) and unique data (e.g., trade ID, timestamp).
Instead of storing all data in each transaction object, you can share the common data across multiple transactions.

*** Structure ***
Flyweight: Declares an interface through which flyweights can receive and act on extrinsic state.
ConcreteFlyweight: Implements the Flyweight interface and stores intrinsic state.
FlyweightFactory: Creates and manages flyweight objects, ensuring that flyweights are shared properly.
Client: Maintains references to flyweights and computes extrinsic states.

*** Example: Financial Transactions ***
Let's consider an example of financial transactions in a trading application.
"""

#============================= Flyweight Interface =============================

# Define the flyweight interface for financial transactions

from abc import ABC, abstractmethod

class Transaction(ABC):
    @abstractmethod
    def execute(self, unique_data: dict) -> None:
        pass

#============================= Concrete Flyweight =============================

# Implement the concrete flyweight class for financial transactions

class TradeTransaction(Transaction):
    def __init__(self, trade_type: str, symbol: str):
        self.trade_type = trade_type
        self.symbol = symbol

    def execute(self, unique_data: dict) -> None:
        print(f"Executing {self.trade_type} trade for {self.symbol}")
        print(f"Unique Data: {unique_data}")

#============================= Flyweight Factory =============================

# Create a flyweight factory to manage and share flyweight objects

class TransactionFactory:
    _transactions = {}

    @classmethod
    def get_transaction(cls, trade_type: str, symbol: str) -> TradeTransaction:
        key = (trade_type, symbol)
        if key not in cls._transactions:
            cls._transactions[key] = TradeTransaction(trade_type, symbol)
        return cls._transactions[key]

#============================= Client Code =============================

# Use the flyweight factory to manage transactions in the client code

if __name__ == "__main__":
    # Create a transaction factory
    factory = TransactionFactory()

    # Unique data for transactions
    unique_data1 = {'trade_id': 'T001', 'timestamp': '2024-07-29 10:00:00'}
    unique_data2 = {'trade_id': 'T002', 'timestamp': '2024-07-29 10:05:00'}
    unique_data3 = {'trade_id': 'T003', 'timestamp': '2024-07-29 10:10:00'}

    # Get shared flyweight objects and execute transactions
    transaction1 = factory.get_transaction('buy', 'AAPL')
    transaction1.execute(unique_data1)

    transaction2 = factory.get_transaction('buy', 'AAPL')
    transaction2.execute(unique_data2)

    transaction3 = factory.get_transaction('sell', 'TSLA')
    transaction3.execute(unique_data3)

    # Verify that shared objects are reused
    print(f"Transaction1 and Transaction2 are the same object: {transaction1 is transaction2}")
    print(f"Transaction1 and Transaction3 are the same object: {transaction1 is transaction3}")


#============================= How It Works  =============================

"""
1. Flyweight Interface
Transaction is the interface for flyweight objects, declaring the execute method that takes unique data as a parameter.

2. Concrete Flyweight
TradeTransaction implements the Transaction interface and stores the intrinsic state (trade_type and symbol).

3. Flyweight Factory
TransactionFactory creates and manages shared TradeTransaction objects. It ensures that the same TradeTransaction object is reused for the same trade_type and symbol.

4. Client Code
The client code uses the TransactionFactory to obtain shared TradeTransaction objects and executes them with unique data.

"""
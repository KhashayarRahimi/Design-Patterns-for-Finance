"""
The Iterator Pattern is a behavioral design pattern that provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
This pattern is particularly useful for traversing collections like lists, trees, or other complex data structures.

*** Purpose ***
The primary purpose of the Iterator Pattern is to separate the traversal logic from the actual data structure, allowing different ways to traverse the structure without modifying it.

*** Intuition ***
Imagine you have a collection of financial transactions, and you want to iterate through them to perform various operations, such as calculating totals or generating reports.
The Iterator Pattern allows you to traverse these transactions sequentially without exposing the internal details of the collection.

*** Structure ***
1. Iterator Interface: Declares the interface for accessing and traversing elements.
2. Concrete Iterator: Implements the iterator interface and keeps track of the current position in the traversal.
3. Aggregate Interface: Declares an interface for creating an iterator object.
4. Concrete Aggregate: Implements the aggregate interface and returns an instance of the concrete iterator.

*** Example: Financial Transactions ***
Let's consider an example where we have a collection of financial transactions, and we want to iterate through them.

"""

#========================== Iterator Interface ==========================

# Define the iterator interface

from abc import ABC, abstractmethod
from typing import Any

class Iterator(ABC):
    @abstractmethod
    def next(self) -> Any:
        pass

    @abstractmethod
    def has_next(self) -> bool:
        pass


#========================== Concrete Iterator ==========================

# Implement the concrete iterator

class TransactionIterator(Iterator):
    def __init__(self, transactions):
        self._transactions = transactions
        self._index = 0

    def next(self) -> Any:
        if self.has_next():
            transaction = self._transactions[self._index]
            self._index += 1
            return transaction
        else:
            raise StopIteration

    def has_next(self) -> bool:
        return self._index < len(self._transactions)
    
#========================== Aggregate Interface ==========================

# Define the aggregate interface

from abc import ABC, abstractmethod

class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass

#========================== Concrete Aggregate ==========================

# Implement the concrete aggregate

class TransactionCollection(Aggregate):
    def __init__(self):
        self._transactions = []

    def add_transaction(self, transaction):
        self._transactions.append(transaction)

    def create_iterator(self) -> Iterator:
        return TransactionIterator(self._transactions)

#========================== Client Code ==========================

# Use the iterator in the client code to traverse the transactions

if __name__ == "__main__":
    # Create a collection of transactions
    transactions = TransactionCollection()
    transactions.add_transaction({"id": 1, "amount": 100})
    transactions.add_transaction({"id": 2, "amount": 200})
    transactions.add_transaction({"id": 3, "amount": 300})

    # Create an iterator for the transactions
    iterator = transactions.create_iterator()

    # Traverse the transactions using the iterator
    while iterator.has_next():
        transaction = iterator.next()
        print(f"Transaction ID: {transaction['id']}, Amount: {transaction['amount']}")

#========================== How It Works ==========================

"""
1. Iterator Interface
Iterator is the interface that declares methods for traversing elements (next and has_next).

2. Concrete Iterator
TransactionIterator implements the Iterator interface and keeps track of the current position in the transaction list.

3. Aggregate Interface
Aggregate is the interface that declares a method for creating an iterator (create_iterator).

4. Concrete Aggregate
TransactionCollection implements the Aggregate interface and returns an instance of the TransactionIterator.

5. Client Code
The client creates a collection of transactions and an iterator to traverse them. The iterator handles the traversal logic, while the client uses it to access each transaction.

"""
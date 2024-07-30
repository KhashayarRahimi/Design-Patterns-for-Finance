"""

The Chain of Responsibility Pattern is a behavioral design pattern that allows a request to be passed along a chain of handlers.
Each handler in the chain processes the request or passes it to the next handler in the chain.
This pattern decouples the sender of a request from its receiver, allowing multiple handlers to handle the request without the sender needing to know which handler will handle it.

*** Purpose ***
The primary purpose of the Chain of Responsibility Pattern is to avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request.
This pattern can be used when multiple objects might handle a request, and the handler is not known in advance.

*** Intuition ***
Imagine you are developing a financial transaction approval system where transactions need to go through various levels of approval (e.g., manager, senior manager, director).
Each level can either approve the transaction or pass it to the next level. The Chain of Responsibility Pattern is perfect for this scenario.

*** Structure ***
1. Handler Interface: Declares a method for handling requests and an optional method for setting the next handler in the chain.
2. Concrete Handlers: Implement the handler interface and handle requests or pass them to the next handler.
3. Client: Initiates the request to a handler in the chain.

*** Example: Financial Transaction Approval ***
Let's consider an example where financial transactions need approval from different levels of authority.

"""

#====================================== Handler Interface ======================================

# Define the handler interface for approving transactions

from abc import ABC, abstractmethod

class Approver(ABC):
    @abstractmethod
    def set_next(self, approver: 'Approver') -> 'Approver':
        pass

    @abstractmethod
    def approve(self, amount: float) -> None:
        pass

#====================================== Concrete Handlers ======================================

# Implement the concrete handlers for different levels of approval

class Manager(Approver):
    def __init__(self):
        self._next_approver = None

    def set_next(self, approver: 'Approver') -> 'Approver':
        self._next_approver = approver
        return approver

    def approve(self, amount: float) -> None:
        if amount <= 1000:
            print("Manager approves the transaction.")
        elif self._next_approver:
            self._next_approver.approve(amount)
        else:
            print("Transaction requires higher approval.")

class SeniorManager(Approver):
    def __init__(self):
        self._next_approver = None

    def set_next(self, approver: 'Approver') -> 'Approver':
        self._next_approver = approver
        return approver

    def approve(self, amount: float) -> None:
        if amount <= 5000:
            print("Senior Manager approves the transaction.")
        elif self._next_approver:
            self._next_approver.approve(amount)
        else:
            print("Transaction requires higher approval.")

class Director(Approver):
    def __init__(self):
        self._next_approver = None

    def set_next(self, approver: 'Approver') -> 'Approver':
        self._next_approver = approver
        return approver

    def approve(self, amount: float) -> None:
        if amount <= 10000:
            print("Director approves the transaction.")
        elif self._next_approver:
            self._next_approver.approve(amount)
        else:
            print("Transaction requires board approval.")

#====================================== Client Code ======================================

# Use the chain of responsibility in the client code to handle transaction approval

if __name__ == "__main__":
    # Create the chain of approvers
    manager = Manager()
    senior_manager = SeniorManager()
    director = Director()

    # Set up the chain: Manager -> Senior Manager -> Director
    manager.set_next(senior_manager).set_next(director)

    # Test the chain with different amounts
    transaction_amounts = [500, 2000, 7000, 15000]

    for amount in transaction_amounts:
        print(f"\nProcessing transaction for amount: ${amount}")
        manager.approve(amount)

#====================================== How It Works ======================================

"""
1. Handler Interface
Approver is the interface that declares methods for setting the next handler (set_next) and for handling the request (approve).

2. Concrete Handlers
Manager, SeniorManager, and Director are concrete handlers that implement the Approver interface. Each handler processes the request or passes it to the next handler in the chain.

3. Client Code
The client sets up the chain of responsibility by linking the handlers. It then initiates requests by calling the approve method on the first handler in the chain.

"""
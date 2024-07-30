"""
The State Pattern is a behavioral design pattern that allows an object to change its behavior when its internal state changes.
This pattern is particularly useful when an object needs to change its behavior based on its state, and it helps to avoid conditional statements for state-dependent behavior.

*** Purpose ***
The primary purpose of the State Pattern is to encapsulate state-specific behavior and delegate state-related responsibilities to individual state objects.
This makes the code more maintainable and flexible by promoting the Single Responsibility Principle.

*** Intuition ***
Imagine you are developing a trading system where an order can be in different states, such as New, Filled, or Cancelled.
Each state has specific behavior associated with it.
The State Pattern allows you to encapsulate these behaviors in separate state classes and delegate the state-dependent behavior to these classes.

*** Structure ***
1. Context: Maintains an instance of a Concrete State subclass that defines the current state.
2. State Interface: Declares methods that concrete states should implement.
3. Concrete States: Implement behavior associated with a state of the Context.

*** Example: Trading System Order States ***
Let's consider an example where we have a trading system with different order states (New, Filled, Cancelled).

"""

#===================================== State Interface =====================================

# Define the state interface

from abc import ABC, abstractmethod

class OrderState(ABC):
    @abstractmethod
    def process(self, order):
        pass

    @abstractmethod
    def cancel(self, order):
        pass


#===================================== Concrete States =====================================

# Implement the concrete states

class NewOrderState(OrderState):
    def process(self, order):
        print("Processing new order.")
        order.set_state(FilledOrderState())

    def cancel(self, order):
        print("Cancelling new order.")
        order.set_state(CancelledOrderState())

class FilledOrderState(OrderState):
    def process(self, order):
        print("Order already filled.")

    def cancel(self, order):
        print("Cancelling filled order.")
        order.set_state(CancelledOrderState())

class CancelledOrderState(OrderState):
    def process(self, order):
        print("Cannot process a cancelled order.")

    def cancel(self, order):
        print("Order already cancelled.")

#===================================== Contexts =====================================

# Implement the context class

class Order:
    def __init__(self):
        self._state = NewOrderState()

    def set_state(self, state: OrderState):
        self._state = state

    def process(self):
        self._state.process(self)

    def cancel(self):
        self._state.cancel(self)

#===================================== Client Code =====================================

# Use the state pattern in the client code to manage order states

if __name__ == "__main__":
    order = Order()

    # Initial state is NewOrderState
    order.process()  # Output: Processing new order.
    order.cancel()   # Output: Cancelling filled order.

    # Try to process a cancelled order
    order.process()  # Output: Cannot process a cancelled order.
    order.cancel()   # Output: Order already cancelled.

#===================================== How It Works =====================================

"""
1. State Interface
OrderState is an abstract class that declares methods (process and cancel) to be implemented by concrete state classes.

2. Concrete States
NewOrderState, FilledOrderState, and CancelledOrderState are concrete implementations of OrderState. They encapsulate behavior specific to each state.

3. Context
Order is the context class that maintains a reference to the current state. It delegates state-specific behavior to the current state object.

4. Client Code
The client interacts with the Order object, which delegates behavior to its current state. The state transitions are managed internally by changing the state reference.

"""
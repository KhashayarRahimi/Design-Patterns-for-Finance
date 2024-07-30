"""
The Strategy Pattern is a behavioral design pattern that defines a family of algorithms, encapsulates each one, and makes them interchangeable.
The pattern allows the algorithm to vary independently from clients that use it. It is often used to enable selecting an algorithm at runtime without changing the client code.

*** Purpose ***
The primary purpose of the Strategy Pattern is to define a set of interchangeable algorithms or behaviors and make them easily switchable.
This allows the algorithm or behavior to be selected dynamically based on the context without modifying the client code.

*** Intuition ***
Imagine you are developing a payment processing system where different payment methods (credit card, PayPal, etc.) are available.
Using the Strategy Pattern, you can define each payment method as a strategy and switch between them based on user preference or other factors.
This makes it easy to add or change payment methods without altering the main payment processing code.

*** Structure ***
1. Context: Maintains a reference to a strategy object and can replace it at runtime.
2. Strategy: Defines the interface for the algorithm or behavior.
3. ConcreteStrategy: Implements the Strategy interface and defines specific algorithms or behaviors.

*** Example: Payment Processing System ***
Let's consider an example where we have different payment methods in an e-commerce application.
"""

#======================================= Strategy Interface =======================================

# Define the strategy interface

from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

#======================================= Concrete Strategies =======================================


# Implement concrete strategies for different payment methods

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"Paying {amount} using credit card {self.card_number}")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paying {amount} using PayPal account {self.email}")

#======================================= Context =======================================


# Define the context that uses a payment strategy

class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def execute_payment(self, amount):
        self._strategy.pay(amount)

#======================================= Client Code =======================================

# Use the strategy pattern in the client code to process payments

if __name__ == "__main__":
    # Create different payment strategies
    credit_card_payment = CreditCardPayment(card_number="1234-5678-9876-5432")
    paypal_payment = PayPalPayment(email="user@example.com")

    # Create payment context with credit card payment strategy
    payment_context = PaymentContext(credit_card_payment)
    payment_context.execute_payment(100)  # Output: Paying 100 using credit card 1234-5678-9876-5432

    # Change strategy to PayPal and execute payment
    payment_context.set_strategy(paypal_payment)
    payment_context.execute_payment(200)  # Output: Paying 200 using PayPal account user@example.com

#======================================= How It Works =======================================


"""
1. Strategy Interface
PaymentStrategy defines the interface for the payment algorithm, with a method pay that concrete strategies must implement.

2. Concrete Strategies:
CreditCardPayment and PayPalPayment are concrete implementations of the PaymentStrategy interface, each providing a specific way to process payments.

3. Context
PaymentContext maintains a reference to a PaymentStrategy and can switch strategies at runtime using the set_strategy method. It delegates the payment processing to the current strategy.

4. Client Code
The client creates instances of different payment strategies, sets them in the context, and executes payments. The context uses the strategy to perform the payment.
"""
"""
The Memento Pattern is a behavioral design pattern that allows an object to save and restore its previous state without revealing the details of its implementation.
This pattern is useful when you want to implement undo functionality or rollback to a previous state in an application.

*** Purpose ***
The primary purpose of the Memento Pattern is to capture and externalize an object's internal state so that it can be restored later, without violating encapsulation.

*** Intuition ***
Imagine you are developing a financial application that processes transactions.
If an error occurs during a transaction,you might want to rollback to the previous state before the transaction started.
The Memento Pattern allows you to save the state of the system before the transaction and restore it if necessary.

*** Structure ***
1. Memento: Stores the internal state of the Originator object. The Memento can have two interfaces: one for the Originator to store and restore the state, and one for other objects (Caretaker) to get the Memento.
2. Originator: Creates a Memento containing a snapshot of its current internal state and uses the Memento to restore its state.
3. Caretaker: Is responsible for the Memento's safekeeping. It never operates on or examines the contents of a Memento.

*** Example: Financial Transaction Rollback ***
Let's consider an example where we have a financial system that processes transactions, and we want to implement rollback functionality using the Memento Pattern.

"""

#=================================== Memento ===================================

# Define the Memento class to store the state

class Memento:
    def __init__(self, balance):
        self._balance = balance

    def get_saved_state(self):
        return self._balance

#=================================== Originator ===================================

# Implement the Originator class that creates and restores Memento objects

class Account:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def get_balance(self):
        return self._balance

    def save_state(self):
        return Memento(self._balance)

    def restore_state(self, memento):
        self._balance = memento.get_saved_state()

#=================================== Caretaker ===================================

# Implement the Caretaker class that manages the Memento objects

class Caretaker:
    def __init__(self, account):
        self._account = account
        self._history = []

    def save(self):
        self._history.append(self._account.save_state())

    def undo(self):
        if not self._history:
            print("No states to restore")
            return
        memento = self._history.pop()
        self._account.restore_state(memento)

#=================================== Client Code ===================================

# Use the Memento Pattern in the client code to manage account transactions

if __name__ == "__main__":
    account = Account()
    caretaker = Caretaker(account)

    # Initial deposit
    account.deposit(100)
    print(f"Balance after deposit: {account.get_balance()}")  # Output: 100

    # Save state
    caretaker.save()

    # Perform some transactions
    account.deposit(50)
    print(f"Balance after deposit: {account.get_balance()}")  # Output: 150

    account.withdraw(30)
    print(f"Balance after withdrawal: {account.get_balance()}")  # Output: 120

    # Save state
    caretaker.save()

    # Perform another transaction
    account.withdraw(100)
    print(f"Balance after withdrawal: {account.get_balance()}")  # Output: 20

    # Undo last transaction
    caretaker.undo()
    print(f"Balance after undo: {account.get_balance()}")  # Output: 120

    # Undo to initial state
    caretaker.undo()
    print(f"Balance after undo: {account.get_balance()}")  # Output: 100

#=================================== How It Works ===================================


"""

1. Memento
Memento stores the internal state of the Account object. It has a method get_saved_state to retrieve the stored state.

2. Originator
Account acts as the Originator. It can create a Memento of its current state using save_state and restore its state using restore_state.

3. Caretaker
Caretaker is responsible for saving and restoring the Memento objects. It keeps a history of Memento objects and can undo the last state by popping the last Memento from the history.

4. Client Code
The client code interacts with the Account and Caretaker objects to perform transactions and manage the state history.

"""
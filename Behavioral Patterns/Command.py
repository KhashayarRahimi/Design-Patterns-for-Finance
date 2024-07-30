"""

The Command Pattern is a behavioral design pattern that turns a request into a stand-alone object containing all information about the request.
This pattern allows you to parameterize objects with operations, queue or log requests, and support undoable operations.

*** Purpose ***
The primary purpose of the Command Pattern is to encapsulate a request as an object, thus allowing you to parameterize clients with queues, requests, and operations.
It decouples the sender of a request from the receiver, enabling more flexible and dynamic command handling.

*** Intuition ***
Imagine you are developing a trading application where users can execute various trading commands, such as buy, sell, or cancel orders.
Using the Command Pattern, you can encapsulate each trading command as an object, allowing you to queue commands, execute them, or even undo them if necessary.

*** Structure ***
1. Command: Declares an interface for executing a command.
2. ConcreteCommand: Implements the Command interface and defines the binding between a receiver object and an action.
3. Client: Creates a ConcreteCommand object and sets its receiver.
4. Invoker: Asks the command to execute the request.
5. Receiver: Knows how to perform the operations required to fulfill a request.

*** Example: Trading System Commands ***
Let's consider an example where we have a trading system that allows users to execute buy and sell commands.

"""

#======================================  Command Interface ======================================

# Define the Command interface

from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

#======================================  Concrete Commands ======================================

# Implement the concrete commands

class BuyOrderCommand(Command):
    def __init__(self, trader, amount):
        self._trader = trader
        self._amount = amount

    def execute(self):
        self._trader.buy(self._amount)

class SellOrderCommand(Command):
    def __init__(self, trader, amount):
        self._trader = trader
        self._amount = amount

    def execute(self):
        self._trader.sell(self._amount)

#======================================  Receiver ======================================

# Implement the receiver class that performs the actual operations

class Trader:
    def buy(self, amount):
        print(f"Buying {amount} units")

    def sell(self, amount):
        print(f"Selling {amount} units")

#====================================== Invoker ======================================

# Implement the invoker class that requests the command execution

class Broker:
    def __init__(self):
        self._commands = []

    def add_command(self, command: Command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()
        self._commands = []

#====================================== Client Code ======================================

# Use the command pattern in the client code

if __name__ == "__main__":
    trader = Trader()

    # Create commands
    buy_command = BuyOrderCommand(trader, 100)
    sell_command = SellOrderCommand(trader, 50)

    # Create broker and add commands
    broker = Broker()
    broker.add_command(buy_command)
    broker.add_command(sell_command)

    # Execute all commands
    broker.execute_commands()
    # Output:
    # Buying 100 units
    # Selling 50 units


#====================================== How It Works ======================================


"""
1. Command Interface
Command declares the execute method, which concrete commands must implement.

2. Concrete Commands
BuyOrderCommand and SellOrderCommand implement the Command interface and encapsulate the actions required to execute buy and sell operations.

3. Receiver
Trader is the receiver class that performs the actual buy and sell operations.

4. Invoker
Broker is the invoker class that manages and executes commands. It stores a list of commands and calls the execute method on each one.

5. Client Code
The client creates instances of the concrete commands, adds them to the invoker, and then executes the commands. The invoker handles the execution, delegating it to the appropriate receiver.

"""
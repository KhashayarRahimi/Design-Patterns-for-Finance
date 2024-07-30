"""
The Mediator Pattern is a behavioral design pattern that defines an object that encapsulates how a set of objects interact.
This pattern promotes loose coupling by keeping objects from referring to each other explicitly, and it allows their interaction to be managed by a central mediator object.

*** Purpose ***
The primary purpose of the Mediator Pattern is to reduce the complexity of communication between objects by centralizing their interaction in a single mediator.
This helps in reducing the dependency between objects and making the system more maintainable and scalable.

*** Intuition ***
Imagine you are building a chat application where multiple users can send and receive messages.
Without a mediator, each user would need to know about every other user to send a message.
Using the Mediator Pattern, you can introduce a central mediator (like a chat server) that manages the communication between users, simplifying the interactions and reducing dependencies.

*** Structure ***
1. Mediator: Declares an interface for communication between Colleagues.
2. ConcreteMediator: Implements the Mediator interface and coordinates communication between Colleagues.
3. Colleague: Defines an interface for communication with other Colleagues via the Mediator.
4. ConcreteColleague: Implements the Colleague interface and communicates with other Colleagues through the Mediator.

*** Example: Chat Application ***
Let's consider an example of a chat application where users (Colleagues) communicate through a chat server (Mediator).
"""

#========================================== Mediator Interface ==========================================

# Define the mediator interface

from abc import ABC, abstractmethod

class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, message: str, user: 'User'):
        pass

#========================================== Concrete Mediator ==========================================


# Implement the concrete mediator that manages communication between users

class ConcreteChatMediator(ChatMediator):
    def __init__(self):
        self._users = []

    def add_user(self, user: 'User'):
        self._users.append(user)
        user.set_mediator(self)

    def send_message(self, message: str, user: 'User'):
        for u in self._users:
            if u != user:
                u.receive_message(message)

#========================================== Colleague Interfacer ==========================================


# Define the colleague interface

class User(ABC):
    def __init__(self, name: str):
        self._name = name
        self._mediator = None

    def set_mediator(self, mediator: ChatMediator):
        self._mediator = mediator

    @abstractmethod
    def send_message(self, message: str):
        pass

    @abstractmethod
    def receive_message(self, message: str):
        pass


#========================================== Concrete Colleagues ==========================================


# Implement the concrete colleagues (users)

class ConcreteUser(User):
    def send_message(self, message: str):
        print(f"{self._name} sends: {message}")
        self._mediator.send_message(message, self)

    def receive_message(self, message: str):
        print(f"{self._name} receives: {message}")

#========================================== Client Code ==========================================


# Use the mediator pattern in the client code to manage user communication

if __name__ == "__main__":
    mediator = ConcreteChatMediator()

    user1 = ConcreteUser("Alice")
    user2 = ConcreteUser("Bob")
    user3 = ConcreteUser("Charlie")

    mediator.add_user(user1)
    mediator.add_user(user2)
    mediator.add_user(user3)

    user1.send_message("Hello, everyone!")
    user2.send_message("Hi Alice!")

#========================================== How It Works ==========================================

"""
1. Mediator Interface
ChatMediator declares an interface for communication between Colleagues.

2. Concrete Mediator
ConcreteChatMediator implements the mediator interface and manages the list of users. It coordinates the sending and receiving of messages between users.

3. Colleague Interface
User defines the methods for sending and receiving messages. It also has a reference to the mediator.

4. Concrete Colleagues
ConcreteUser implements the user interface. It sends and receives messages through the mediator.

5. Client Code
The client creates instances of the mediator and users, sets up the users with the mediator, and uses the mediator to handle communication.

"""
"""

The Observer Pattern is a behavioral design pattern that defines a one-to-many dependency between objects so that when one object (the subject) changes its state,
all its dependents (observers) are automatically notified and updated. This pattern is commonly used to implement distributed event-handling systems.

*** Purpose ***
The primary purpose of the Observer Pattern is to create a system where one object (the subject) can notify multiple objects (observers) about changes in its state
without being tightly coupled to them. This helps in maintaining a consistent state across multiple objects and allows for dynamic and flexible interactions.

*** Intuition ***
Imagine you are building a weather monitoring application where multiple displays show different weather metrics (temperature, humidity, etc.).
When the weather data updates, all the displays need to be updated accordingly.
Using the Observer Pattern, you can have the weather data (the subject) notify all the displays (observers) when the data changes, keeping them synchronized.

*** Structure ***
1. Subject: Defines an interface for attaching and detaching observers and notifying them of changes.
2. ConcreteSubject: Implements the Subject interface and maintains the state. It notifies observers when the state changes.
3. Observer: Defines an interface for receiving updates from the subject.
4. ConcreteObserver: Implements the Observer interface and updates its state based on notifications from the subject.

*** Example: Weather Monitoring System ***
Let's consider an example where we have a weather monitoring system with multiple displays.

"""

#======================================= Subject Interface =======================================


# Define the subject interface

from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

#======================================= Concrete Subject =======================================


# Implement the concrete subject that maintains the state and notifies observers

class WeatherData(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = 0

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify()

#======================================= Observer Interface =======================================

# Define the observer interface

class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

#======================================= Concrete Observers =======================================

# Implement concrete observers (displays)


class TemperatureDisplay(Observer):
    def update(self, temperature):
        print(f"Temperature Display: Current temperature is {temperature}°C")

class HumidityDisplay(Observer):
    def update(self, temperature):
        # For simplicity, let's say humidity depends on temperature
        humidity = 100 - temperature
        print(f"Humidity Display: Current humidity is {humidity}%")

#======================================= Client Code =======================================

# Use the observer pattern in the client code to update displays when weather data changes:

if __name__ == "__main__":
    weather_data = WeatherData()

    temp_display = TemperatureDisplay()
    humidity_display = HumidityDisplay()

    weather_data.attach(temp_display)
    weather_data.attach(humidity_display)

    # Set new temperature and notify observers
    weather_data.set_temperature(25)
    # Output:
    # Temperature Display: Current temperature is 25°C
    # Humidity Display: Current humidity is 75%

    # Set another temperature
    weather_data.set_temperature(30)
    # Output:
    # Temperature Display: Current temperature is 30°C
    # Humidity Display: Current humidity is 70%

#======================================= How It Works =======================================

"""
1. Subject Interface
Subject declares methods for attaching, detaching, and notifying observers.

2. Concrete Subject
WeatherData implements the Subject interface and maintains the temperature state. It notifies observers when the temperature changes.

3. Observer Interface
Observer declares the update method that observers must implement to receive updates.

4. Concrete Observers:
TemperatureDisplay and HumidityDisplay implement the Observer interface and update their display based on the temperature.

5. Client Code
The client creates instances of the subject and observers, attaches the observers to the subject, and sets new temperatures.
The subject notifies the observers of changes, and they update accordingly.
"""
"""
The Singleton Pattern is a design pattern that ensures a class has only one instance and provides a global point of access to that instance.
It’s particularly useful when exactly one instance of a class is needed throughout the lifetime of an application.

*** Singleton Pattern Explained Intuitively ***

Imagine a Global Configuration Manager

*** Single Instance ***
Singleton: Think of a Singleton as a global configuration manager for an application.
You want this manager to be unique—there should be only one instance managing all configuration settings.

*** Global Access ***
Global Access Point: The Singleton pattern provides a global access point to this unique instance,
so every part of the application can access the same configuration manager.

*** Structure ***
Singleton Class: The class that ensures there is only one instance.
It typically provides a method to access that instance and controls the instantiation process.

Instance: The single instance of the class that is created and used throughout the application.

Example: Logging System
Let’s use the Singleton Pattern to manage a logging system in a financial application.
We want a single logging instance to handle all log messages consistently across the application.

"""

class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):  # Avoid re-initialization
            self.log_file = "application.log"
            self.initialized = True

    def log(self, message: str) -> None:
        with open(self.log_file, "a") as file:
            file.write(message + "\n")

# Example Usage
if __name__ == "__main__":
    logger1 = Logger()
    logger2 = Logger()

    logger1.log("This is the first log message.")
    logger2.log("This is the second log message.")

    # Check if both logger1 and logger2 are the same instance
    print(f"logger1 is logger2: {logger1 is logger2}")  # Output: True

#============================== How It Works? ==============================

"""
*** Private Constructor ***
The __new__ method ensures that only one instance of the class is created.
If _instance is None, it creates a new instance; otherwise, it returns the existing instance.

*** Global Access Point ***
The Logger class provides a global access point via the __new__ method. Every call to Logger() returns the same instance.

*** Instance Initialization ***
The __init__ method ensures that the logger is initialized only once. The initialized attribute prevents re-initialization.

"""
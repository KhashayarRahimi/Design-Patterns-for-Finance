"""
The Prototype Pattern is a design pattern used to create new objects by copying an existing object, known as a prototype.
This is particularly useful when the cost of creating a new object is more expensive than copying an existing one.
Here’s a detailed and intuitive explanation of the Prototype Pattern:

---- Prototype Pattern Explained Intuitively ----

Imagine You’re Creating Custom Products

*** Prototype ***
Prototype: Think of the prototype as a master template for a product.
For example, if you have a prototype for a high-end luxury car, you can create new cars based on this prototype.

*** Copying the Prototype ***
Cloning: Instead of designing each car from scratch, you can clone the prototype.
This is like copying the design and features of the existing car to create a new one.
The new car will have the same basic design but can be customized further if needed.

*** Structure *** 
Prototype: An interface or abstract class defining a method for cloning itself.
ConcretePrototype: Implements the clone method defined by the Prototype. It represents the actual object that can be copied.
Client: Uses the prototype to create new objects by cloning it.
"""

from abc import ABC, abstractmethod
from copy import deepcopy

class StrategyPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class TradingStrategy(StrategyPrototype):
    def __init__(self, risk_level: str, trading_frequency: str, asset_allocation: dict):
        self.risk_level = risk_level
        self.trading_frequency = trading_frequency
        self.asset_allocation = asset_allocation

    def clone(self):
        # Use deep copy to create a clone of the object
        return deepcopy(self)
    
    def __str__(self):
        return (f"TradingStrategy(risk_level={self.risk_level}, "
                f"trading_frequency={self.trading_frequency}, "
                f"asset_allocation={self.asset_allocation})")

# Client Code
if __name__ == "__main__":
    # Create an initial strategy
    original_strategy = TradingStrategy(
        risk_level="Medium",
        trading_frequency="Weekly",
        asset_allocation={"Stocks": 0.5, "Bonds": 0.5}
    )
    print(f"Original Strategy: {original_strategy}")

    # Clone the original strategy to create a new one
    cloned_strategy = original_strategy.clone()
    print(f"Cloned Strategy: {cloned_strategy}")

    # Modify the cloned strategy
    cloned_strategy.asset_allocation["Real Estate"] = 0.1
    print(f"Modified Cloned Strategy: {cloned_strategy}")


#============================= Why Use the Prototype Pattern? =============================
"""
1. Avoiding Expensive Object Creation

When creating an object is costly (in terms of time or resources), copying an existing object (prototype) can be more efficient. This is particularly useful for complex objects or when initial setup is resource-intensive.

2. Simplifying Object Creation

The Prototype Pattern simplifies the creation process by allowing you to clone an existing object and then make modifications. This avoids the need to set up the object from scratch.

3. Flexibility

It provides a flexible approach to object creation. You can create different variations of an object by cloning a prototype and then adjusting the cloned object as needed.

4. Managing Complex Object Structures

For objects with complex internal structures or states, cloning a prototype is easier than creating a new object from scratch. This is especially true when dealing with objects that have many interrelated components.

"""
#============================= Benefits =============================
"""
1. Efficiency

Cloning an existing object is often more efficient than constructing a new one from scratch, especially if the setup process is complex.

2. Flexibility

Allows for easy creation of new instances with variations based on an existing prototype. This is useful for scenarios where objects are similar but need some customization.

3. Consistency

Ensures that new objects are consistent with the prototype, reducing the risk of errors or inconsistencies in object creation.

4. Simplifies Object Creation

By using cloning, you avoid the complexities involved in creating complex objects from scratch.

"""
"""
Imagine You’re Building a Custom Sandwich

*** The Sandwich ***
Product: Think of the final sandwich as the complex object you want to create. A sandwich can have many different components like bread, meat, cheese, veggies, and sauces.

*** Building Process ***
Builder: This is like the person making the sandwich. They follow a recipe to assemble the sandwich but can vary the ingredients and their combinations based on what you want.

*** Recipes ***
ConcreteBuilder: This is a specific type of sandwich maker with their own set of recipes. For example, one recipe might be for a classic ham sandwich, while another is for a veggie delight.

*** Instructions ***
Director: This is like a chef who tells the sandwich maker (builder) what type of sandwich to make. They might say, “Make a basic ham sandwich,” or “Make a deluxe veggie sandwich,” providing the specific instructions for how to assemble it.

===================================================

Breaking It Down
*** Product (The Sandwich)***
This is the end result. A complex sandwich with various ingredients and flavors, depending on what you choose.

*** Builder (Sandwich Maker) ***
Defines how to assemble the sandwich. This involves adding layers of ingredients, choosing types of bread, adding condiments, etc. It provides the methods for adding each part.

*** ConcreteBuilder (Specific Recipes) ***
Implements the specific way to make different sandwiches. For example, one builder might focus on making traditional sandwiches, while another might specialize in gourmet options.

*** Director (Chef) ***
Provides instructions to the builder on how to create a specific type of sandwich. They ensure that the builder follows the right steps to create the desired sandwich.

---- Example: Building a Financial Trading Strategy ----

*** TradingStrategy (Product) ***
This is the complex object you're creating, like a comprehensive trading strategy that includes various parameters.

*** StrategyBuilder (Builder) ***
Defines methods for setting different components of the trading strategy, such as risk level, trading frequency, and asset allocation.

*** ConcreteStrategyBuilder (Specific Builders) ***
Implements these methods for specific types of strategies. For example, one builder might be for a conservative strategy, while another is for an aggressive strategy.

*** StrategyDirector (Director) ***
Provides a sequence of steps to create a specific type of trading strategy. It tells the builder how to set parameters for a basic strategy or an advanced one.

"""

# Product: The complex object to build
class TradingStrategy:
    def __init__(self):
        self.risk_level = None
        self.trading_frequency = None
        self.asset_allocation = None
    
    def __str__(self):
        return (f"TradingStrategy(risk_level={self.risk_level}, "
                f"trading_frequency={self.trading_frequency}, "
                f"asset_allocation={self.asset_allocation})")

# Builder: Interface for building parts of the product
class StrategyBuilder:
    def set_risk_level(self, risk_level: str) -> None:
        raise NotImplementedError
    
    def set_trading_frequency(self, frequency: str) -> None:
        raise NotImplementedError
    
    def set_asset_allocation(self, allocation: dict) -> None:
        raise NotImplementedError
    
    def get_result(self) -> TradingStrategy:
        raise NotImplementedError

# ConcreteBuilder: Implements the actual construction logic
class ConcreteStrategyBuilder(StrategyBuilder):
    def __init__(self):
        self.reset()
    
    def reset(self) -> None:
        self._strategy = TradingStrategy()
    
    def set_risk_level(self, risk_level: str) -> None:
        self._strategy.risk_level = risk_level
    
    def set_trading_frequency(self, frequency: str) -> None:
        self._strategy.trading_frequency = frequency
    
    def set_asset_allocation(self, allocation: dict) -> None:
        self._strategy.asset_allocation = allocation
    
    def get_result(self) -> TradingStrategy:
        strategy = self._strategy
        self.reset()
        return strategy

# Director: Defines the construction process
class StrategyDirector:
    def __init__(self, builder: StrategyBuilder):
        self._builder = builder
    
    def construct_basic_strategy(self) -> TradingStrategy:
        self._builder.set_risk_level("Low")
        self._builder.set_trading_frequency("Daily")
        self._builder.set_asset_allocation({"Stocks": 0.6, "Bonds": 0.4})
        return self._builder.get_result()
    
    def construct_advanced_strategy(self) -> TradingStrategy:
        self._builder.set_risk_level("High")
        self._builder.set_trading_frequency("Hourly")
        self._builder.set_asset_allocation({"Stocks": 0.8, "Bonds": 0.2, "Commodities": 0.2})
        return self._builder.get_result()

# Client Code: Uses the director and builder to create strategies
builder = ConcreteStrategyBuilder()
director = StrategyDirector(builder)

basic_strategy = director.construct_basic_strategy()
print(f"Basic Strategy: {basic_strategy}")

advanced_strategy = director.construct_advanced_strategy()
print(f"Advanced Strategy: {advanced_strategy}")


"""
*** Product: The end result (like a complex sandwich or trading strategy).
*** Builder: Defines how to build the product step by step.
*** ConcreteBuilder: Implements the actual construction details for different products.
*** Director: Manages the building process, ensuring that the builder follows the correct steps.

The Builder Pattern helps to break down complex object creation into manageable steps, allowing for flexible and customizable construction processes.

"""
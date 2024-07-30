"""
The Bridge Pattern is a structural design pattern that decouples an abstraction from its implementation, allowing the two to vary independently.
This pattern is especially useful when both the abstraction and its implementation need to be extended through inheritance.

*** Bridge Pattern Explained Intuitively ***
Imagine Separating the Remote and TV

1. Abstraction and Implementation

Abstraction: Think of a remote control that can turn a device on or off.
Implementation: The device itself (e.g., TV, radio) that performs the actual operations when receiving commands from the remote.

2.Decoupling:

By separating the remote (abstraction) from the device (implementation), you can easily change or extend the functionality of either independently.
For example, you can use the same remote to control different types of devices, or you can change the internal workings of a device without changing how the remote interacts with it.

*** Structure ***
Abstraction: Defines the interface for the abstraction's control.
Refined Abstraction: Extends the abstraction to include more refined or specific operations.
Implementor: Defines the interface for the implementation.
Concrete Implementor: Implements the Implementor interface and defines the actual operations.

*** Example: Financial Trading Systems ***

Let’s use the Bridge Pattern in the context of financial trading systems, where we might want to decouple the way trades are executed from the types of trades.

"""

#==================== Abstraction ====================

# Define an interface for the abstraction

class Trade:
    def __init__(self, implementor):
        self._implementor = implementor

    def execute(self):
        raise NotImplementedError


#==================== Refined Abstraction ====================

# Extend the abstraction to include more specific types of trades:

class BuyTrade(Trade):
    def execute(self):
        self._implementor.execute_trade("buy")

class SellTrade(Trade):
    def execute(self):
        self._implementor.execute_trade("sell")

#==================== Implementor ====================

# Define the interface for the implementation

class TradeImplementor:
    def execute_trade(self, trade_type: str):
        raise NotImplementedError

#==================== Concrete Implementor ====================

# Implement the interface with specific details

class StockTradeImplementor(TradeImplementor):
    def execute_trade(self, trade_type: str):
        print(f"Executing {trade_type} trade for stocks")

class BondTradeImplementor(TradeImplementor):
    def execute_trade(self, trade_type: str):
        print(f"Executing {trade_type} trade for bonds")

#==================== Client Code ====================

# Use the abstraction and implementor to execute trades

# Client Code
if __name__ == "__main__":
    # Create implementors
    stock_trade_implementor = StockTradeImplementor()
    bond_trade_implementor = BondTradeImplementor()

    # Create trades with different implementors
    buy_stock_trade = BuyTrade(stock_trade_implementor)
    sell_stock_trade = SellTrade(stock_trade_implementor)
    buy_bond_trade = BuyTrade(bond_trade_implementor)
    sell_bond_trade = SellTrade(bond_trade_implementor)

    # Execute trades
    buy_stock_trade.execute()
    sell_stock_trade.execute()
    buy_bond_trade.execute()
    sell_bond_trade.execute()

#======================= How It Works =======================

"""
*** Abstraction ***
Trade is the abstraction that maintains a reference to the Implementor and delegates the execute method to the implementor.

*** Refined Abstraction ***
BuyTrade and SellTrade are refined abstractions that specify the type of trade and call the appropriate method on the implementor.

*** Implementor ***
TradeImplementor is the interface for the implementation that defines the execute_trade method.

*** Concrete Implementor ***
StockTradeImplementor and BondTradeImplementor are concrete implementors that provide the actual implementation of the execute_trade method.

"""
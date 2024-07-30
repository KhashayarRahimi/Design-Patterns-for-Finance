"""
The Adapter Pattern is a structural design pattern that allows objects with incompatible interfaces to work together.
It acts as a bridge between two incompatible interfaces, enabling them to interact seamlessly.

*** Adapter Pattern Explained Intuitively ***

Imagine Adapting Different Power Plugs

1. Different Standards
Incompatible Interfaces: Think of different power plugs and sockets used in different countries.
Each country has its own standard for power plugs and sockets, making it impossible to use a plug from one country in a socket from another directly.

2. Adapter
Bridge: An adapter acts as a bridge, allowing you to plug a device with a foreign power plug into a local socket. It converts the plug from one standard to another.

*** Structure ***
Target Interface: The interface that the client expects.
Adaptee: The existing class with an incompatible interface.
Adapter: A class that implements the Target interface and wraps the Adaptee, translating requests from the Target interface to the Adaptee.

Example: Financial Trading Systems
Let’s use the Adapter Pattern in the context of financial trading systems, where we might need to integrate a new third-party trading API with our existing system.
"""

#======================= Target Interface =======================

#Define the interface that our system expects
class TradingSystem:
    def execute_trade(self, symbol: str, quantity: int, trade_type: str):
        raise NotImplementedError


#======================= Adaptee =======================

#The new third-party trading API with an incompatible interface

class ThirdPartyTradingAPI:
    def place_order(self, instrument: str, amount: int, order_type: str):
        print(f"Placing order for {amount} of {instrument} as {order_type}")


#======================= Adapter =======================

#The adapter class that makes the Adaptee compatible with the Target interface:

class TradingAdapter(TradingSystem):
    def __init__(self, third_party_api: ThirdPartyTradingAPI):
        self.third_party_api = third_party_api

    def execute_trade(self, symbol: str, quantity: int, trade_type: str):
        # Adapt the method call to the third-party API's method
        self.third_party_api.place_order(symbol, quantity, trade_type)

#======================= Client Code =======================

#Use the adapter to interact with the third-party API through the Target interface

# Client Code
if __name__ == "__main__":
    third_party_api = ThirdPartyTradingAPI()
    adapter = TradingAdapter(third_party_api)

    # Use the adapter to execute a trade
    adapter.execute_trade("AAPL", 100, "buy")

#======================= How It Works =======================

"""

*** Target Interface ***
TradingSystem defines the interface our system expects, with the execute_trade method.

*** Adaptee ***
ThirdPartyTradingAPI is the existing class with an incompatible interface, using place_order instead of execute_trade.

*** Adapter ***
TradingAdapter implements the TradingSystem interface and wraps the ThirdPartyTradingAPI. It translates the execute_trade calls to place_order calls on the third-party API.

"""

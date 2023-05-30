from src.binarysearchtree.Obbst import ObBST
from src.models.order import Order
from constants import BID, ASK

class Orderbook:

    def __init__(self):
        self.bids = ObBST()
        self.asks = ObBST()

    def size(self):
        return len(self.bids) + len(self.asks)

    # Adds an order to the order book
    def add(self, order):
        # Before order is placed, run matching algorithm
        if order.side == BID:
            self.bids.update(order)
        elif order.side == ASK:
            self.asks.update(order)
        else:
            raise Exception("Order does not have a valid side")

    # Returns the orders at the best bid
    def bestBid(self):
        try:
            return self.bids.getMinNode().orders
        except:
            return []

    # Returns the orders at the best ask
    def bestAsk(self):
        try:
            return self.asks.getMaxNode().orders
        except:
            return []

    # Returns all orders at a level, bids and asks
    def priceLevel(self, price):
        bids = self.bids.getOrdersAtPrice(price)
        asks = self.asks.getOrdersAtPrice(price)
        return bids + asks
    

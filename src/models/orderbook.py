from src.binarysearchtree.Obbst import ObBST
from src.models.order import Order
from constants import BID, ASK

class Orderbook:

    def __init__(self):
        self.bids = ObBST()
        self.asks = ObBST()

    # Adds an order to the order book
    def add(self, order):
        # Before order is placed, run matching algorithm
        if order.side == BID:
            self.bids.update(order)
        elif order.side == ASK:
            self.asks.update(order)
        else:
            raise Exception("Order does not have a valid side")
    

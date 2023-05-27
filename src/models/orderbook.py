from src.binarysearchtree.Obbst import ObBST
from src.models.order import Order
from constants import BID, ASK

class Orderbook:

    def __init__(self):
        self.bids = ObBST()
        self.asks = ObBST()

    # Adds an order to the order book
    def add(self, order):
        if order.side == BID:
            pass
        elif order.side == ASK:
            pass
        else:
            raise Exception("Order has not valid side")
    

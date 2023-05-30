from src.binarysearchtree.Obbst import ObBST
from src.models.order import Order
from constants import BID, ASK

class Orderbook:

    def __init__(self):
        self.bids = ObBST(BID)
        self.asks = ObBST(ASK)

    def size(self):
        return len(self.bids) + len(self.asks)

    # Adds an order to the order book
    def add(self, order):
        # Before order is placed, run matching algorithm
        if self.instantMatch(order):
            if order.side == BID:
                pass
            elif order.side == ASK:
                pass
        else:
            if order.side == BID:
                self.bids.update(order)
            elif order.side == ASK:
                self.asks.update(order)
            else:
                raise Exception("Order does not have a valid side")

    def bestBid(self):
        try:
            return self.bids.getMinNode().val
        except:
            return 0
    
    def bestAsk(self):
        try:
            return self.asks.getMaxNode().val
        except:
            return 0

    # Returns all orders at a level, bids and asks
    def priceLevel(self, price):
        bids = self.bids.getOrdersAtPrice(price)
        asks = self.asks.getOrdersAtPrice(price)
        return bids + asks

    def getSpread(self):
        try:
            x = self.bids.getMinNode().val
            y = self.asks.getMaxNode().val
            return x - y
        except:
            raise Exception("One side of the orderbook is empty")

    # True or false if an order will be instantly matched
    def instantMatch(self, order):
        if len(self.bids) == 0 and order.side == ASK:
            return False
        if len(self.asks) == 0 and order.side == BID:
            return False
        elif order.side == ASK and order.price >= self.bestBid():
            return True
        elif order.side == BID and order.price <= self.bestAsk():
            return True
        else: return False
    

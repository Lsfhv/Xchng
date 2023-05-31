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
            self.match(order)
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
    
    def match(self, order):
        if order.side == BID:
            side = self.asks
        elif order.side == ASK:
            side = self.bids
        
        priceLevels = side.getPriceLevelsUpto(order.price)
        # print(len(priceLevels))
        while priceLevels and order.size != 0:
            if len(priceLevels[0].orders) == 0:
                print(f"Removed {priceLevels[0].val}")
                side.remove(priceLevels[0].val) 
            else:
                counterOrder = priceLevels[0].orders[0]
                # print(counterOrder.size)
                amountToTrade = min(order.size, counterOrder.size)
                # print(amountToTrade)
                order.size -= amountToTrade 
                counterOrder.size -= amountToTrade

                if counterOrder.size == 0:
                    priceLevels[0].orders.pop(0)
            # if len(priceLevels[0].orders) == 0:
            #     side.remove(pricelLevels[0].val) 
            priceLevels = side.getPriceLevelsUpto(order.price)

        if len(priceLevels[0].orders) == 0:
            print(f"Removed {priceLevels[0].val}")
            side.remove(priceLevels[0].val)

        if order.size != 0:
            self.add(order)
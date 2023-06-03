from src.binarysearchtree.Obbst import ObBST
from src.models.order import Order
from constants import BID, ASK

class Orderbook:
    
    def __init__(self):
        self.bids = ObBST(BID)
        self.asks = ObBST(ASK)

    # Takes an order, matches it if it can, then adds it to the orderbook
    def match(self, order):
        # print(order)
        def add(order):
            if order.side == ASK:
                self.asks.update(order)
            else:
                self.bids.update(order)

        if (order.side == ASK and self.bids.empty()) or (order.side == BID and self.asks.empty()): 
            add(order)
            return 

        # The opposite side to the order. Where we would attempt to match on
        if order.side == BID:
            side = self.asks
        elif order.side == ASK:
            side = self.bids
        
        priceLevels = side.getPriceLevelsUpto(order.price)

        while priceLevels and order.size != 0:
            counterOrder = priceLevels[0].orders[0]
            amountToTrade = min(counterOrder.size, order.size)
            order.size -= amountToTrade
            counterOrder.size -= amountToTrade
            if counterOrder.size == 0:
                priceLevels[0].orders.pop(0)
            if len(priceLevels[0].orders) == 0:
                side.remove(priceLevels[0].val)
            priceLevels = side.getPriceLevelsUpto(order.price)
            
        if order.size != 0:
            add(order)

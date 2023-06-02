from constants import BID, ASK

class Order:
    def __init__(self, price, size, side, userId = None):
        self.price = price
        self.size = size 
        if side != BID and side != ASK:
            raise TypeError("side must be a BID or an ASK")
        self.side = side
        self.userId = userId


    def __str__(self):
        return f"[price: {self.price}, size: {self.size}, userId: {self.userId}, side: {self.side}]"

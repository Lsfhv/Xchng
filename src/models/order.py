from constants import BID, ASK

class Order:
    def __init__(self, price, size, side, userId = None):
        self.price = price
        self.size = size 
        if side != BID and side != ASK:
            raise TypeError("side must be a BID or an ASK")
        self.side = side
        self.userId = userId

    def toDict(self):
        return {"price":self.price, "size":self.size, "side":self.side,"userId":self.userId} 

    def __str__(self):
        return self.json()

    # Returns in json
    def json(self):
        return {"price":self.price, "size":self.size, "side":self.side,"userId":self.userId}
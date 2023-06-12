from constants import BID, ASK

class Order:
    def __init__(self, price, size, side, userId = None):
        print(type(price))
        if type(price) != type(0.0) and type(price) != type(0):
            raise TypeError("Price must be a float or integer")
        if type(size) != type(0.0) and type(size) != type(0):
            raise TypeError("Size must be a float or integer")
        if side != BID and side != ASK:
            raise TypeError("side must be a BID or an ASK")
            
        self.side = side
        self.userId = userId
        self.price = price
        self.size = size 

    def toDict(self):
        return {"price":self.price, "size":self.size, "side":self.side,"userId":self.userId} 

    def __str__(self):
        return self.json()

    # Returns in json
    def json(self):
        return {"price":self.price, "size":self.size, "side":self.side,"userId":self.userId}
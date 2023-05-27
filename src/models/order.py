class Order:
    def __init__(self, price, size, userId = None, side = None):
        self.price = price
        self.size = size 
        self.userId = userId
        self.side = side

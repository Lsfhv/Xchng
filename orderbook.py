from order import Order
from bst import BST
from bst import Node
# from test import response_json

from orderbookStream.wssorderbookbinance import wssRun
from threading import Thread 
from orderbookStream.orderbooksnapshot import getSnapshot

class Orderbook:
    
    def __init__(self):
        self.bids = BST()
        self.asks = BST()
        self.orderPool = []
        self.start()
    

    # fills order book
    def start(self):
        t1 = Thread(target=wssRun, args = (self.orderPool,))
        t1.start()

        t2 = Thread(target = self.add)
        t2.start()

        x = getSnapshot()

        for bid in x['bids']:
            self.bids.insert(Node(Order(bid[0], bid[1])))
        for ask in x['asks']:
            self.asks.insert(Node(Order(ask[0], ask[1])))
        t1.join()
        # t2.join()

    def add(self):
        while True:
            while self.orderPool:
                print(f"OrderPool size: {len(self.orderPool)}")
                first = self.orderPool[0]
                self.orderPool.pop(0)
                bids = first['b']
                asks = first['a']

                for bid in bids:
                    self.bids.insert(Node(Order(bid[0], bid[1])))

                for ask in asks:
                    self.bids.insert(Node(Order(ask[0], ask[1])))
                print(f"OrderPool size: {len(self.bids)}")
            # print(len(self.bids))

    

Orderbook()
    

# need to be able to find the maximum,
# search for a specific price level
# removals
# insertions
    

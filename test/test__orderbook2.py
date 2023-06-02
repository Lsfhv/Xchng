from src.binarysearchtree.Obbst import ObBST
import unittest
from src.binarysearchtree.binarySearchTree import BinarySearchTree, Node
from src.models.order import Order

from src.models.orderbook import Orderbook

from constants import BID, ASK

class TestOrderbook(unittest.TestCase):

    def setUp(self):
        self.ob = Orderbook()
        self.order1 = Order(100, 2, "bob", ASK)
        self.order2 = Order(100, 10, "alice", ASK)
        # self.order3 = Order(101, 10, "", BID)

        self.ob.add(self.order1)
        self.ob.add(self.order2)
        # self.ob.add(self.order3)

        self.filledOrderbook = Orderbook()

        for i in range(100, 120):
            self.filledOrderbook.add(Order(i, 10, "", BID))

        for i in range(60, 91):
            self.filledOrderbook.add(Order(i, 10, "", ASK))

    def test_hi(self):
        pass


    # def test_orderbookBecomesEmptyAfterMatching(self):
    #     order = Order(100, 12, "", BID)
    #     self.ob.add(order)

    #     self.assertEqual(self.ob.bids.root, None)
    #     self.assertEqual(self.ob.asks.root, None)
        
    #     self.assertRaises(Exception, self.ob.getSpread)

    # def test_matchingOnFilledOrderbook(self):
    #     order = Order(80, 100, "", BID)
    #     self.filledOrderbook.add(order)
    #     self.assertEqual(self.filledOrderbook.bestAsk(), 80)

        
    def test_orderGetsPlacesAfterMatching(self):
        order = Order(80, 111, "", BID)
        self.filledOrderbook.add(order)
        
        self.assertEqual(self.filledOrderbook.bestBid(), 80)

        print(self.filledOrderbook.bestBid())

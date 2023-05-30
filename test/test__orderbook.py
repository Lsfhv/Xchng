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

        self.ob.add(self.order1)
        self.ob.add(self.order2)

    def test_orderbookhascorrectlength(self):
        self.assertEqual(self.ob.size(), 1)

    def test_priceLevelHoldsCorrectAmountOfOrders(self):
        lst = self.ob.priceLevel(100)
        self.assertEqual(len(lst), 2)
    
    def test_priceLevelOrdersAreOrderedCorrectly(self):
        lst = self.ob.priceLevel(100)

        self.assertEqual(lst[0], self.order1)
        self.assertEqual(lst[1], self.order2) 

    def test_bestAsk(self):
        lst = self.ob.bestAsk()
        self.assertEqual(lst, [self.order1, self.order2])  

    def test_bestBid(self):
        lst = self.ob.bestBid()
        self.assertEqual(lst, [])     

        order = Order(20, 0, "bob", BID)
        self.ob.add(order)
        lst = self.ob.bestBid()
        self.assertEqual(lst, [order])
    
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
        self.order3 = Order(101, 10, "alice", BID)

        self.ob.add(self.order1)
        self.ob.add(self.order2)
        self.ob.add(self.order3)

        self.emptyOB = Orderbook()

    def test_orderbookhascorrectlength(self):
        self.assertEqual(self.ob.size(), 2)

    def test_priceLevelHoldsCorrectAmountOfOrders(self):
        lst = self.ob.priceLevel(100)
        self.assertEqual(len(lst), 2)
    
    def test_priceLevelOrdersAreOrderedCorrectly(self):
        lst = self.ob.priceLevel(100)
        self.assertEqual(lst[0], self.order1)
        self.assertEqual(lst[1], self.order2) 

    def test_spread(self):
        self.assertEqual(self.ob.getSpread(), 1)
        self.ob.add(Order(100.1, 10, "alice", BID))
        self.assertEqual(round(self.ob.getSpread(), 2), 0.1)

    def test_spreadEmpty(self):
        self.assertRaises(Exception, self.emptyOB.getSpread)

    def test_instantMatch(self):
        self.ob.add(Order(101,1, "bob", BID))

        self.assertEqual(self.ob.instantMatch(Order(101,0,"",ASK)), True)
        self.assertEqual(self.ob.instantMatch(Order(101,0,"",BID)), False)
        self.assertEqual(self.ob.instantMatch(Order(100,0,"",BID)), True)

        self.assertEqual(self.emptyOB.instantMatch(Order(101, 0, "", ASK)), False)
        self.assertEqual(self.emptyOB.instantMatch(Order(101, 0, "", BID)), False)


    def test_match(self):
        order4 = Order(100, 12, None, BID)
        self.ob.add(order4)
        # print(self.ob.asks.root.val)
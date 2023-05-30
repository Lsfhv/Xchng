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

        self.order3 = Order(101, 10, "", BID)

        self.ob.add(self.order1)
        self.ob.add(self.order2)
        self.ob.add(self.order3)

    def test_hi(self):
        pass
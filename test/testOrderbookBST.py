import unittest
from src.binarysearchtree.binarySearchTree import BinarySearchTree, Node
from src.models.order import Order
from constants import ASK, BID
from src.binarysearchtree.Obbst import ObBST

class TestOrderbookBST(unittest.TestCase):
    def setUp(self):
        self.bstASK = ObBST(ASK)
        self.bstBID = ObBST(BID)

        self.bids = []
        self.asks = []

        for i in range(0, 20 + 1):
            self.bids.append(Order(i + 50, 10, BID))
            self.asks.append(Order(i + 50, 10, ASK))
        
    def testGetPriceLevelsBetween(self):
        pass

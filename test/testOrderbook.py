import unittest
from src.binarysearchtree.binarySearchTree import BinarySearchTree, Node
from src.models.order import Order
from constants import ASK, BID
from src.binarysearchtree.Obbst import ObBST
from src.models.orderbook import Orderbook

class TestOrderbook(unittest.TestCase):
    def setUp(self):
        self.orderbook = Orderbook()

        self.bids = []
        self.asks = []

        for i in range(0, 20  + 1):
            self.asks.append(Order(i + 50, 10, ASK)) # [50,70]
            self.bids.append(Order(i + 20, 10, BID)) # [20, 40]

        for i in self.bids:
            self.orderbook.match(i)
        for i in self.asks:
            self.orderbook.match(i)

    def testOrderbookIsInitalisedCorrectlyAndMakeATradeThenMakesItsCounterTrade(self):
        self.assertEqual(self.orderbook.bids.getBestPrice(), 40)   
        self.assertEqual(self.orderbook.asks.getBestPrice(), 50) 

        self.orderbook.match(Order(41,10,ASK))

        self.assertEqual(self.orderbook.bids.getBestPrice(), 40)   
        self.assertEqual(self.orderbook.asks.getBestPrice(), 41) 

        self.orderbook.match(Order(41, 10, BID))

        self.assertEqual(self.orderbook.bids.getBestPrice(), 40)   
        self.assertEqual(self.orderbook.asks.getBestPrice(), 50) 

    def testOrderbookIsClearedCorrectly(self):
        self.orderbook.match(Order(40, 10, ASK))
        self.assertEqual(self.orderbook.bids.getBestPrice(), 39)   
        self.assertEqual(self.orderbook.asks.getBestPrice(), 50)

        self.orderbook.match(Order(39, 5, ASK)) 
        self.assertEqual(self.orderbook.bids.getBestPrice(), 39)   
        self.assertEqual(self.orderbook.bids.getMaxNode().orders[0].size, 5)
        self.assertEqual(self.orderbook.asks.getBestPrice(), 50)

        self.orderbook.match(Order(39, 1, ASK)) 
        self.assertEqual(self.orderbook.bids.getBestPrice(), 39)   
        self.assertEqual(self.orderbook.bids.getMaxNode().orders[0].size, 4)
        self.assertEqual(self.orderbook.asks.getBestPrice(), 50)

        self.orderbook.match(Order(39, 4, ASK)) 
        self.assertEqual(self.orderbook.bids.getBestPrice(), 38)   
        self.assertEqual(self.orderbook.bids.getMaxNode().orders[0].size, 10)
        self.assertEqual(self.orderbook.asks.getBestPrice(), 50)

        self.orderbook.match(Order(30, 91, ASK)) 
        self.assertEqual(self.orderbook.bids.getBestPrice(), 29)   
        self.assertEqual(self.orderbook.bids.getMaxNode().orders[0].size, 10)
        self.assertEqual(self.orderbook.asks.getBestPrice(), 30)   
        self.assertEqual(self.orderbook.asks.getMinNode().orders[0].size, 1)

        self.orderbook.match(Order(20, 100, ASK))
        self.assertRaises(Exception, self.orderbook.bids.getBestPrice)  
        self.assertEqual(self.orderbook.asks.getBestPrice(), 30)   
        self.assertTrue(self.orderbook.bids.empty())
        # print(self.orderbook.bids.len)
        # self.assertTrue(len(self.orderbook.bids) == 0)
        # No bids remaining

        self.orderbook.match(Order(1000, 1, BID))
        self.assertRaises(Exception, self.orderbook.bids.getBestPrice)  
        self.assertEqual(self.orderbook.asks.getBestPrice(), 50)  

        self.orderbook.match(Order(70, 200, BID))
        self.assertRaises(Exception, self.orderbook.bids.getBestPrice)  
        self.assertEqual(self.orderbook.asks.getBestPrice(), 70)  

        self.orderbook.match(Order(70, 10, BID))
        self.assertRaises(Exception, self.orderbook.bids.getBestPrice)  
        self.assertRaises(Exception, self.orderbook.asks.getBestPrice)  

        
        self.assertTrue(self.orderbook.bids.empty())
        self.assertTrue(self.orderbook.asks.empty())





    





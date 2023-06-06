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
            self.bids.append(Order(i + 50, 10, BID)) # [50,70]
            self.asks.append(Order(i + 20, 10, ASK)) # [20,40]
        
        for i in self.bids:
            self.bstBID.update(i)
        for i in self.asks:
            self.bstASK.update(i)
            
    def testBestPrice(self):
        self.assertEqual(self.bstBID.getBestPrice(), 70)
        self.assertEqual(self.bstASK.getBestPrice(), 20)

        self.bstBID.update(Order(71, 10, BID))
        self.assertEqual(self.bstBID.getBestPrice(), 71)

        self.assertRaises(Exception, ObBST(ASK).getBestPrice)
        self.assertRaises(Exception, ObBST(BID).getBestPrice)
        
    def testGetPriceLevelsBetweenBid(self):
        bids = self.bstBID.getPriceLevelsBetween(70, 60)
        self.assertEqual(bids[0].val, 70)
        self.assertEqual(bids[-1].val, 60)
        for i in range(0, len(bids) - 1):
            self.assertTrue(bids[i] > bids[i + 1])
        
        bids = self.bstBID.getPriceLevelsBetween(70, 70)
        self.assertEqual(len(bids), 1)
        self.assertEqual(bids[0].val, 70)

        bids = self.bstBID.getPriceLevelsBetween(70, 71)
        self.assertEqual(len(bids), 0)

        bids = self.bstBID.getPriceLevelsBetween(60, 70)
        self.assertEqual(len(bids), 0)

        bids = self.bstBID.getPriceLevelsBetween(65, 60)
        self.assertEqual(bids[0].val, 65)
        self.assertEqual(bids[-1].val, 60)
        for i in range(0, len(bids) - 1):
            self.assertTrue(bids[i] > bids[i + 1])
    
    def testGetPriceLevelsBetweenAsk(self):
        asks = self.bstASK.getPriceLevelsBetween(20, 30)
        self.assertEqual(asks[0].val, 20)
        self.assertEqual(asks[-1].val, 30)
        for i in range(0, len(asks) - 1):
            self.assertTrue(asks[i] < asks[i+1])
            self.assertTrue(asks[i].val + 1 == asks[i + 1].val)

        asks = self.bstASK.getPriceLevelsBetween(20, 20)
        self.assertEqual(asks[0].val, 20)
        self.assertEqual(len(asks), 1)

        asks = self.bstASK.getPriceLevelsBetween(20, 19)
        self.assertEqual(len(asks), 0)

        asks = self.bstASK.getPriceLevelsBetween(25, 30)
        self.assertEqual(asks[0].val, 25)
        self.assertEqual(asks[-1].val, 30)
        for i in range(0, len(asks) - 1):
            self.assertTrue(asks[i] < asks[i+1])
            self.assertTrue(asks[i].val + 1 == asks[i + 1].val)

    def testGetPriceLevelsUptoBid(self):
        bids = self.bstBID.getPriceLevelsUpto(60)
        self.assertEqual(bids[0].val, 70)
        self.assertEqual(bids[-1].val, 60)
        for i in range(0, len(bids) - 1):
            self.assertTrue(bids[i] > bids[i + 1])

        bids = self.bstBID.getPriceLevelsUpto(50)
        self.assertEqual(bids[0].val, 70)
        self.assertEqual(bids[-1].val, 50)
        for i in range(0, len(bids) - 1):
            self.assertTrue(bids[i] > bids[i + 1])

        bids = self.bstBID.getPriceLevelsUpto(49)
        self.assertEqual(bids[0].val, 70)
        self.assertEqual(bids[-1].val, 50)
        for i in range(0, len(bids) - 1):
            self.assertTrue(bids[i] > bids[i + 1])

        bids = self.bstBID.getPriceLevelsUpto(-100)
        self.assertEqual(bids[0].val, 70)
        self.assertEqual(bids[-1].val, 50)
        for i in range(0, len(bids) - 1):
            self.assertTrue(bids[i] > bids[i + 1])

        self.bstBID.update(Order(100, 10, BID))
        self.assertEqual(self.bstBID.getBestPrice(), 100)
        bids = self.bstBID.getPriceLevelsUpto(60)
        self.assertEqual(bids[0].val, 100)
        self.assertEqual(bids[-1].val, 60)

    def testGetPriceLevelsUptoAsk(self):
        asks = self.bstASK.getPriceLevelsUpto(30)
        self.assertEqual(asks[0].val, 20)
        self.assertEqual(asks[-1].val, 30)
        for i in range(0, len(asks) - 1):
            self.assertTrue(asks[i] < asks[i + 1])

        asks = self.bstASK.getPriceLevelsUpto(40)
        self.assertEqual(asks[0].val, 20)
        self.assertEqual(asks[-1].val, 40)
        for i in range(0, len(asks) - 1):
            self.assertTrue(asks[i] < asks[i + 1])

        asks = self.bstASK.getPriceLevelsUpto(41)
        self.assertEqual(asks[0].val, 20)
        self.assertEqual(asks[-1].val, 40)
        for i in range(0, len(asks) - 1):
            self.assertTrue(asks[i] < asks[i + 1])

        asks = self.bstASK.getPriceLevelsUpto(19)
        self.assertTrue(len(asks) == 0)

        # add an order and check method works correctly

        self.bstASK.update(Order(1, 10, ASK))
        self.assertTrue(self.bstASK.getBestPrice(), 1)
        asks = self.bstASK.getPriceLevelsUpto(30)
        self.assertEqual(asks[0].val, 1)
        self.assertEqual(asks[-1].val, 30)
        for i in range(0, len(asks) - 1):
            self.assertTrue(asks[i] < asks[i + 1])
        
    def testBSTRejectsOrderWithWrongSide(self):
        self.assertRaises(TypeError, self.bstASK.update, args = [Order(10,10,BID)])
        self.assertRaises(TypeError, self.bstBID.update, args = [Order(10,10,ASK)])

    def testGetAllOrders(self):
        orders = self.bstBID.getAllOrders()
        self.assertEqual(orders[0].price, 70)
        self.assertEqual(orders[-1].price, 50)
        for i in range(0, len(orders) - 1) :
            self.assertTrue(orders[i].price > orders[i + 1].price)

        orders = self.bstASK.getAllOrders()
        self.assertEqual(orders[0].price, 20)
        self.assertEqual(orders[-1].price, 40)
        for i in range(0, len(orders) - 1) :
            self.assertTrue(orders[i].price < orders[i + 1].price)

        self.bstBID.update(Order(70, 100, BID))
        orders = self.bstBID.getAllOrders()
        
        self.assertEqual(orders[1].price, 70)
        self.assertEqual(orders[1].size, 100)

        # Empty books
        self.assertEqual(ObBST(side = BID).getAllOrders(), [])
        self.assertEqual(ObBST(side = ASK).getAllOrders(), [])


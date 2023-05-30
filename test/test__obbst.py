from src.binarysearchtree.Obbst import ObBST
import unittest
from src.binarysearchtree.binarySearchTree import BinarySearchTree, Node
from src.models.order import Order

from constants import BID, ASK

class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.ob = ObBST()

        self.ob.insert(Node(Order(100, 0)))

        self.ob.insert(Node(Order(75, 0)))
        self.ob.insert(Node(Order(125, 0)))

        self.ob.insert(Node(Order(65, 0)))
        self.ob.insert(Node(Order(85, 0)))
        self.ob.insert(Node(Order(115, 0)))
        self.ob.insert(Node(Order(150, 0)))

        self.ob.insert(Node(Order(60, 0)))
        self.ob.insert(Node(Order(70, 0)))
        self.ob.insert(Node(Order(95, 0)))
        self.ob.insert(Node(Order(135, 0)))
        self.ob.insert(Node(Order(175, 10)))


        self.orderbookASK = ObBST(ASK)
        for i in range(50,100):
            self.orderbookASK.update(Order(i, 10))
        self.orderbookBID = ObBST(BID)
        for i in range(50,100):
            self.orderbookBID.update(Order(i,10))

    def test_obUpdatePriceLevelAlreadyExists(self):
        order = Order(100, 1000)
        self.ob.update(order)
        priceLevel = self.ob.find(100).orders
        self.assertEqual(len(priceLevel), 2)
        self.assertEqual(priceLevel[1], order)


    def test_obUpdatePriceLeveLDoesNotExist(self):
        order = Order(101, 10, userId = "HI", side = "BID")
        self.ob.update(order)
        priceLevel = self.ob.find(101)
        self.assertEqual(priceLevel.val, 101)
        
    def test_updatingIntoAnEmptyOrderBook(self):
        ob = ObBST()
        ob.update(Order(1,1))
        self.assertEqual(len(ob), 1)
        self.assertEqual(ob.root.val, 1)
        self.assertTrue(ob.root.left == None)
        self.assertTrue(ob.root.right == None)
        
    def test_getOrdersBetweenInterval(self):
        ob = ObBST()
        order1 = Order(100, 0)
        order2 = Order(90, 0)
        order3 = Order(101, 0)
        order4 = Order(20, 0)
        ob.update(order1)
        ob.update(order2)
        ob.update(order3)
        ob.update(order4)

        self.assertEqual(ob.getOrdersBetweenInterval(100, 90), ob.getOrdersBetweenInterval(90, 100))
        
        self.assertEqual(ob.getOrdersBetweenInterval(100, 100), [order1])
        self.assertEqual(ob.getOrdersBetweenInterval(102, 102), [])

    def test_getOrdersUptoPrice(self):
        pass
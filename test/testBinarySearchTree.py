import unittest
from src.binarysearchtree.binarySearchTree import BinarySearchTree, Node
from src.models.order import Order
from constants import ASK, BID
class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

        self.bst.insert(Node(Order(100, 0, ASK)))

        self.bst.insert(Node(Order(75, 0, ASK)))
        self.bst.insert(Node(Order(125, 0, ASK)))

        self.bst.insert(Node(Order(65, 0, ASK)))
        self.bst.insert(Node(Order(85, 0, ASK)))
        self.bst.insert(Node(Order(115, 0, ASK)))
        self.bst.insert(Node(Order(150, 0, ASK)))

        self.bst.insert(Node(Order(60, 0, ASK)))
        self.bst.insert(Node(Order(70, 0, ASK)))
        self.bst.insert(Node(Order(95, 0, ASK)))
        self.bst.insert(Node(Order(135, 0, ASK)))
        self.bst.insert(Node(Order(175, 10, ASK)))
        self.inorder = [60, 65, 70, 75, 85, 95, 100, 115, 125, 135, 150, 175]
        self.inorderReverse = [175, 150, 135, 125, 115, 100, 95, 85, 75, 70, 65, 60]
        self.lst = [100, 75, 125, 65, 85, 115, 150, 60,70,95,135,175]
        self.length = 12

    def testRemovingAllNodesFromBST(self):
        self.assertEqual(len(self.bst), self.length)
        for i in self.lst:
            self.bst.remove(i)
            self.length -= 1
            self.assertEqual(len(self.bst), self.length)
        self.assertEqual(self.bst.root, None)
        self.assertEqual(self.bst.find(100), None)
        self.assertEqual(self.bst.inorderTraversal(), [])
        self.assertEqual(self.bst.inorderTraversal(reverse = True), [])
        self.assertRaises(Exception, self.bst.getMinNode)
        self.assertRaises(Exception, self.bst.getMaxNode)

    def testBSTInorder(self):
        self.assertEqual(self.bst.toList(), self.inorder)
        self.assertEqual(self.bst.toList(True), self.inorderReverse)

    def testBSTRemovals(self):
        self.assertEqual(self.bst.getMaxNode().val, 175)
        self.assertEqual(self.bst.getMinNode().val, 60)
        self.bst.remove(175)
        self.assertEqual(self.bst.getMaxNode().val, 150)
    
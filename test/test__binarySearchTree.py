import unittest
from src.binarysearchtree.binarySearchTree import BinarySearchTree
from src.models.order import Order

class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.bst = BinarySearchTree()
        self.bst.update(Order(1,10))
        self.bst.update(Order(0,10))
        self.bst.update(Order(2,10))

    def test_bstIsOrderedCorrectly(self):
        self.assertEqual(len(self.bst),3)
        self.assertEqual(self.bst.toList(), [0, 1, 2])

    def test_bstUpdate(self):
        self.bst.update(Order(1,20))
        self.bst.update(Order(-1,0))

        self.assertEqual(self.bst.root.pool[None], 30)
        self.assertEqual(len(self.bst), 4)
        self.assertEqual(self.bst.root.left.left.pool[None], 0)
        self.assertEqual(str(self.bst), "[-1, 0, 1, 2]")

    def test_bstLength(self):
        self.assertEqual(len(self.bst), 3)
        self.bst.update(Order(1,1))
        self.assertEqual(len(self.bst), 3)
        self.bst.update(Order(-1,10))
        self.assertEqual(len(self.bst), 4)

    
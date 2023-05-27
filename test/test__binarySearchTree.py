import unittest
from src.binarysearchtree.binarySearchTree import BinarySearchTree, Node
from src.models.order import Order

class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.bst = BinarySearchTree()

        self.bst.insert(Node(Order(100, 0)))

        self.bst.insert(Node(Order(75, 0)))
        self.bst.insert(Node(Order(125, 0)))

        self.bst.insert(Node(Order(65, 0)))
        self.bst.insert(Node(Order(85, 0)))
        self.bst.insert(Node(Order(115, 0)))
        self.bst.insert(Node(Order(150, 0)))

        self.bst.insert(Node(Order(60, 0)))
        self.bst.insert(Node(Order(70, 0)))
        self.bst.insert(Node(Order(95, 0)))
        self.bst.insert(Node(Order(135, 0)))
        self.bst.insert(Node(Order(175, 10)))

    def test_bstHasCorrectLength(self):
        self.assertEqual(len(self.bst), 12)

    def test_bstIsSorted(self):
        self.assertEqual(self.bst.toList(), [60, 65, 70, 75, 85, 95, 100, 115, 125, 135, 150, 175])

    def test_bstFindFindsTheCorrectNode(self):
        node = self.bst.find(175)
    
    def test_bstFindFindsTheClosestNodeForAKeyThatDoesntExist(self):
        node = self.bst.find(176)
        self.assertEqual(node.val, 175)

        node = self.bst.find(84)
        self.assertEqual(node.val, 85)

        node = self.bst.find(66)
        self.assertEqual(node.val, 70)

    # Checks some nodes that their pointers are set correctly
    def test_someBstPointers(self):
        self.assertEqual(self.bst.root.parent, None)

        node = self.bst.find(66)
        self.assertEqual(node.parent.val, 65)

    
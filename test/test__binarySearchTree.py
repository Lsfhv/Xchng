# import unittest
# from src.binarysearchtree.binarySearchTree import BinarySearchTree, Node
# from src.models.order import Order


# class TestBinarySearchTree(unittest.TestCase):

#     def setUp(self):
#         self.bst = BinarySearchTree()

#         self.bst.insert(Node(Order(100, 0)))

#         self.bst.insert(Node(Order(75, 0)))
#         self.bst.insert(Node(Order(125, 0)))

#         self.bst.insert(Node(Order(65, 0)))
#         self.bst.insert(Node(Order(85, 0)))
#         self.bst.insert(Node(Order(115, 0)))
#         self.bst.insert(Node(Order(150, 0)))

#         self.bst.insert(Node(Order(60, 0)))
#         self.bst.insert(Node(Order(70, 0)))
#         self.bst.insert(Node(Order(95, 0)))
#         self.bst.insert(Node(Order(135, 0)))
#         self.bst.insert(Node(Order(175, 10)))

#     def test_inorderOnEmptyBST(self):
#         bst = BinarySearchTree()
#         self.assertEqual(bst.inorderTraversal(), [])

#     def test_bstHasCorrectLength(self):
#         self.assertEqual(len(self.bst), 12)

#     def test_bstIsSortedReversed(self):
#         self.assertEqual(self.bst.toList(reverse = True), [175, 150, 135, 125, 115, 100, 95, 85, 75, 70, 65, 60])

#     def test_bstIsSorted(self):
#         self.assertEqual(self.bst.toList(), [60, 65, 70, 75, 85, 95, 100, 115, 125, 135, 150, 175])

#     def test_bstFindFindsTheCorrectNode(self):
#         node = self.bst.find(175)
    
#     def test_bstFindFindsTheClosestNodeForAKeyThatDoesntExist(self):
#         node = self.bst.find(176)
#         self.assertEqual(node.val, 175)

#         node = self.bst.find(84)
#         self.assertEqual(node.val, 85)

#         node = self.bst.find(66)
#         self.assertEqual(node.val, 70)

#     # Checks some nodes that their pointers are set correctly
#     def test_someBstPointers(self):
#         self.assertEqual(self.bst.root.parent, None)

#         node = self.bst.find(66)
#         self.assertEqual(node.parent.val, 65)

#     #       10
#     #       /
#     #      9
#     #     /\
#     #    8 9.1
#     def test_removeRootWithOnly1ChildOnTheLeft(self): 
#         bst = BinarySearchTree()
#         bst.insert(Node(Order(10,0)))
#         bst.insert(Node(Order(9,0)))
#         bst.insert(Node(Order(8,0)))
#         bst.insert(Node(Order(9.1,0)))
#         self.assertEqual(bst.toList(), [8,9,9.1,10])
#         bst.remove(10)
#         self.assertEqual(bst.toList(), [8,9,9.1])
#         self.assertTrue(bst.root.val == 9)
#         self.assertTrue(bst.root.left.val == 8)
#         self.assertTrue(bst.root.right.val == 9.1)
#         self.assertTrue(bst.root.left.parent == bst.root)
#         self.assertTrue(bst.root.right.parent == bst.root)
#         self.assertTrue(bst.root.parent == None)

#     #    #       10
#     #    #       /
#    #     #      9
#    #     #     /
#     #    #    8 
#     #        /\
#     #       7  8.1 
#     def test_removeNodeWithOnly1Child(self):
#         bst = BinarySearchTree()
#         bst.insert(Node(Order(10,0)))
#         bst.insert(Node(Order(9,0)))
#         bst.insert(Node(Order(8,0)))
#         bst.insert(Node(Order(7,0)))
#         bst.insert(Node(Order(8.1,0)))
#         self.assertEqual(bst.toList(), [7,8,8.1,9,10])
#         bst.remove(9)
#         self.assertEqual(bst.toList(), [7,8,8.1,10])

#         self.assertTrue(bst.root.left.val == 8)
#         self.assertTrue(bst.root.left.parent.val == 10)

#         self.assertTrue(bst.root.left.left.val == 7)
#         self.assertTrue(bst.root.left.right.val == 8.1)

#     #  10
#     #  /\
#     # 8 11
#     def test_removeRootWith2Children(self):
#         bst = BinarySearchTree()
#         bst.insert(Node(Order(10,0)))
#         bst.insert(Node(Order(11,0)))
#         bst.insert(Node(Order(8,0)))

#         bst.remove(10)

#         self.assertEqual(bst.toList(), [8,11])

#         self.assertEqual(bst.root.val, 11)
#         self.assertTrue(bst.root.left.parent == bst.root)

#         self.assertTrue(bst.root.right == None)
#         self.assertTrue(bst.root.parent == None)

#     def test_removeNodeWith2Children(self):
#         bst = BinarySearchTree()

#         bst.insert(Node(Order(100, 0)))
        
#         bst.insert(Node(Order(75, 0)))
#         bst.insert(Node(Order(125, 0)))

#         bst.insert(Node(Order(65, 0)))
#         bst.insert(Node(Order(85, 0)))
#         bst.insert(Node(Order(115, 0)))
#         bst.insert(Node(Order(150, 0)))

#         bst.insert(Node(Order(60, 0)))
#         bst.insert(Node(Order(70, 0)))
#         bst.insert(Node(Order(80, 0)))
#         bst.insert(Node(Order(95, 0)))
#         bst.insert(Node(Order(110, 0)))
#         bst.insert(Node(Order(120, 0)))
#         bst.insert(Node(Order(135, 0)))
#         bst.insert(Node(Order(175, 0)))

#         bst.remove(75)

#         self.assertTrue(bst.root.val == 100)
#         self.assertTrue(bst.root.left.val == 80)
#         self.assertTrue(bst.root.left.left.val == 65)
#         self.assertTrue(bst.root.left.right.val == 85)
#         self.assertTrue(bst.root.left.right.left == None)
#         self.assertTrue(bst.root.left.right.right.val == 95)

#     def test_removeNodeWith2ChildrenAgain(self):
#         bst = BinarySearchTree()

#         bst.insert(Node(Order(100, 0)))
        
#         bst.insert(Node(Order(75, 0)))
#         bst.insert(Node(Order(125, 0)))

#         bst.insert(Node(Order(65, 0)))
#         bst.insert(Node(Order(85, 0)))
#         bst.insert(Node(Order(115, 0)))
#         bst.insert(Node(Order(150, 0)))

#         bst.insert(Node(Order(60, 0)))
#         bst.insert(Node(Order(70, 0)))
#         bst.insert(Node(Order(80, 0)))
#         bst.insert(Node(Order(95, 0)))
#         bst.insert(Node(Order(110, 0)))
#         bst.insert(Node(Order(120, 0)))
#         bst.insert(Node(Order(135, 0)))
#         bst.insert(Node(Order(175, 0)))

#         bst.remove(100)

#         self.assertEqual(bst.toList(), [60, 65, 70, 75, 80, 85, 95, 110, 115, 120, 125, 135, 150, 175])
#         self.assertEqual(bst.root.val, 110)

#     def test_removeRoot(self):
#         bst = BinarySearchTree()
#         bst.insert(Node(Order(100,0)))
#         bst.remove(100)
#         self.assertEqual(bst.root, None)

#     def test_getMinNode(self):
#         minVal = self.bst.getMinNode().val
#         self.assertEqual(minVal, 60)

#     def test_getMaxNode(self):
#         maxVal = self.bst.getMaxNode().val
#         self.assertEqual(maxVal, 175)

#     def test_getMaxNodeEmptyBST(self):
#         bst = BinarySearchTree()
#         self.assertRaises(Exception, bst.getMaxNode)

#     def test_getMinNodeEmptyBST(self):
#         bst = BinarySearchTree()
#         self.assertRaises(Exception, bst.getMinNode)
    
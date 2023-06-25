from functools import reduce

class Node:
    def __init__(self, T):
        
        self.parent = None
        self.left = None
        self.right = None

        self.val = T.price # price level

        self.orders = [T]

    def __gt__(self, other):
        return self.val > other.val
    
    def __lt__(self, other):
        return self.val < other.val
    
    def totalSize(self): 
        return reduce(lambda x,y: x + y.size ,self.orders, 0)

# Ordering is not gauraunteed in the case the not all nodes have distinct vals.
class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.len = 0 

    def insert(self, node):
        if self.root == None:
            self.root = node
        else:
            target = self.find(node.val)
            node.parent = target
            if node.val <= target.val:
                target.left = node
            else:
                target.right = node
                
        self.len += 1

    def remove(self, key):
        nodeToRemove = self.find(key)
        if nodeToRemove.val != key:
            raise Exception("Element does not exist")
        
        parent = nodeToRemove.parent

        if nodeToRemove.left != None and nodeToRemove.right != None:
            # Node to remove has 2 children
            inorder = self.inorderTraversal()

            minOfRightSubTree = inorder[inorder.index(nodeToRemove) + 1]

            self.remove(minOfRightSubTree.val)

            leftChild = nodeToRemove.left
            rightChild = nodeToRemove.right

            if leftChild != None: leftChild.parent = minOfRightSubTree
            if rightChild != None: rightChild.parent = minOfRightSubTree

            if parent == None:
                self.root = minOfRightSubTree
            if parent != None and parent.right == nodeToRemove: 
                parent.right = minOfRightSubTree
            elif parent != None and parent.left == nodeToRemove:
                parent.left = minOfRightSubTree

            minOfRightSubTree.parent = parent
            minOfRightSubTree.left = leftChild
            minOfRightSubTree.right = rightChild
        elif nodeToRemove.left != None or nodeToRemove.right != None:
            # Node to remove has 1 child

            # The subtree of the node that will be removed
            if nodeToRemove.left != None:
                subTree = nodeToRemove.left
            else:
                subTree = nodeToRemove.right
            
            if parent == None: # Node removed was root
                self.root = subTree
                self.root.parent = None
            else:
                subTree.parent = parent
                if parent.left == nodeToRemove:
                    parent.left = subTree
                elif parent.right == nodeToRemove:
                    parent.right = subTree
            self.len -= 1
        else:
            # Node to remove has 0 children (leaf)
            nodeToRemove.parent = None
            if parent != None and parent.left == nodeToRemove:
                parent.left = None
            elif parent != None and parent.right == nodeToRemove:
                parent.right = None
            if self.root == nodeToRemove:
                self.root = None
            self.len -= 1

    
    # Finds element with key and returns it. 
    # If not found, return the node where 
    # a new node with key would be the child of.
    # returns None if the tree is empty. 
    def find(self, key):
        current = self.root
        previous = None
        while current != None:
            previous = current 
            if current.val == key:
                return current
            elif key <= current.val:
                current = current.left
            else:
                current = current.right
        return previous   

    # Returns nodes inorder
    def inorderTraversal(self, reverse = False):
        lst = []
        def helper(node):
            if node != None:
                if reverse:
                    helper(node.right)
                    lst.append(node)
                    helper(node.left)
                else:
                    helper(node.left)
                    lst.append(node)
                    helper(node.right)     
        helper(self.root)
        return lst

    def toList(self, reverse = False):
        return list(map(lambda node: node.val, self.inorderTraversal(reverse = reverse)))

    def __str__(self): return str(self.toList())

    def __len__(self): return self.len

    def getMaxNode(self):
        current = self.root
        if current == None:
            raise Exception("Cannot find maximum node of an empty BST")
        previous = None
        while current != None:
            previous = current
            current = current.right
        return previous

    def getMinNode(self):
        current = self.root
        if current == None:
            raise Exception("Cannot find minimum node of an empty BST") 
        previous = None
        while current != None:
            previous = current
            current = current.left
        return previous

    # Returns True if BST is empty
    def empty(self):
        if self.root == None: return True
        else: return False
    
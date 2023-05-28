class Node:
    def __init__(self, T):
        
        self.parent = None
        self.left = None
        self.right = None

        self.val = T.price # price level

        self.orders = [T]


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.len = 0 

    def insert(self, node):
        self.len += 1;
        if self.root == None:
            self.root = node
        else:
            target = self.find(node.val)
            node.parent = target
            if node.val <= target.val:
                target.left = node
            else:
                target.right = node

    def remove(self, key):
        nodeToRemove = self.find(key)
        if nodeToRemove.val != key:
            raise Exception("Element does not exist")
        
        parent = nodeToRemove.parent

        if nodeToRemove.left != None and nodeToRemove.right != None:
            # Node to remove has 2 children
            pass
        elif nodeToRemove.left != None or nodeToRemove.right != None:
            # Node to remove has 1 child

            # The subtree of the node that will be removed
            if nodeToRemove.left != None:
                subTree = nodeToRemove.left
            else:
                subTree = nodeToRemove.right
            
            if parent == None:
                self.root = subTree
                self.root.parent = None
            else:
                subTree.parent = parent
                if parent.left == nodeToRemove:
                    parent.left = subTree
                elif parent.right == nodeToRemove:
                    parent.right = subTree
        else:
            # Node to remove has 0 children
            if parent != None and parent.left == nodeToRemove:
                parent.left = None
            elif parent != None and parent.right == nodeToRemove:
                parent.right = None
    
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
    def inorderTraversal(self):
        lst = []
        def helper(node):
            if node != None:
                helper(node.left)
                lst.append(node)
                helper(node.right)
        helper(self.root)
        return lst

    def toList(self):
        return list(map(lambda node: node.val, self.inorderTraversal()))

    def __str__(self): return str(self.toList())

    def __len__(self): return self.len

    
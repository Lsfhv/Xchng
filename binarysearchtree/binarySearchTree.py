class Node:

    def __init__(self, T):
        
        self.parent = None
        self.left = None
        self.right = None

        self.val = T.price # price level
        self.pool = {} # map users to their size at this price level

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.max = None
        self.min = None
        self.len = 0 

    def insert(self,node):
        if self.root == None:
            self.root = node
            self.len += 1
        else:
            x = self.root
            val = node.value
            prev = None
            while x != None:
                prev = x
                if val <= x.value:
                    x = x.left
                else:
                    x = x.right
            parent = prev
            if val <= parent.value:
                parent.left = node
                node.parent = parent
            else:
                parent.right = node
                node.parent = parent             
    
    # Finds element with key and returns it. 
    # If not found, return the node where 
    # a new node with key would be the child of.
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

    

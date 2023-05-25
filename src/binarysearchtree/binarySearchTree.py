class Node:
    def __init__(self, T):
        
        self.parent = None
        self.left = None
        self.right = None

        self.val = T.price # price level
        self.pool = {T.userId: T.size} # map players to their size at this price level

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.max = None
        self.min = None
        self.len = 0 

    def insert(self,node):
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
    
    # Adds order to price level, 
    # If price level doesnt exist then create a new one.
    def update(self, order):
        toInsert = self.find(order.price)
        if toInsert.val == order.price:
            if order.userId in toInsert.pool: 
                toInsert.pool[order.userId] += order.size
            else: 
                toInsert.pool[order.userId] = order.size
        else:
            self.insert(Node(order))

    
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

    def inorderTraversal(self):
        lst = []
        def helper(node):
            if node != None:
                helper(node.left)
                lst.append(node.value)
                helper(node.right)
        helper(self.root)
        return lst
    
    def __str__(self): return str(self.inorderTraversal())

    def __len__(self): return self.len
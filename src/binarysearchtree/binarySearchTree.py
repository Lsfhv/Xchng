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

    # Removes a price level
    def remove(self, node):
        toRemove = self.find(node)
        if node.val == toRemove.val:
            if node.right != None and node.left != None:
                pass
            elif node.right != None or node.left != None:
                pass
            else:
                parent = toRemove.parent
                if parent.right == toRemove:
                    parent.right = None
                else:
                    parent.left = None
                del toRemove
        else:
            raise Exception("Element doesnt exist")
    
    # Adds order to price level, 
    # If price level doesnt exist then create a new one.
    def update(self, order):
        toInsert = self.find(order.price)
        if toInsert != None and toInsert.val == order.price:
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

    
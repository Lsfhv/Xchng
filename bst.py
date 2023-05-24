from order import Order
class Node:
    def __init__(self, T): 
        self.T = T
        self.parent = None
        self.right = None
        self.left = None
        self.value = T.price

class BST:
    def __init__(self):
        self.root = None
        self.max = None
        self.min = None
        self.len = 0 
    
    def resetCache(self):
        self.max = None
        self.min = None

    def insert(self, node):
        self.len += 1
        self.resetCache()
        if self.root == None:
            self.root = node
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

    def find(self, value):
        x = self.root
        while x != None:
            if x.value == value:
                return x.T
            elif value <= x.value:
                x = x.left
            else:
                x = x.right
        raise Exception("Element not found")

    # inorder traversal
    def __str__(self):
        lst = []
        def helper(node):
            if node != None:
                helper(node.left)
                lst.append(node.value)
                helper(node.right)
        helper(self.root)
        return str(lst)
    
    def getMax(self):
        if self.max != None:
            return self.max
        x = self.root
        while x != None:
            y = x.value
            x = x.right
        return y
    
    def getMin(self):
        if self.min != None:
            return self.min
        x = self.root
        while x!= None:
            y = x.value
            x = x.left
        return y

    def __len__(self): return self.len



# order1 = Order(1,2)
# order2 = Order(3,4)
# order3 = Order(0,0)


        
        
# bst = BST()
# bst.insert(Node(order1))
# bst.insert(Node(order2))
# bst.insert(Node(order3))

# print(bst.getMax())

# print(bst.print())

# print(bst.find(-1))
# print(bst.root.left.value)

# insertions
# deletions
# keep the max/min
# generic
# find
# seraching
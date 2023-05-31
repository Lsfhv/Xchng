from src.binarysearchtree.binarySearchTree import BinarySearchTree, Node
from constants import BID, ASK

class ObBST(BinarySearchTree):

    def __init__(self, side = None):
        super().__init__()
        self.side = side

    # Adds an order
    def update(self, order):
        node = self.find(order.price)

        if node == None:
            self.insert(Node(order))
        elif node.val == order.price:
            node.orders.append(order)
        else:
            # Price level doesnt exist so add it 
            nodeToInsert = Node(order)
            nodeToInsert.parent = node
            if nodeToInsert.val <= node.val:
                node.left = nodeToInsert
            else:
                node.right = nodeToInsert 

    def getOrdersAtPrice(self, price):
        node = self.find(price)
        if node == None:
            # No orders
            return []
        if node.val == price:
            return node.orders
        else:
            # Price level doesnt exist
            return []

    # def getOrdersBetweenInterval(self, start, end, side = None):
    #     inorder = self.inorderTraversal()
    #     if start >= end:
    #         temp = end
    #         end = start
    #         start = temp
    #     rtnlst = []
    #     lst = filter(lambda node: 
    #         node.val >= start and node.val <= end, inorder)
        
    #     for x in lst: rtnlst += x.orders
    #     x = filter(lambda order: order.side == side or side == None,rtnlst)
    #     return list(x)

    def getPriceLevelsBetween(self, start, end):
        inorder = self.inorderTraversal(self.side == ASK)
        if start >= end:
            temp = end
            end = start
            start = temp

        return list(filter(lambda node: 
            node.val >= start and node.val <= end, inorder))
        
    def getPriceLevelsUpto(self, price):
        if self.side == ASK:
            start = self.getMaxNode().val
        else:
            start = self.getMinNode().val
        return self.getPriceLevelsBetween(start, price)
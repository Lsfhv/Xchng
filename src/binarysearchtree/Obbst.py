from src.binarysearchtree.binarySearchTree import BinarySearchTree, Node
from constants import BID, ASK

class ObBST(BinarySearchTree):

    def __init__(self, side):
        super().__init__()
        if side != BID and side != ASK:
            raise TypeError("SIDE MUST TAKE BID OR ASK")
        self.side = side

    # Adds an order
    def update(self, order):
        if order.side != self.side:
            raise TypeError("Order side doesnt match the side of this bst")

        node = self.find(order.price)

        if node == None or node.val != order.price:
            self.insert(Node(order))
        else:
            node.orders.append(order)
        
    def getPriceLevelsUpto(self, price):
        try:
            start = self.getBestPrice()
        except:
            return []
        return self.getPriceLevelsBetween(start, price)

    # if bids, start >= end
    # if asks, start <= end
    # otherwise, return empty list
    # for bids, list return goes from larger -> small
    # for asks, list return goes from small -> largeer
    def getPriceLevelsBetween(self, start, end):
        inorder = self.inorderTraversal(self.side == BID)
        if self.side == ASK:
            return list(filter(lambda node: 
                node.val >= start and node.val <= end, inorder))
        else :
            return list(filter(lambda node: 
                node.val <= start and node.val >= end, inorder))

    # Returns the best price, exception in the case that it is empty
    def getBestPrice(self):
        try:
            if self.side == ASK:
                return self.getMinNode().val
            elif self.side == BID:
                return self.getMaxNode().val
        except:
            raise Exception(f"{self.side} is empty")

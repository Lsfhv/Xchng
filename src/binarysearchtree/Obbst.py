from src.binarysearchtree.binarySearchTree import BinarySearchTree, Node

class ObBST(BinarySearchTree):

    # Adds an order
    def update(self, order):
        node = self.find(order.price)
        if node.val == order.price:
            node.orders.append(order)
        else:
            # Price level doesnt exist so add it 
            nodeToInsert = Node(order)
            nodeToInsert.parent = node
            if nodeToInsert.val <= node.val:
                node.left = nodeToInsert
            else:
                node.right = nodeToInsert 


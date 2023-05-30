from src.binarysearchtree.binarySearchTree import BinarySearchTree, Node

class ObBST(BinarySearchTree):

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


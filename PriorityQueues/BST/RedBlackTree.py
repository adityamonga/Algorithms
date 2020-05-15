from BST import BST
from Node import Node

class RedBlackTree(BST):
    """RedBlackTree operations on top of Standard BST"""
    def __init__(self):
        super().__init__()

    def isRed(self, node):
        if node is None:
            return False
        return node.red

    def leftRotate(self, node):
        rnode = node.right
        node.right = rnode.left
        rnode.left = node
        rnode.red = node.red
        node.red = True

        return rnode

    def rightRotate(self, node):
        lnode = node.left
        node.left = lnode.right
        lnode.right = node
        lnode.red = node.red
        node.red = True

        return lnode

    def flipColors(self, node):
        # assert not self.isRed(node)
        # assert self.isRed(node.left)
        # assert self.isRed(node.right)
        if node == self.root:
            node.red = False
        else:
            node.red = True

        node.right.red = False
        node.left.red = False

    def put(self, key, value):
        if self.root:
            self.root = self._put(key, value, self.root)
        else:
            self.root = Node(key, value, red=False)

    def _put(self, key, value, current_node):
        if current_node is None:
            current_node = Node(key, value, red=True)

        if key < current_node.key:
            current_node.left = self._put(key, value, current_node.left)
        elif current_node.key < key:
            current_node.right = self._put(key, value, current_node.right)
        else:
            current_node.value = value

        if self.isRed(current_node.right) and not self.isRed(current_node.left):
            current_node = self.leftRotate(current_node)
        if self.isRed(current_node.left) and self.isRed(current_node.left.left):
            current_node = self.rightRotate(current_node)
        if self.isRed(current_node.left) and self.isRed(current_node.right):
            self.flipColors(current_node)

        return current_node

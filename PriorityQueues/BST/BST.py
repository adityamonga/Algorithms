from Node import Node
import random

class BST:
    """Binary Search Tree"""
    def __init__(self):
        self.root = None

    def get(self, key):
        x = self.root
        while x is not None:
            if key < x.key:
                x = x.left
            elif x.key < key:
                x = x.right
            else:
                return x.value
        return x

    def put(self, key, value):
        if self.root:
            self.root = self._put(key, value, self.root)
        else:
            self.root = Node(key, value)

    def _put(self, key, value, current_node):
        if current_node is None:
            current_node = Node(key, value)
            return current_node

        if key < current_node.key:
            current_node.left = self._put(key, value, current_node.left)
        elif current_node.key < key:
            current_node.right = self._put(key, value, current_node.right)
        else:
            current_node.value = value

        return current_node

    def inorder(self, node):
        keys = []
        if node.left:
            keys += self.inorder(node.left)
        keys.append(node)
        if node.right:
            keys += self.inorder(node.right)
        return keys

    def findMin(self, node):
        while node.left:
            node = node.left
        return node

    def findMax(self, node):
        while node.right:
            node = node.right
        return node

    def delMin(self, node):
        if node.left is None:
            return node.right

        node.left = self.delMin(node.left)
        return node

    def delete(self, key):
        self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif node.key < key:
            node.right = self._delete(node.right, key)
        else:
            if node.right is None: return node.left
            if node.left is None: return node.right

            tmp = node
            node = self.findMin(tmp.right)
            node.right = self.delMin(tmp.right)
            node.left = tmp.left

        return node

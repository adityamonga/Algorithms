class Node:
    """Node of Tree"""
    def __init__(self, key, value, red=False):
        self.key = key
        self.value = value
        self.left, self.right = None, None
        self.red = red
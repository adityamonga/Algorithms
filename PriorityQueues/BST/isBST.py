def isBST(node):
    if node is None:
        return 1

    left, right = 0, 0

    if not node.left or node.left.key < node.key:
        left = isBST(node.left)
    if not node.right or node.right.key > node.key:
        right = isBST(node.right)
    
    return left and right 
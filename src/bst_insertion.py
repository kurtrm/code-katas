"""
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bst_insert(root, val):
    """
    """
    if val < root.val:
        if root.left:
            bst_insert(root.left, val)
        else:
            root.left = TreeNode(val)
    else:
        if root.right:
            bst_insert(root.right, val)
        else:
            root.right = TreeNode(val)

"""
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def _recursive_inorder(node):
    """
    """
    if node.left:
        for val in _recursive_inorder(node.left):
            yield val
    yield node.val
    if node.right:
        for val in _recursive_inorder(node.right):
            yield val


def _iterative_inorder(node):
    """
    """
    

tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)

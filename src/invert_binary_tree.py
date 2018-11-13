"""
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def invert_binary_tree(root):
    """
    """
    if not root:
        return
    if root.left and root.right:
        root.left, root.right = root.right, root.left
    elif root.left and not root.right:
        root.right = root.left
        root.left = None
    elif root.right and not root.left:
        root.left = root.right
        root.right = None
    else:
        return root

    invert_binary_tree(root.left)
    invert_binary_tree(root.right)

    return root


def pre_order_trav(node):
    """
    """
    yield node
    if node.left:
        for left in pre_order_trav(node.left):
            yield left
    else:
        yield None
    if node.right:
        for right in pre_order_trav(node.right):
            yield right
    else:
        yield None


if __name__ == '__main__':
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)
    tree.right = TreeNode(7)
    tree.right.right = TreeNode(9)
    tree.right.left = TreeNode(6)

    invert_binary_tree(tree)

    for node in pre_order_trav(tree):
        try:
            print(node.val)
        except AttributeError:
            pass

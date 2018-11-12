"""
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def merge_bst(t1=None, t2=None):
    """
    traverse both trees
    if both aren't none:
        add values together, add

    """
    if t1 and t2:
        new_node = TreeNode(t1.val + t2.val)
        new_node.left = merge_bst(t1.left, t2.left)
        new_node.right = merge_bst(t1.right, t2.right)
    elif t1 and not t2:
        new_node = TreeNode(t1.val)
        new_node.left = merge_bst(t1.left)
        new_node.right = merge_bst(t1.right)
    elif t2 and not t1:
        new_node = TreeNode(t2.val)
        new_node.left = merge_bst(t2.left)
        new_node.right = merge_bst(t2.right)
    else:
        return None

    return new_node


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
    tree1 = TreeNode(1)
    tree1.left = TreeNode(3)
    tree1.right = TreeNode(2)
    tree1.left.left = TreeNode(5)
    tree2 = TreeNode(2)
    tree2.left = TreeNode(1)
    tree2.right = TreeNode(3)
    tree2.left.right = TreeNode(4)
    tree2.right.right = TreeNode(7)

    new_tree = merge_bst(tree1, tree2)

    for node in pre_order_trav(new_tree):
        try:
            print(node.val)
        except AttributeError:
            print(None)

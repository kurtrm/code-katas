"""
prune binary tree exercise.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def pruneTree(root):
    """
    """
    if not root:
        return None
    if root.left and root.right:
        root.left = pruneTree(root.left)
        root.right = pruneTree(root.right)
    elif root.left:
        root.left = pruneTree(root.left)
    elif root.right:
        root.right = pruneTree(root.right)
    if root.val == 0 and not root.left and not root.right:
        return None
    return root


def printTree(root):
    """
    """
    if root.left:
        for each_val in printTree(root.left):
            yield each_val
    if root.right:
        for each_val in printTree(root.right):
            yield each_val
    yield root.val


if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(1)
    node.right = TreeNode(0)
    node.left.left = TreeNode(1)
    node.left.right = TreeNode(1)
    node.left.left.left = TreeNode(0)
    node.right.left = TreeNode(0)
    node.right.right = TreeNode(1)

    # node = TreeNode(1)
    # node.left = TreeNode(0)
    # node.right = TreeNode(1)
    # node.left.left = TreeNode(0)
    # node.left.right = TreeNode(0)
    # node.right.left = TreeNode(0)
    # node.right.right = TreeNode(1)

    start = list(printTree(node))
    print(start)
    new_node = pruneTree(node)
    end = list(printTree(new_node))
    print(end)

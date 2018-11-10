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


# def _iterative_inorder(root):
#     """
#     """
#     if not root:
#         return []
#     traversal_list = []
#     node_list = []
#     curr_node = root
#     prev_node = root
#     while True:
#         if curr_node.left:
#             if prev_node == curr_node.left or prev_node == curr_node.right:
#                 traversal_list.append(curr_node.val)
#                 if curr_node.right:
#                     curr_node = curr_node.right
#                     continue
#                 else:
#                     if node_list:
#                         prev_node = curr_node
#                         curr_node = node_list.pop()
#                         continue
#                     else:
#                         break
#             else:
#                 node_list.append(curr_node)
#                 curr_node = curr_node.left
#                 continue
#             node_list.append(curr_node)
#             curr_node = curr_node.left
#         else:
#             traversal_list.append(curr_node.val)
#             if curr_node.right:
#                 prev_node = curr_node
#                 curr_node = curr_node.right
#             elif node_list:
#                 import pdb; pdb.set_trace()
#                 prev_node = curr_node
#                 curr_node = node_list.pop()
#             else:
#                 if curr_node.right:
#                     curr_node = curr_node.right
#                 else:
#                     break

    # return traversal_list


def _iterative_inorder(root):
    """
    """
    if not root:
        return []
    traversal_path = []
    node_stack = []
    curr_node = root
    left_cleared = False
    while True:
        if curr_node.left:
            if left_cleared:
                traversal_path.append(curr_node.val)
                if curr_node.right:
                    curr_node = curr_node.right
                    left_cleared = False
                else:
                    try:
                        curr_node = node_stack.pop()
                        left_cleared = True
                    except IndexError:
                        break
            else:
                node_stack.append(curr_node)
                curr_node = curr_node.left
        else:
            traversal_path.append(curr_node.val)
            if curr_node.right:
                curr_node = curr_node.right
            else:
                try:
                    curr_node = node_stack.pop()
                    left_cleared = True
                except IndexError:
                    break
    return traversal_path

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.right = TreeNode(3)
tree.left.left = TreeNode(10)
tree.right = TreeNode(5)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(23)

# [10, 2, 3, 1, 15, 5, 23]
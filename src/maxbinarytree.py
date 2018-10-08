"""
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def constructMaximumBinaryTree(nums):
    """
    """
    if not nums:
        return None
    max_num = max(nums)
    max_index = nums.index(max_num)
    node = TreeNode(max_num)
    node.left = constructMaximumBinaryTree(nums[:max_index])
    node.right = constructMaximumBinaryTree(nums[max_index+1:])

    return node


if __name__ == '__main__':
    listy = [3, 2, 1, 6, 0, 5]
    constructMaximumBinaryTree(listy)

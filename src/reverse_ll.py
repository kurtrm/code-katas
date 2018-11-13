"""
(4)->(3)->(2)->None
(2)->
"""


class Node:
    """
    """
    def __init__(self, x):
        self.val = x
        self.next = None


def _reverse_ll(node):
    """
    reverse_ll(4)
      reverse_ll(3)
        reverse_ll(2)
        returns 2
      returns 3
    """
    if node.next:
        reversal_node, head = _reverse_ll(node.next)
        node.next = None
        reversal_node.next = node
        return node, head
    else:
        return node, node


# def revised_reverse(node):
#     """
#     """
#     if not node or node.next is None:
#         return node
#     head = revised_reverse(node.next)
#     node.next.next = node
#     node.next = None
#     return head


def iterative_reversed_ll(node):
    """
    (4)->(3)->(2)->None
    None<-(4)->()()
    """
    prev, head = None, node
    while head:
        head.next, prev, head = prev, head, head.next

    return prev


def reverse_node(node):
    """
    """
    return _reverse_ll(node)[1]


if __name__ == '__main__':
    ll = Node(4)
    ll.next = Node(3)
    # ll.next.next = Node(2)

    head = iterative_reversed_ll(ll)
    while head is not None:
        print(head.val)
        head = head.next

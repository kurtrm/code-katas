"""
Merge two sorted lists.
"""


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    """
    """
    l1_next, l2_next = l1.next, l2.next
    l1.next = l2
    l2.next = l1_next
    if l1_next is None and l2_next is None:
        return l1
    if l1_next is None:
        l2.next = l2_next
        return l1
    elif l2_next is None:
        return l1
    return mergeTwoLists(l1_next, l2_next)


def print_merged(ll):
    """
    """
    x = ll
    while ll is not None:
        print(x.val)
        x = x.next


if __name__ == '__main__':
    node1 = Node(Node(Node(Node(Node(None, 5), 4), 3), 2), 1)
    node2 = Node(Node(Node(Node(Node(None, 6), 7), 8), 9), 10)
    ll = mergeTwoLists(node1, node2)
    print_merged(ll)

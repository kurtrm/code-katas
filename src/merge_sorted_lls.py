"""
Merge two sorted lists.
"""


class Node:
    def __init__(self, nxt, x):
        self.val = x
        self.next = nxt


def mergeTwoLists(l1, l2):
    """
    """
    l1_next, l2_next = l1.next, l2.next
    l1.next = l2
    if l1_next is not None and l2_next is not None:
        mergeTwoLists(l1_next, l2_next)
    if l1_next is None:
        l2.next = l2_next
    else:
        l2.next = l1_next
    return l1


def print_merged(ll):
    """
    """
    x = ll
    while x is not None:
        print(x.val)
        x = x.next


if __name__ == '__main__':
    # import pdb; pdb.set_trace()
    node1 = Node(Node(Node(Node(Node(None, 5), 4), 3), 2), 1)
    node2 = Node(Node(Node(Node(Node(None, 6), 7), 8), 9), 10)
    ll = mergeTwoLists(node1, node2)
    print_merged(ll)
    node2 = Node(Node(Node(Node(Node(None, 6), 7), 8), 9), 10)
    node3 = Node(Node(Node(None, 11), 12), 13)
    ll2 = mergeTwoLists(node3, node2)
    print('==========')
    print_merged(ll2)
    node3 = Node(Node(Node(Node(Node(None, 6), 7), 8), 9), 10)
    node2 = Node(Node(Node(None, 11), 12), 13)
    ll3 = mergeTwoLists(node3, node2)
    print('==========')
    print_merged(ll2)

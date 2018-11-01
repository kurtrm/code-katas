"""
"""


class Node:
    """
    """
    def __init__(self, x):
        self.val = x
        self.next = None


def ll_remove_dups(ll):
    """
    """
    node = ll
    runner = ll
    while True:
        while runner.next is not None:
            if node.val != runner.next.val:
                runner = runner.next
            else:
                runner.next = runner.next.next
        else:
            node = node.next
            runner = node
        if node is None:
            break

    return ll


if __name__ == '__main__':
    linky = Node(5)
    linky.next = Node(4)
    linky.next.next = Node(10)
    linky.next.next.next = Node(7)
    linky.next.next.next.next = Node(4)

    lll = linky
    while lll is not None:
        print(lll.val)
        lll = lll.next

    dups_removed = ll_remove_dups(linky)
    print('-----------')

    lll = linky
    while lll is not None:
        print(lll.val)
        lll = lll.next

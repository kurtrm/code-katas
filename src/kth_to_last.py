"""
"""


class Node:
    """
    """
    def __init__(self, x):
        self.val = x
        self.next = None


def kth_to_last_node(num: int, node: Node) -> Node:
    """
    the phrase "second to last" means return the node
    before the last node. So the user should pass 2 to get
    the second to last node. Passing 1 would return the last
    node.
    """
    if num < 1:
        return None
    num -= 1
    head = node
    runner = node
    for _ in range(num):
        runner = runner.next
    while runner.next is not None:
        runner = runner.next
        head = head.next

    return head


if __name__ == '__main__':
    linky = Node(5)
    linky.next = Node(4)
    linky.next.next = Node(10)
    linky.next.next.next = Node(7)
    linky.next.next.next.next = Node(4)
    linky.next.next.next.next.next = Node(6)
    linky.next.next.next.next.next.next = Node(18)

    for i in range(1, 8):
        print(kth_to_last_node(i, linky).val)

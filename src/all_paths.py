"""
Given DAG find all paths from 0 to N-1.
"""


def all_paths(graph):
    """
    """
    end = len(graph) - 1
    paths = []
    stack = []
    for node in graph[0]:
        if node == end:
            paths.append([0, node])
        else:
            stack.append([0, node])
    while stack:
        popped = stack.pop()
        next_node = graph[popped[-1]]
        for node in next_node:
            new_popped = popped + [node]
            if node == end:
                paths.append(new_popped)
            else:
                stack.append(new_popped)
    return paths


if __name__ == '__main__':
    dag = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    print(all_paths(dag))

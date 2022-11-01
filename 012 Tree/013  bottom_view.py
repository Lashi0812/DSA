# %%
from collections import defaultdict
from queue import Queue


# %%
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def bottom_view(node):
    hashmap = defaultdict(list)
    q: Queue[tuple[int, Node]] = Queue()
    max_level = min_level = 0

    # initialise the root
    hashmap[0].append(node.data)
    q.put((0, node))

    while not q.empty():
        level, temp = q.get()
        max_level = max(max_level, level)
        min_level = min(min_level, level)
        if temp.left is not None:
            q.put((level - 1, temp.left))
            hashmap[level - 1].append(temp.left.data)
        if temp.right is not None:
            q.put((level + 1, temp.right))
            hashmap[level + 1].append(temp.right.data)

    view = []
    for lev in range(min_level, max_level + 1):
        view.append(hashmap[lev][-1])

    return view


# %%
if __name__ == '__main__':
    root = Node(9)
    root.left = Node(60)
    root.left.left = Node(2)
    root.left.left.left = Node(6)
    root.left.left.right = Node(-3)

    root.right = Node(4)
    root.right.left = Node(3)
    root.right.right = Node(8)
    root.right.right.right = Node(17)
    root.right.left.left = Node(10)
    root.right.left.right = Node(11)

    print(bottom_view(root))

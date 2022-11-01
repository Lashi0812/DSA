# %%
from collections import defaultdict
from queue import Queue
from typing import Optional


# %%
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def get_children(self) -> dict:
        child = {}
        if self.left is not None:
            child["l"] = self.left
        if self.right is not None:
            child["r"] = self.right
        return child


def vertical_level_traversal(node: Node):
    hashmap = defaultdict(list)
    q: Queue[tuple[int, Node]] = Queue()

    # initialise for root
    hashmap[0].append(node.data)
    q.put((0, node))

    while not q.empty():
        level, temp = q.get()
        for side, ele in temp.get_children().items():
            if side == "l":
                q.put((level - 1, ele))
                hashmap[level - 1].append(ele.data)
            elif side == "r":
                hashmap[level + 1].append(ele.data)
                q.put((level + 1, ele))

    order = []
    for _, v in sorted(hashmap.items()):
        order += v

    return order


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

    print(vertical_level_traversal(root))

"""
Return the path from the root to element
"""

# %%
from typing import Optional


# %%
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def path(node, element, paths=None):
    if paths is None:
        paths = list()
    if node is None:
        return paths
    if node.data == element:
        paths.append(node.data)
        return paths[::-1]
    if path(node.left, element, paths) or path(node.right, element, paths):
        paths.append(node.data)
        return paths[::-1]
    return paths[::-1]


# %%
if __name__ == '__main__':
    root = Node(7)
    root.left = Node(8)
    root.left.left = Node(9)
    root.left.right = Node(15)
    root.left.right.left = Node(19)
    root.right = Node(11)
    root.right.left = Node(4)
    root.right.right = Node(16)
    root.right.right.left = Node(20)
    root.right.right.right = Node(17)
    ele = 15
    print(f" path of {ele} from the root? ", path(root, ele))

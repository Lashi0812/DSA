"""
search if the k element exits in your tree return true
"""
# %%
from typing import Optional


# %%
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def search(node, element):
    if node is None:
        return False
    if node.data == element:
        return True
    return search(node.left, element) or search(node.right, element)


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
    ele = 3
    print(f" Does the {ele} in the tree? ", search(root, 8))

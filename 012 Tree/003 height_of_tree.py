"""
Calculate the Height of the tree
"""
# %%
from typing import Optional


# %%
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __repr__(self):
        return str(self.data)


def height(node):
    if node is None:
        return -1
    return max(height(node.left), height(node.right)) + 1


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
    print("Height of the tree", height(root))

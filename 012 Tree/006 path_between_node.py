"""
Given the two element in the tree , return the path between the two element
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
        return paths
    if path(node.left, element, paths) or path(node.right, element, paths):
        paths.append(node.data)
        return paths
    return paths


def path_between(node, one, another):
    path_a = path(node, one)
    path_b = path(node, another)
    complete_path = []
    for ele in path_a:
        if ele in path_b:
            idx = path_b.index(ele)
            complete_path += path_b[idx::-1]
            break
        complete_path.append(ele)
    return complete_path


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
    a = 20
    b = 19
    print(f" path between {a} and {b}  ", path_between(root, a, b))

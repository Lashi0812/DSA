"""
Given the improper bst make them as the proper bst.

Improper Bst mean : Two node are improperly placed in the Tree .Place these node in the correct place.
"""
# %%
from typing import Optional


# %%
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


def construct_bst(array, start, end):
    if start > end:
        return None
    mid = (start + end) >> 1
    root = Node(array[mid])
    root.left = construct_bst(array, start, mid - 1)
    root.right = construct_bst(array, mid + 1, end)
    return root


def find_improper(node, previous=None, first=None, second=None):
    if node is None:
        return previous, first, second
    # go to left
    previous, first, second = find_improper(node.left, previous, first, second)
    # access the root
    if previous is not None and node.data < previous.data:
        if first is None:
            first = previous
        second = node
    previous = node
    previous, first, second = find_improper(node.right, previous, first, second)
    return previous, first, second


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end=" -> ")
    inorder(node.right)


def preorder(node):
    if node is None:
        return
    print(node.data, end=" -> ")
    preorder(node.left)
    preorder(node.right)


# %%
if __name__ == '__main__':
    array1 = [2, 6, 13, 9, 11, 7, 15, 16, 18, 21]
    tree = construct_bst(array1, 0, len(array1) - 1)
    inorder(tree)
    print()
    preorder(tree)
    print()
    print(find_improper(tree))

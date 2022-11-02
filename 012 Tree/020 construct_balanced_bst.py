"""
    Given the sortd array , construct the balanced binary search tree.

    Balanced Binary Search Tree means all the node will have height of right child - height of left child should not
    greater than 1
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = self.right = None

    def __repr__(self):
        return str(self.data)


def construct_balanced_bst(array, start, end):
    if start > end:
        return None
    mid = (end + start) >> 1
    root = Node(array[mid])
    root.left = construct_balanced_bst(array, start, mid - 1)
    root.right = construct_balanced_bst(array, mid + 1, end)
    return root


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


if __name__ == '__main__':
    array1 = [1, 3, 5, 8, 10, 15, 18, 20]
    tree = construct_balanced_bst(array1, 0, len(array1) - 1)
    inorder(tree)
    print()
    preorder(tree)

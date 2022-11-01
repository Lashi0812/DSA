# %%
from typing import Optional


# %%
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def construct_tree(preorder, inorder):
    if len(preorder) < 1:
        return
    # first element in the preorder will the root
    root = preorder[0]
    node = Node(root)
    # find the lst and rst
    num_lst = inorder.index(root)
    pre_lst = preorder[1:num_lst + 1]
    in_lst = inorder[:num_lst]

    pre_rst = preorder[num_lst + 1:]
    in_rst = inorder[num_lst + 1:]

    node.left = construct_tree(pre_lst, in_lst)
    node.right = construct_tree(pre_rst, in_rst)

    return node


def preorder(node):
    if node is None:
        return

    # access the root data
    print(node.data, end=" -> ")

    # go to left
    preorder(node.left)

    # go to right
    preorder(node.right)


def postorder(node):
    if node is None:
        return
        # go to left
    postorder(node.left)

    # go to right
    postorder(node.right)

    # access the root
    print(node.data, end=",")


# %%
if __name__ == '__main__':
    pre = [8, 6, 5, 15, 19, 9, 18, 25, 4, 7, 41, 30, 39, 48]
    ino = [15, 5, 19, 6, 18, 9, 25, 8, 7, 41, 4, 39, 30, 48]
    preorder(construct_tree(pre, ino))
    postorder(construct_tree(pre,ino))

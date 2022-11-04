"""
Given the Binary search tree find the kth element
"""


# %%
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


def construct_tree(preorder, inorder):
    root = _construct_tree(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
    return root


def _construct_tree(preorder, ps, pe, inorder, ins, ine):
    if ps > pe:
        return
    # find the root
    root = Node(preorder[ps])
    # find the root index in the inorder
    idx = inorder.index(preorder[ps])
    # number of element in the lst
    num_lst = idx - ins
    # construct the tree
    root.left = _construct_tree(preorder, ps + 1, ps + num_lst, inorder, ins, idx - 1)
    root.right = _construct_tree(preorder, ps + num_lst + 1, pe, inorder, idx + 1, ine)

    return root


def find_kth_element(node, k, count=0):
    while k > count:
        if node is None:
            return count
        # go to left
        count = find_kth_element(node.left, k, count)
        # access the root
        count += 1
        if count == k:
            print(node.data)
        count = find_kth_element(node.right, k, count)
        return count
    return count


def get_inorder(node):
    if node is None:
        return
    get_inorder(node.left)
    print(node.data, end=" -> ")
    get_inorder(node.right)


def get_preorder(node):
    if node is None:
        return
    print(node.data, end=" -> ")
    get_preorder(node.left)
    get_preorder(node.right)


# %%
if __name__ == '__main__':
    pre = [10, 5, 2, 7, 6, 8, 20, 22, 21, 50]
    ino = [2, 5, 6, 7, 8, 10, 20, 21, 22, 50]
    tree = construct_tree(pre, ino)
    get_inorder(tree)
    print()
    get_preorder(tree)
    print()
    print(find_kth_element(tree,11))

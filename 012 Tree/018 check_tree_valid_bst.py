"""
Given the tree we need to check that tre is valid Binary search Tree


Approach 1 (Inorder traversal):
    find the inorder traversal
    Check inorder traversal is sorted or not

Approach 2 (Bottom up Approach):
    max of lst < root < min of rst
    1. find the maximum in the lst
    2. find the minimum in the rst
    3. Check for the condition

Approach 3 (Top-down Approach):
    1. maintain the range
    2. check that node is within the range
    3. When going left change the upper bound to parent - 1
    4. When going right change the lower bound to parent +1
"""
# %%
from typing import Optional


# %%
class Node:
    def __init__(self, data=None):
        self.data = data
        self.right: Optional[Node] = None
        self.left: Optional[Node] = None

    def __repr__(self):
        return self.data


class BinarySearchTree:
    def __init__(self):
        self.root: Optional[Node] = None

    def construct_tree(self, preorder, inorder):
        self.root = self._construct_tree(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
        return self.root

    def _construct_tree(self, preorder, ps, pe, inorder, ins, ine):
        if ps > pe:
            return
        # find the root
        root = Node(preorder[ps])
        # find the root index in the inorder
        idx = inorder.index(preorder[ps])
        # number of element in the lst
        num_lst = idx - ins
        # construct the tree
        root.left = self._construct_tree(preorder, ps + 1, ps + num_lst, inorder, ins, idx - 1)
        root.right = self._construct_tree(preorder, ps + num_lst + 1, pe, inorder, idx + 1, ine)

        return root

    def _inorder_traversal(self, node, inorder=None):

        if inorder is None:
            inorder = list()
        if node is None:
            return

        self._inorder_traversal(node.left, inorder)
        inorder.append(node.data)
        self._inorder_traversal(node.right, inorder)

        return inorder

    def _approach1(self, temp):
        order = self._inorder_traversal(temp)
        if order == sorted(order):
            return True
        else:
            return False

    def _approach2(self, node, maxi=float("inf"), mini=float("-inf"), valid=True):
        while valid:
            if node is None:
                return float("inf"), float("-inf"), True
            min_l, max_l, valid = self._approach2(node.left, maxi, mini, valid)
            min_r, max_r, valid = self._approach2(node.right, maxi, mini, valid)
            data = node.data
            if max_l < data < min_r:
                minimum = min(min_l, data)
                maximum = max(max_r, data)
                return minimum, maximum, valid
            else:
                return mini, maxi, False
        return maxi, mini, valid

    def _approach3(self, node, lower_bound=float("-inf"), upper_bound=float("inf")):
        if node is None:
            return True
        data = node.data
        if lower_bound < data < upper_bound:
            return self._approach3(node.left, lower_bound, data) and self._approach3(node.right, data, upper_bound)
        else:
            return False

    def check_valid_bst(self):
        temp = self.root
        return self._approach3(temp)


# %%
if __name__ == '__main__':
    ino = [3, 5, 7, 9, 10, 13, 14, 15, 19, 20]
    pre = [10, 5, 3, 9, 7, 15, 13, 14, 20, 19]
    bst = BinarySearchTree()
    root = bst.construct_tree(pre, ino)
    print(bst.check_valid_bst())

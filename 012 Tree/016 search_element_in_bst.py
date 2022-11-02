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

    def search_element(self, ele):
        temp = self.root
        while temp is not None:
            if temp.data == ele:
                return True
            elif temp.data > ele:
                # then root is greater than searching element then element will in the left
                temp = temp.left
            else:
                temp = temp.right
        return False

    def _inorder_traversal(self, node):
        if node is None:
            return
        # go to left
        self._inorder_traversal(node.left)
        # access the root
        print(node.data, end=" -> ")
        # go to right
        self._inorder_traversal(node.right)

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        return self._inorder_traversal(node)

    def _preorder_traversal(self, node):
        if node is None:
            return
        # access the root
        print(node.data, end=" -> ")
        # go to left
        self._preorder_traversal(node.left)
        # go to right
        self._preorder_traversal(node.right)

    def preorder_traversal(self, node=None):
        if node is None:
            node = self.root
        return self._preorder_traversal(node)

    def _postorder_traversal(self, node):
        if node is None:
            return
        # go to left
        self._postorder_traversal(node.left)
        # go to right
        self._postorder_traversal(node.right)
        # access the root
        print(node.data, end=" -> ")

    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        return self._postorder_traversal(node)


#%%
if __name__ == '__main__':
    ino = [1, 4, 6, 7, 8, 10, 13, 15, 17]
    pre = [8, 4, 1, 7, 6, 13, 10, 15, 17]
    bst = BinarySearchTree()
    root = bst.construct_tree(pre, ino)
    bst.preorder_traversal()
    print()
    bst.postorder_traversal()
    print(bst.search_element(100))

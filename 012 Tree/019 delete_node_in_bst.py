# %%
from typing import Optional


# %%
class Node:
    def __init__(self, data=None):
        self.data = data
        self.right: Optional[Node] = None
        self.left: Optional[Node] = None

    def get_number_of_child(self):
        count = 0
        if self.right is not None:
            count += 1
        if self.left is not None:
            count += 1
        return count

    def __repr__(self):
        return str(self.data)


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

    def delete(self, ele):
        def connect_node_with_parent(temp):
            if parent.left == node:
                parent.left = temp
            else:
                parent.right = temp

        node = self.root
        parent = None
        # Search the element
        while node.data != ele:
            parent = node
            if node.data > ele:
                node = node.left
            else:
                node = node.right

        # perform deletion operation
        if node is not None:
            if parent is not None:
                if node.get_number_of_child() == 0:
                    connect_node_with_parent(None)
                elif node.get_number_of_child() == 1:
                    if node.left is not None:
                        temp = node.left
                    else:
                        temp = node.right
                    connect_node_with_parent(temp)
                else:
                    # find the maximum in lst and removing the maximum node
                    lst_maxi_parent = None
                    lst_maxi = node.left
                    while lst_maxi.right is not None:
                        lst_maxi_parent = lst_maxi
                        lst_maxi = lst_maxi.right
                    # there is chance of having the no right in lst
                    if lst_maxi_parent is None:
                        node.left = lst_maxi.left
                    else:
                        lst_maxi_parent.right = lst_maxi.left

                    # replace the node to remove with lst maximum node
                    lst_maxi.right = node.right
                    lst_maxi.left = node.left

                    # connect the parent of node to remove with lst maximum
                    connect_node_with_parent(lst_maxi)
                return self.root
            else:
                if node.get_number_of_child() == 1:
                    if node.left is None:
                        node = node.right
                    else:
                        node = node.left
                    return self.root
                elif node.get_number_of_child() == 2:
                    # find the maximum in lst and removing the maximum node
                    lst_maxi_parent = None
                    lst_maxi = node.left
                    while lst_maxi.right is not None:
                        lst_maxi_parent = lst_maxi
                        lst_maxi = lst_maxi.right
                    # there is chance of having the no right in lst
                    if lst_maxi_parent is None:
                        node.left = lst_maxi.left
                    else:
                        lst_maxi_parent.right = lst_maxi.left

                    # replace the node to remove with lst maximum node
                    lst_maxi.right = node.right
                    lst_maxi.left = node.left

                    node.right = None
                    node.left = None

                    return lst_maxi
        else:
            print("Node is not found")
            return self.root


def get_preorder(node):
    if node is None:
        return

    # access the root data
    print(node.data, end=" -> ")

    # go to left
    get_preorder(node.left)

    # go to right
    get_preorder(node.right)


def get_inorder(node):
    if node is None:
        return
    # go to left
    get_inorder(node.left)
    # access the root data
    print(node.data, end=" -> ")
    # go to right
    get_inorder(node.right)


# %%
if __name__ == '__main__':
    ino = [-2, 3, 5, 6, 7, 10, 11, 12, 14, 15, 19, 25]
    pre = [10, 5, 3, -2, 7, 6, 15, 12, 11, 14, 19, 25]
    bst = BinarySearchTree()
    root = bst.construct_tree(pre, ino)
    t = bst.delete(10)
    get_inorder(t)

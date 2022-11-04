"""
Perform the inorder traversal with space complexity of O(1) don't use the recursive stack space
"""


# %%

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = self.right = None

    def __repr__(self):
        return str(self.data)


def _construct_tree(preorder, ps, pe, inorder, ins, ine):
    if ps > pe:
        return
        # get the root node
    root = Node(preorder[ps])
    # find the root in the inorder
    idx = inorder.index(preorder[ps])
    # number element in the lst
    num_lst = idx - ins
    # create the left
    root.left = _construct_tree(preorder, ps + 1, ps + num_lst, inorder, ins, idx - 1)
    root.right = _construct_tree(preorder, ps + num_lst + 1, pe, inorder, idx + 1, ine)
    return root


def construct_tree(preorder, inorder):
    return _construct_tree(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)


def moris_inorder_traversal(root):
    cur = root
    while cur is not None:
        if cur.left is None:
            print(cur.data, end=" -> ")
            cur = cur.right
        else:
            # before moving to left we need to store the cur in the inorder predecessor right
            inorder_predecessor = cur.left
            # find the inorder predecessor
            while inorder_predecessor.right is not None and inorder_predecessor.right != cur:
                # move to right until you find the max in the lst
                inorder_predecessor = inorder_predecessor.right
            # first traversal to find inorder predecessor
            if inorder_predecessor.right is None:
                # make the connection with cur
                inorder_predecessor.right = cur
                # now you can move cur to left
                cur = cur.left
            # second traversal to find the inorder traversal
            else:
                # disconnect the connection of inorder predecessor with curr
                inorder_predecessor.right = None
                # we have done left traversal and reached the root
                print(cur.data, end=" -> ")
                # now we can move to right
                cur = cur.right


def get_inorder(node):
    if node is None:
        return
    get_inorder(node.left)
    print(node.data, end=" -> ")
    get_inorder(node.right)


# %%
if __name__ == '__main__':
    ino = [6, 8, 9, 10, 15, 17, 19, 20, 23, 25, 29, 30, 32, 33, 35, 39]
    pre = [6, 8, 29, 20, 15, 9, 10, 17, 19, 23, 25, 32, 30, 35, 33, 39]
    tree = construct_tree(pre, ino)
    get_inorder(tree)
    print()
    moris_inorder_traversal(tree)

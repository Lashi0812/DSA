# %%
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = self.right = None

    def __repr__(self):
        return str(self.data)


def _construct_tree(preorder, ps, pe, inorder, ins, ine):
    if ps > pe:
        return None
    root = Node(preorder[ps])
    idx = inorder.index(preorder[ps])
    num_lst = idx - ins
    root.left = _construct_tree(preorder, ps + 1, ps + num_lst, inorder, ins, idx - 1)
    root.right = _construct_tree(preorder, ps + num_lst + 1, pe, inorder, idx + 1, ine)
    return root


def construct_tree(preorder, inorder):
    return _construct_tree(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)


def count_node_at_level(node, k):
    if node is None:
        return 0
    if k == 0:
        return 1
    return count_node_at_level(node.left, k - 1) + count_node_at_level(node.right, k - 1)


# %%
if __name__ == '__main__':
    ino = [6, 8, 9, 10, 15, 17, 19, 20, 23, 25, 29, 30, 32, 33, 35, 39]
    pre = [6, 8, 29, 20, 15, 9, 10, 17, 19, 23, 25, 32, 30, 35, 33, 39]
    tree = construct_tree(pre, ino)
    print(count_node_at_level(tree, 0))
    #print(globals())
    print(locals())
    print(__builtins__)

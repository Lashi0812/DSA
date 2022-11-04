class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = self.right = None

    def __repr__(self):
        return str(self.data)


def _construct_tree(preorder, ps, pe, inorder, ins, ine):
    if ps > pe:
        return
    root = Node(preorder[ps])
    idx = inorder.index(preorder[ps])
    num_lst = idx - ins
    root.left = _construct_tree(preorder, ps + 1, ps + num_lst, inorder, ins, idx - 1)
    root.right = _construct_tree(preorder, ps + num_lst + 1, pe, inorder, idx + 1, ine)
    return root


def construct_tree(preorder, inorder):
    return _construct_tree(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)


def max_path_sum(node):
    if node is None:
        return 0
    return node.data + max(max_path_sum(node.left), max_path_sum(node.right), 0)


def max_path_sum_contain_root(node):
    if node is None:
        return 0
    return node.data + max(max_path_sum(node.left), 0) + max(max_path_sum(node.right), 0)


if __name__ == '__main__':
    ino = [-3, -8, 1, 6, 5, 11, 4, 3, -2]
    pre = [5, -8, -3, 6, 1, 4, 11, -2, 3]
    tree = construct_tree(pre, ino)
    print(max_path_sum(tree))
    print(max_path_sum_contain_root(tree))

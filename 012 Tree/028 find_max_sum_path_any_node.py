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


def max_path_sum_any_node(node):
    if node is None:
        return 0
    ans = 0

    def max_path_sum(node):
        nonlocal ans
        if node is None:
            return 0
        sums = node.data + max(max_path_sum(node.left), max_path_sum(node.right), 0)
        ans = max(ans, sums)
        return sums

    max_path_sum(node)
    return ans


if __name__ == '__main__':
    ino = [6, -8, 15, 3, 4, 2, -3, 1, -6]
    pre = [4, -8, 6, 3, 15, -3, 2, -6, 1]
    tree = construct_tree(pre, ino)
    print(max_path_sum_any_node(tree))

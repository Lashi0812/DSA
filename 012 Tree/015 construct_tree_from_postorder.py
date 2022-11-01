# %%
class Node:
    def __init__(self, value=None):
        self.data = value
        self.left = None
        self.right = None


def construct_tree(post, ps, pe, ino, ins, ine):
    # base condition
    if ps > pe:
        return
    # find the root
    root = Node(post[pe])
    # find the number of element in lst
    ind = hashmap[post[pe]]
    num_lst = ind - ins
    # add the node to root
    root.left = construct_tree(post, ps, ps + num_lst - 1, ino, ins, ind - 1)
    root.right = construct_tree(post, ps + num_lst, pe - 1, ino, ind + 1, ine)

    return root


def get_preorder(node):
    if node is None:
        return

    # access the root data
    print(node.data, end=" -> ")

    # go to left
    get_preorder(node.left)

    # go to right
    get_preorder(node.right)


def get_postorder(node):
    if node is None:
        return
        # go to left
    get_postorder(node.left)

    # go to right
    get_postorder(node.right)

    # access the root
    print(node.data, end=",")


# %%
if __name__ == '__main__':
    preorder = [8, 6, 5, 15, 19, 9, 18, 25, 4, 7, 41, 30, 39, 48]
    postorder = [15, 19, 5, 18, 25, 9, 6, 41, 7, 39, 48, 30, 4, 8]
    inorder = [15, 5, 19, 6, 18, 9, 25, 8, 7, 41, 4, 39, 30, 48]
    hashmap = {v: k for k, v in enumerate(inorder)}
    get_preorder(construct_tree(postorder, 0, len(postorder) - 1, inorder, 0, len(inorder) - 1))
    print()
    get_postorder(construct_tree(postorder, 0, len(postorder) - 1, inorder, 0, len(inorder) - 1))

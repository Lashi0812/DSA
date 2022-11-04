from collections import deque


class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = self.left = None

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
    return _construct_tree(preorder=preorder, ps=0, pe=len(preorder) - 1, inorder=inorder, ins=0, ine=len(inorder) - 1)


def iterative_inorder_traversal(root):
    cur = root
    stack = deque()
    while len(stack) != 0 or cur is not None:
        while cur is not None:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        print(cur.data, end=" -> ")
        cur = cur.right


def iterative_preorder_traversal(root):
    cur = root
    stack = deque()
    while len(stack) != 0 or cur is not None:
        while cur is not None:
            print(cur.data, end=" -> ")
            stack.append(cur.right)
            cur = cur.left
        cur = stack.pop()


def iterative_postorder_traversal(root):
    cur = root
    stack = deque()
    # store the last visited node
    prev = None
    while len(stack) != 0 or cur is not None:
        # go to left
        while cur is not None:
            stack.append(cur)
            cur = cur.left
        cur = stack[-1]
        # go to right
        if cur.right is None or prev == cur.right:
            print(cur.data, end=" -> ")
            stack.pop()
            # update the previous
            prev = cur
            cur = None
        else:
            cur = cur.right


if __name__ == '__main__':
    ino = [12, 9, 19, 7, 3, 15, 14, -12, 6, 4, 18]
    pre = [3, 7, 9, 12, 19, 4, 14, 15, -12, 6, 18]
    tree = construct_tree(pre, ino)
    iterative_inorder_traversal(tree)
    print()
    iterative_preorder_traversal(tree)
    print()
    iterative_postorder_traversal(tree)

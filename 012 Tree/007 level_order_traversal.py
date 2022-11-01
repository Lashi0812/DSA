# %%
from queue import Queue
from typing import Optional


# %%
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def get_children(self):
        child = []
        if self.left is not None:
            child.append(self.left)
        if self.right is not None:
            child.append(self.right)
        return child


def level_order_traversal(node):
    if node is None:
        return -1
    q = Queue()
    q.put(node)
    q.put(None)
    while q.qsize() > 1:
        temp = q.get()
        if temp is not None:
            print(temp.data, end=" , ")
            for ele in temp.get_children():
                q.put(ele)
        else:
            q.put(None)
            print()


# %%
if __name__ == '__main__':
    root = Node(3)
    root.left = Node(7)
    root.left.left = Node(9)
    root.left.left.left = Node(12)
    root.left.left.right = Node(19)

    root.right = Node(4)
    root.right.left = Node(14)
    root.right.right = Node(18)
    root.right.right.right = Node(5)
    root.right.left.left = Node(15)
    root.right.left.left.left = Node(21)
    root.right.left.left.right = Node(2)
    root.right.left.right = Node(1)
    root.right.left.right.right = Node(6)
    level_order_traversal(root)

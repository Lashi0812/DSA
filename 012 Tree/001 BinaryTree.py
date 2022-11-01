# %%
from typing import Optional


# %%

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class Tree:
    def __init__(self):
        self.root = None

    def inorder(self, node):
        # stop condition
        if node is None:
            return
        # Go the left
        self.inorder(node.left)
        # access the root
        print(node.data, end=" -> ")
        # Go the Right
        self.inorder(node.right)

    def preorder(self, node):
        if node is None:
            return

        # access the root data
        print(node.data, end=" -> ")

        # go to left
        self.preorder(node.left)

        # go to right
        self.preorder(node.right)

    def postorder(self, node):
        if node is None:
            return

            # go to left
        self.preorder(node.left)

        # go to right
        self.preorder(node.right)

        # access the root  data
        print(node.data, end=" -> ")


# %%
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(34)
    root.right = Node(89)
    root.left.left = Node(45)
    root.left.right = Node(50)
    tree = Tree()
    print("Inorder    = ", tree.inorder(root))
    print("Pre  order = ", tree.preorder(root))
    print("Post order = ", tree.postorder(root))

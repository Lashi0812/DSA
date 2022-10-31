# %%
from typing import MutableSequence, Optional


# %%
class Node:
    def __init__(self, data) -> None:
        self.next: Optional[Node] = None
        self.data = data

    def __repr__(self) -> str:
        return str(self.data)


class Stack:
    def __init__(self, data: Optional[MutableSequence] = None) -> None:
        self.head: Optional[Node] = None

        if data is not None and data:
            for ele in data:
                self.push(ele)

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        if self.head is not None:
            self.head = self.head.next
        else:
            print("you cant perform pop operation in the empty stack")

    def top(self):
        return self.head

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return str(nodes)


# %%
if __name__ == "__main__":
    stack = Stack()
    print(stack)
    stack.push(17)
    stack.push(5)
    stack.push(3)
    stack.push(2)
    print(stack)
    stack.pop()
    print(stack)
    print(stack.top())
    stack.pop()
    print(stack)
    stack.push(8)
    stack.push(-1)
    print(stack)
    stack.pop()
    print(stack)
    print(stack.top())
    print(stack)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
# %%

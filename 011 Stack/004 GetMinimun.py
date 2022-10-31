"""
    Implement the stack with get minimum operation
"""
# %%
import sys
from typing import MutableSequence, Optional


# %%
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        return str(self.data)


class Stack:
    class MinStack:
        def __init__(self) -> None:
            self.head: Optional[Node] = None

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

        def top(self) -> int:
            if self.head is None:
                return sys.maxsize
            return self.head.data

    def __init__(self, data: Optional[MutableSequence] = None) -> None:
        self.head: Optional[Node] = None
        self.min_stack: Stack.MinStack = Stack.MinStack()

        if data is not None and data:
            for ele in data:
                self.push(ele)

    def push(self, data):
        node = Node(data)
        cur_min = min(self.min_stack.top(), data)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

        self.min_stack.push(cur_min)

    def pop(self):
        if self.head is not None:
            self.head = self.head.next
        self.min_stack.pop()

    def getMin(self):
        return self.min_stack.top()


# %%
if __name__ == "__man__":
    stack = Stack([7, 5, 2, 8, 1])
    print(stack.getMin())
    stack.pop()
    print(stack.getMin())

# %%

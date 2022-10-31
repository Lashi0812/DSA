"""
    Implement the stack with get minimum operation without extra operation
"""

# %%
import sys


# %%
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return str(self.data)


class Stack:
    def __init__(self, data=None) -> None:
        self.head = None
        self.cur_min = sys.maxsize

        if data is not None and data:
            for ele in data:
                self.push(ele)

    def push(self, data):
        if self.head is None:
            node = Node(data)
        else:
            cur_min = min(self.cur_min, data)
            if cur_min != self.cur_min:
                node = Node(2 * data - self.cur_min)
            else:
                node = Node(data)
        node.next = self.head
        self.head = node
        self.cur_min = min(self.cur_min, data)

    def top(self):
        if self.head is not None:
            return self.head.data

    def pop(self):
        if self.top() < self.cur_min:
            self.cur_min = 2 * self.cur_min - self.top()
        self.head = self.head.next

    def get_min(self):
        return self.cur_min


# %%
if __name__ == "__main__":
    stack = Stack([7, 5, 2, 8, 1])
    print(stack.get_min())
    stack.pop()
    print(stack.get_min())

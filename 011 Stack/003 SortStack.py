"""
    Sort the stack in ascending order using the another stack
"""

from typing import MutableSequence, Optional


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        return str(self.data)


class Stack:
    def __init__(self, data: Optional[MutableSequence] = None) -> None:
        self.head: Optional[Node] = None

        if data is not None and data:
            for ele in data:
                self.push(ele)

    def is_empty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        if not self.isEmpty():
            self.head = self.head.next  # type: ignore
        else:
            print("Stack is empty ypu cant perform this operation")

    def top(self) -> Optional[Node]:
        return self.head

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return str(nodes)


# %%
class Solution:
    def sort(self, s1: Stack):
        s2 = Stack()
        while not s1.isEmpty():
            temp = s1.top().data  # type: ignore
            s1.pop()
            if not s2.isEmpty():
                while not s2.isEmpty() and s2.top().data > temp:  # type: ignore
                    s1.push(s2.top().data)  # type: ignore
                    s2.pop()
            s2.push(temp)

        while not s2.isEmpty():
            s1.push(s2.top().data)  # type: ignore
            s2.pop()

        return s1


# %%
if __name__ == "__main__":
    stack = Stack([4, 6, -5, 0, -1, 2, 5, 3, 1])
    test = Solution()
    test.sort(stack)
    print(test.sort(stack))

# %%

"""
For every index i, Find the nearest element on the left side which is smaller than array[i]

Input : 4   5   2   10  8   2
Output: -1  4   -1  2   2   -1
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self.head = None

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

    def top(self):
        if self.head is not None:
            return self.head.data


def nearest_smallest_element(array):
    near_small_array = []
    smallest_stack = Stack()

    for ele in array:

        # loop until get the smallest element in the stack
        while smallest_stack.head is not None and smallest_stack.top() >= ele:
            smallest_stack.pop()

        if smallest_stack.head is None:
            near_small_array.append(-1)
        else:
            near_small_array.append(smallest_stack.top())

        smallest_stack.push(ele)

    return near_small_array


# %%
if __name__ == '__main__':
    array = [4, 6, 10, 11, 7, 8, 3, 5]
    print(nearest_smallest_element(array))
    array1 = [4, 5, 2, 10, 8, 2]
    print(nearest_smallest_element(array1))

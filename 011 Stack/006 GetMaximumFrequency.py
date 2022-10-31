"""
Implement the stack with operation -> that return the maximum frequency and if two element have the save same
frequency return whichever is closet to the top
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class Stack:
    class FrequencyStack:
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

        def __repr__(self) -> str:
            node = self.head
            nodes = []
            while node is not None:
                nodes.append(node.data)
                node = node.next
            return str(nodes)

    def __init__(self, data=None):
        self.head = None
        self.freq_stack = Stack.FrequencyStack()
        self.cur_max = None
        self.hashmap = {}

        if data is not None:
            for ele in data:
                self.push(ele)

    def push(self, data):
        node = Node(data)
        if self.head is None:
            # directly insert in the head
            self.head = node

            # insert in the hashmap
            self.hashmap[data] = 1

            # insert in the frequency stack
            self.freq_stack.push(data)

            # set as current max
            self.cur_max = data
        else:
            # make connection with head and insert in the head
            node.next = self.head
            self.head = node

            # insert in the hashmap
            self.hashmap[data] = self.hashmap.get(data, 0) + 1

            # get maximum element in the hashmap
            maxi = max(self.hashmap.values())
            maxi_ele = [k for k, v in self.hashmap.items() if v == maxi]

            if data in maxi_ele:
                self.cur_max = data

            self.freq_stack.push(self.cur_max)

    def pop(self):
        if self.head is not None:
            self.head = self.head.next

        if self.freq_stack.head is not None:
            self.freq_stack.head = self.freq_stack.head.next
            self.cur_max = self.freq_stack.head.data

    def get_max_freq(self):
        return self.cur_max

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return str(nodes)


# %%
if __name__ == '__main__':
    stack = Stack([5, 7, 2, 5, 2, 1, 7, 5, 6, 2, 7])
    print(stack.get_max_freq())
    print(stack)
    print(stack.freq_stack)
    stack.pop()
    stack.pop()
    print(stack.get_max_freq())
    print(stack)
    print(stack.freq_stack)


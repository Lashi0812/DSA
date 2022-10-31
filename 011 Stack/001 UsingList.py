# %%

# %%
class Stack:
    def __init__(self, data=None) -> None:
        self.top = -1
        self.data = []
        if data is not None:
            for ele in data:
                self.push(ele)

    def push(self, data):
        self.top += 1
        self.data.insert(self.top, data)

    def pop(self):
        self.top -= 1

    def get_top(self):
        return self.data[self.top]

    def __repr__(self) -> str:
        return str(self.data[:self.top + 1])


# %%
if __name__ == "__main__":
    stack = Stack()
    print(stack)
    stack.push(17)
    stack.push(5)
    stack.push(3)
    stack.push(2)
    stack.pop()
    stack.get_top()
    stack.pop()
    stack.push(8)
    stack.push(-1)
    stack.pop()
    stack.get_top()
    print(stack)

# %%

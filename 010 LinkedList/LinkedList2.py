class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return self.data

class LinkedList():
    def __init__(self,nodes= None) -> None:
        self.head = Node
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node

            for ele in nodes:
                node.next = Node(data=ele)  # type: ignore
                node = node.next

    def __repr__(self) -> str:
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)  # type: ignore
            node = node.next  # type: ignore
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next  # type: ignore

    def add_first(self,node):
        node.next = self.head
        self.head = node

if __name__ == "__main__":
    lList = LinkedList(["a","b","c"])
    print(lList)

    for node in lList:
        print(node)

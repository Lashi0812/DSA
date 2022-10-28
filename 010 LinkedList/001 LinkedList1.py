class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
    
    def __repr__(self) -> str:
        return self.data

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

if __name__ == "__main__":
    lList = LinkedList()
    print(lList)

    first_node  = Node("a")
    second_node = Node("b")
    third_node  = Node("c")

    lList.head = first_node  # type: ignore
    print(lList)

    first_node.next = second_node  # type: ignore
    second_node.next = third_node  # type: ignore

    print(lList)
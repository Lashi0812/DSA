from typing import MutableSequence


class Node:
    def __init__(self,data) -> None:
        self.next:Node|None = None
        self.data = data
    def __repr__(self) -> str:
        return str(self.data)
    
class LinkedList:
    def __init__(self,nodes:MutableSequence|Node|None) -> None:
        self.head:Node|None = None
        if isinstance(nodes,Node):
            self.head = nodes
            
        elif nodes is not None and nodes:
            node = Node(nodes.pop(0))
            self.head = node 
            
            for ele in nodes:
                node.next = Node(ele)
                node = node.next
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        
        while node is not None:
            nodes.append(str(node.data))
            node =node.next 
        nodes.append("None")
        
        return " -> ".join(nodes)
    
    def copy(self):
        
        node = self.head
        
        # create the dummy node
        new = Node(-1)
        tail = new
        
        while node is not None:
            tail.next = Node(node.data)
            tail = tail.next
            node = node.next
            
        return LinkedList(new.next)
    
if __name__ == "__main__":
    lList1 = LinkedList([1,2,3,4,5,6])
    print(lList1,id(lList1))
    lList2 = lList1.copy()
    print(lList2,id(lList2))
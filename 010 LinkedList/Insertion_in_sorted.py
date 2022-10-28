from typing import MutableSequence


class Node:
    def __init__(self,data) -> None:
        self.data           = data
        self.next:Node|None = None
    
    def __repr__(self) -> str:
        return self.data

class LinkedList:
    def __init__(self,nodes:MutableSequence|None) -> None:
        self.head:None|Node = None
        
        if nodes is not None and nodes:
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
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def add_first(self,node:Node):
        node.next = self.head
        self.head = node
        
    def add_last(self,node:Node):        
        if self.head is None:
            self.add_first(node)
        else:
            temp = self.head            
            while temp.next is not None:
                temp = temp.next
            temp.next = node
            
    def insert(self,node:Node):
        if self.head is None:
            self.add_first(node)
        elif self.head.data > node.data:
            self.add_first(node)
        else:
            temp = self.head
            #! make the safe jump
            while temp.next is not None and temp.next.data < node.data:
                temp = temp.next
            # First make the connection for the node    
            node.next = temp.next
            # Now add the node 
            temp.next = node

if __name__ == "__main__":
    lList1 =  LinkedList([1,3,5,6,14,18,20])
    print(lList1)
    lList1.insert(Node(9))
    print(lList1)
    lList1.insert(Node(100))
    print(lList1)
    lList1.insert(Node(-1))
    print(lList1)


          
            
            
        
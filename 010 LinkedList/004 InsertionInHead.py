from typing import MutableSequence

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next:Node|None = None
        
    def __repr__(self) -> str:
        return self.data

class LinkedList:
    def __init__(self,nodes:MutableSequence|None = None) -> None:
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
            # Loop until last but before
            while temp.next is not None:
                temp = temp.next
            
            temp.next = node

if __name__ == "__main__":
    lList =  LinkedList([])
    print(lList)
    lList.add_last(Node(5))
    # print(lList)
    lList.add_first(Node(1))
    print(lList)
    lList.add_last(Node(10))
    print(lList)
    
            
        
        
        
        
            
        
        
#%%
from typing import MutableSequence
from typing_extensions import Self


#%%
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next:Node|None = None
    
    def __repr__(self) -> str:
        return str(self.data)

class LinkedList:
    def __init__(self,nodes:None|MutableSequence = None) -> None:
        self.head:Node|None = None
        
        if nodes is not None and nodes:
            node = Node(nodes.pop(0))
            self.head = node
            
            for ele in nodes: 
                # create the connection first                
                node.next = Node(ele)
                # then jump to next node
                node = node.next
                
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def reverse(self) -> Self:
        previous = None
        cur = self.head
        while cur is not None:
            nxt = cur.next
            print(previous,cur,nxt)
            cur.next = previous
            previous = cur
            cur = nxt
        self.head = previous
        return self  
        
        
# %%
if __name__ == "__main__":
    lList1 =  LinkedList([1,3,5,6,14,18,20])
    print(lList1)
    print(lList1.reverse())
    print(lList1)

# %%

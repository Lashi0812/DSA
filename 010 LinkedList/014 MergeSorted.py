#%%
from typing import MutableSequence,Self

# %%
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next:Node|None = None
    
    def __repr__(self) -> str:
        return str(self.data)

class LinkedList:
    def __init__(self,nodes:MutableSequence|Node|None = None) -> None:
        self.head = None
        
        if isinstance(nodes,Node):
            self.head = nodes
        
        elif nodes is not None and nodes and not isinstance(nodes,Node):
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
    
    def merge(self,other:Self) -> Self:
        if self.head is None:
            return other
        if other.head is None:
            return self
        
        h1 = self.head
        h2 = other.head
        
        #? Initially tail is Null so we are handling the initial case
        
        # if h1.data > h2.data:
        #     tail = h2
        #     h3 = h2
        #     h2 = h2.next
        # else:
        #     tail = h1
        #     h3 = h1
        #     h1 = h1.next
        
        #! to handle initial case we will create the dummy Node
        
        h3 = Node(-1)
        tail = h3
            
        while h1 is not None and h2 is not None:
            
            if h1.data > h2.data:
                tail.next = h2
                tail = tail.next
                h2 = h2.next
                
            else:
                tail.next = h1
                tail = tail.next
                h1 = h1.next
                
                
        if h1 is not None:
            tail.next = h1
        elif h2 is not None:
            tail.next = h2

        #! remove the dummy node
        return LinkedList(h3.next)
# %%    
if __name__ == "__main__":
    lList1 = LinkedList([2,6,10,14,19,25])
    lList2 = LinkedList([3,5,9,11,13,18])
    print(lList1)
    print(lList2)
    print(lList1.merge(lList2))
# %%

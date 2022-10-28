"""
    Given the  two LinkedList Merge them into single LinkedList odd node will have the 1st linked list and even node will have the even linked list
"""


#%%
from typing import MutableSequence


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
    
    def merge(self,l1:'LinkedList') -> 'LinkedList':
        if l1.head is None or self.head is None:
            return self
        first   = self.head
        second  = l1.head
        while second is not None and first is not None:
            
            #store the first next address
            nxt = first.next
            
            # store the second next address
            nxt1 = second.next
            
            # Connect the second with first next
            second.next = nxt
            
            # Connect the first with second
            first.next = second
            
            # move the second with second next
            second = nxt1
            
            # move the first with first next
            first = nxt
        
        return self      
        
# %%
if __name__ == "__main__":
    lList1 = LinkedList([1,3,5,7,9])
    lList2 = LinkedList([2,4,6,8])
    print(lList1.merge(lList2))
    print(lList1.merge(LinkedList()))
    print(lList2)
    

# %%

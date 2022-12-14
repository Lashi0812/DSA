#%%
from typing import MutableSequence,Self


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

    def del_head(self) -> Self|None:
        
        if self.head is not None:
            self.head = self.head.next
        return self
    
    def findMiddle(self) -> Node|None:
        if self.head is None: return self.head
        slow = self.head
        fast = self.head
        while (fast.next is not None                   # In case of odd length  
               and fast.next.next is not None):        # In case of even length 
            slow = slow.next                            #type: ignore
            fast = fast.next.next
        return slow
        
    
# %%
if __name__ == "__main__":
    lList =  LinkedList([1,3,5,6,14,18,20])
    print(lList)
    print(lList.findMiddle())
    print(lList.del_head())
    print(lList.findMiddle())
    

# %%

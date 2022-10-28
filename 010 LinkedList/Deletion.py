#%%
from typing import MutableSequence
from typing_extensions import Self


#%%
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next:Node|None = None
    
    def __repr__(self) -> str:
        return self.data

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
        
    def del_tail(self) -> Self|None:
        node = self.head
        if node is None or node.next is None:
            return self.del_head()
        else:                       
            while node.next.next is not None: #type: ignore
                node = node.next #type: ignore
            node.next = None #type: ignore
            return self
        
    def delete(self,ele) -> Self|None:
        node = self.head
        if node is None or node.data == ele:
            return self.del_head()
        else:
            while node.next is not None:
                if node.next.data == ele:
                    node.next = node.next.next
                    return self
                node = node.next
                
                    
                    
        

#%%
if __name__ == "__main__":
    lList =  LinkedList([1,3,5,6,14,18,20])
    print(lList)     
    print(lList.del_tail())
    print(lList.del_head())
    print(lList.delete(6))

# %%

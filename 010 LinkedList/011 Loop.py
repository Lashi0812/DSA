"""
    Given the Linked list find if there loop exists.
"""

# %%
from typing import MutableSequence,Self
# %%
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next :Node|None = None
        
    def __repr__(self) -> str:
        return str(self.data)
    
class LinkedList:
    def __init__(self,nodes:MutableSequence|Node|None) -> None:
        self.head:Node|None = None
        if isinstance(nodes,Node):
            self.head = nodes
                
        elif nodes is not None and nodes and not isinstance(nodes,Node):
            print("enter")
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
    
    def findElement(self,ele)->Node|None:
        if self.head is None: self.head
        node = self.head
        
        while node is not None:
            if node.data == ele:
                return node
            node = node.next            
        return None
            
    
    def isLoopExist(self)->bool:
        if self.head is None : return False
        slow = self.head
        fast = self.head
        while fast.next is not None and fast.next.next is not None and slow.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
# %%
if __name__ == "__main__":
    lList = LinkedList([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
    print(lList.isLoopExist())
    nine = lList.findElement(9)
    thirteen = lList.findElement(13)
    thirteen.next = nine  #type: ignore
    
    print(lList.isLoopExist()) 


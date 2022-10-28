"""
    Given the LinkedList reorder the LinkedList
    
    input : 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 
    output: 1 -> 9 -> 2 -> 8 -> 3 -> 7 -> 4 -> 6 -> 5 
        
"""

# %%
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
        self.head:Node|None = None
        
        if isinstance(nodes,Node):
            self.head = nodes
        
        if nodes is not None and nodes and not isinstance(nodes,Node):
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
    
    def breakAtMiddle(self)-> Self:
        if self.head is None:
            return self
        slow = self.head
        fast = self.head
        
        while fast.next is not None and fast.next.next is not None and slow.next is not None:
            slow = slow.next
            fast = fast.next.next
        second = slow.next 
        slow.next = None
        return LinkedList(second)
    
    def reverse(self)-> Self:
        if self.head is None : return self
        pervious = None 
        cur = self.head
        
        while cur is not None:
            nxt = cur.next
            cur.next = pervious
            pervious = cur
            cur = nxt
        self.head = pervious
        return self
    
    def merge(self,other:Self)->Self:
        if self.head is None:
            return other
        if other.head is None:
            return self
        
        first  = self.head
        second = other.head
        
        while first is not None and second is not None:
            nxt = first.next
            nxt1= second.next
            second.next = nxt
            first.next = second
            second = nxt1
            first = nxt
        return self 
                
# %%

if __name__ == "__main__":
    l1 = LinkedList([1,2,3,4,5,6,7,8])
    l2 = l1.breakAtMiddle()
    print(l1)
    print(l2)
    l2.reverse()
    print(l1.merge(l2))

# %%

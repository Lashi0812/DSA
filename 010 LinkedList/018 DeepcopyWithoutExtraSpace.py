# %%
from typing import MutableSequence, Optional, Union
#%%
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next:Optional[Node]= None
        self.random:Optional[Node]= None
    def __repr__(self) -> str:
        return str(self.data)
    
class LinkedList:
    def __init__(self,nodes:Optional[Union[MutableSequence,Node]]=None) -> None:
        self.head:Optional[Node] = None
        
        if isinstance(nodes,Node):
            self.head = nodes
        
        elif nodes is not None and nodes:
            node = Node(nodes.pop(0))
            self.head = node
            
            for ele in nodes:
                node.next  = Node(ele)
                node = node.next
                
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        
        return " -> ".join(nodes)
    
    def connectRandom(self,index,to):
        node = self.head
        maxi = max(index,to)
        cur = 0
        target = self.head
        
        while node is not None and target is not None and cur<maxi:
            # for forward connection 
            if to >= index:
                if cur < index:
                    node = node.next
                if cur <= to:
                    target = target.next
            # for backward connection
            else:
                if cur <= index:
                    node = node.next
                if cur < to:
                    target = target.next
            cur += 1
                
        if node is not None:
            print(f"making random connection between {node} and {target}")      
            node.random = target
            
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
    
    def deepcopy(self):
        
        """
            Without Extra space
        """
        
        # Shallow copy and merge
        node = self.head
        tail = node
        while tail is not None:
            dummy = Node(tail.data)
            dummy.next = tail.next
            tail.next = dummy
            # jump to next of orig
            tail = tail.next.next
            
        print(LinkedList(node))
        
        
        # make random connection to new node
        cur = node
        while cur is not None and cur.next is not None:
            #making connection
            if cur.random is not None:
                cur.next.random = cur.random.next
            cur = cur.next.next
            
        # break old and new
        old = node 
        new = Node(-1)
        tail = new
            
        while old is not None and old.next is not None:
            tail.next = old.next
            old.next = old.next.next
            tail = tail.next
            old = old.next
            
        return LinkedList(new.next)
#%%    
if __name__ == "__main__":
    lList1 = LinkedList([10,8,4,2,5,9,6,13,11])
    print(lList1)
    connection = [(0,3),(1,7),(2,1),(3,8),(4,6),(5,5),(6,2),(7,4),(8,7)]
    for con in connection:
        lList1.connectRandom(*con)
    print(lList1.deepcopy())

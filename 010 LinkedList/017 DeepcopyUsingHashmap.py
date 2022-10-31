# %%
from typing import MutableSequence, Optional, Union,Self


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
    
    def deepcopy(self)->Self:
        
        """
            Using the hash map to perform the deep copy
        """
        
        # use hashmap to store the address of the its copy
        hashmap = {}
        
        # shallow copy
        node = self.head
        
        # dummy node
        new = Node(-1)
        tail = new
        
        while node is not None:
            itsCopy = Node(node.data)
            hashmap[node] = itsCopy
            tail.next = itsCopy
            tail = tail.next
            node = node.next
        
        # removing dummy node
        new = new.next
        tail= new
        
        # deep copy
        node = self.head
        while node is not None and tail is not None:
            # get the random connection
            rand = node.random
            
            # make random connection to new 
            print(f"making the random connection between {tail} and {hashmap[rand]}")
            tail.random = hashmap[rand]
            
            node = node.next
            tail = tail.next
        
        return LinkedList(new)
#%%    
if __name__ == "__main__":
    lList1 = LinkedList([10,8,4,2,5,9,6,13,11])
    print(lList1)
    connection = [(0,3),(1,7),(2,1),(3,8),(4,6),(5,5),(6,2),(7,4),(8,7)]
    for con in connection:
        lList1.connectRandom(*con)
    print(lList1.deepcopy())

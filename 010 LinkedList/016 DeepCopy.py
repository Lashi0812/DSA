#%%
from typing import MutableSequence

# %%
class Node:
    def __init__(self,data) -> None:
        self.next:Node|None = None
        self.random:Node|None = None 
        self.data = data
    def __repr__(self) -> str:
        return str(self.data)
    
class LinkedList:
    def __init__(self,nodes:MutableSequence|Node|None) -> None:
        self.head:Node|None = None
        if isinstance(nodes,Node):
            self.head = nodes
            
        elif nodes is not None and nodes:
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
            node =node.next 
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
            # print(f"making random connection between {node} and {target}")      
            node.random = target
            
    def deepcopy(self):
        """
            Using Distance method for performing the deepcopy
        """
        
        # first perform the shallow copy 
        copied = self.copy()
        
        
        orig = self.head
        node = copied.head
        new = node
        while node is not None and orig is not None:
            rand = orig.random
            dist = 0
            
            # Find the distance from the start 
            temp = self.head
            while temp is not None:
                if temp == rand:
                    print(f"Found the connection between {orig} and {rand} with distance of {dist} from the start")
                    break
                dist += 1
                temp = temp.next
                
            # make the random connection
            cur = 0
            target = copied.head
            while target is not None and cur<dist:
                target = target.next
                cur +=1
            if target is not None:                
                print(f"making random connection between {node} and {target}")                      
                node.random = target
                
            orig = orig.next
            node = node.next
            
        return LinkedList(new)
                
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
#%%
if __name__ == "__main__":
    lList1 = LinkedList([10,8,4,2,5,9,6,13,11])
    print(lList1)
    connection = [(0,3),(1,7),(2,1),(3,8),(4,6),(5,5),(6,2),(7,4),(8,7)]
    for con in connection:
        lList1.connectRandom(*con)
    print(lList1.deepcopy())
    
# %%

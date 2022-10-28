class Node:
    def __init__(self,data):
        self.data = data
        self.next:Node|None = None
    
    def __repr__(self) -> str:
        return self.data

class LinkedList:
    def __init__(self,nodes = None) -> None:
        self.head:Node|None = None

        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node

            for ele in nodes:
                node.next = Node(data=ele)
                node = node.next

    def __repr__(self) -> str:
        node  = self.head
        nodes = []
        while node is not None:
            nodes.append(node)
            node = node.next
        nodes.append("None")
    
        return " -> ".join(nodes)

    def __iter__(self) : 
        node = self.head
        while node is not None:
            yield node
            node = node.next
            
if __name__ == "__main__":
    lList = LinkedList([1,2,3,4,5,6,7,8,9])
    # get the kth element 
    k = 5
    node = lList.head
    while k>0 and node is not None:
        node = node.next
        k -=1
    if node is not None:
        print(node.data)
    else:
        print(-1)
        
        
            
    

            


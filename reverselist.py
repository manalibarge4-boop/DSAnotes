class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, val):
     new_node = Node(val)
     if self.head == None:
        self.head = new_node
     else:
        curr = self.head
        while curr.next != None:
            curr = curr.next        
        curr.next = new_node

    def traversal(self):
     if self.head == None:
        print("SLL is empty")
     else:
        curr = self.head
        while curr != None:
          print(curr.val, end=" ")
          curr = curr.next   
        print()

        
    
    def reverse_using_stack(self):
     temp = self.head
     stack = []
    
     # Store values in stack
     while temp != None:
        stack.append(temp.val)
        temp = temp.next
    
     # Put values back into nodes
     temp = self.head
    
     while temp != None:
        e = stack.pop()
        temp.val = e
        temp = temp.next
    
    
        # --------------------------------------------------
        # REVERSE USING LINKS - OPTIMAL
        # --------------------------------------------------
    
    def reverse(self):
     temp = self.head
     prev = None
    
     while temp != None:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    
     self.head = prev     

#SLL = SinglyLinkedList()
#SLL.traversal()  o/p SLL is empty

SLL = SinglyLinkedList()

SLL.append(10)
SLL.append(20)
SLL.append(30)
SLL.append(40)
SLL.append(1)

print("Original List:")
SLL.traversal()

print("\nReverse using stack:")
SLL.reverse_using_stack()
SLL.traversal()

print("\nReverse again using links:")
SLL.reverse()
SLL.traversal()
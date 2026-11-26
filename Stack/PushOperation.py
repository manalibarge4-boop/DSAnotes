class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None #self.top represents topmost element
                        #None means stack is currently empty
    def push(self, data):
        new_node = Node(data) #Creates a new node
        new_node.next = self.top #connects Node 30 to the existing TOP (Node 20).
        self.top = new_node  #Updates the top (moves top to node 30)

    def display(self):
        temp = self.top
        while temp is not None:
            print(temp.data)
            temp = temp.next

s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()



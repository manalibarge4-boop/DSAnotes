class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            self.top = self.top.next

    def display(self):
        temp = self.top
        while temp is not None:
            print(temp.data)
            temp = temp.next
s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Stack Element:")
s.display()

s.pop()
print("After POP")
s.display()
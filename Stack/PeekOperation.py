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
    def peek(self):
        if self.top is None:
            print("stack is empty")
        else:
            print(self.top.data)

    def display(self):
        temp = self.top
        while temp is not None:
            print(temp.data)
            temp = temp.next
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

print("Elements in Stack:")
s.display()

s.pop()
print("Elements after POP operation:")
s.display()


print("accessing topmost element:")
s.peek()

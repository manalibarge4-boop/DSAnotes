#Reverse Queue using Stack
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def isempty(self):
        return self.top is None
    def push(self, data):
        new_node = Node(data)

        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            self.top = self.top.next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def reverse(self):
        temp_stack = Stack()

        while self.front is not None:
            temp = self.front
            self.front = self.front.next
            temp_stack.push(temp.data)

        self.rear = None

        while not temp_stack.isempty():
            data = temp_stack.top.data
            temp_stack.pop()
            self.enqueue(data)

    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
             temp = self.front

             while temp is not None:
                 print(temp.data, end= " ")
                 temp = temp.next

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

print("Queue element:")
q.display()

q.reverse()
print("reversed queue:")
q.display()





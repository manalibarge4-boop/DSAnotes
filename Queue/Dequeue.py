class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
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
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp = self.front
            self.front = self.front.next

            if self.front is None:
                self.rear = None
        print("Deleted elements:", temp.data)

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

print("Queue elements: ")
q.display()

print("After dequeue:")
q.dequeue()

print("Updated queue")
q.display()
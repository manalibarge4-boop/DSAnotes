#Queue Implementation using Linked list

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
    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp = self.front

            while temp is not None:
                print(temp.data, end= " ")
                temp = temp.next
#main program
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print("Queue elements:")
q.display()

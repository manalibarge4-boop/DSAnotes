class Node:
  def __init__(self, data, priority):
    self.data = data
    self.priority = priority
    self.next = None
class PriorityQueue:
  def __init__(self):
    self.front = None
  def insert(self, data, priority):
    new_node = Node(data, priority)
    if self.front is None:
      self.front = new_node
    elif priority < self.front.priority:
      new_node.next = self.front
      self.front = new_node
    else:
      temp = self.front
      while temp.next is not None and temp.next.priority <= priority:
        temp = temp.next
      new_node.next = temp.next
      temp.next = new_node
  def delete(self):
    if self.front is None:
      print("priority queue is empty")
    else:
      temp = self.front
      self.front = self.front.next
      print("deleted elements:", temp.data)
  def display(self):
    if self.front is None:
      print("Priority queue is empty")
    else:
      temp = self.front
      while temp is not None:
        print(temp.data, "Priority:", temp.priority)
        temp = temp.next
pq = PriorityQueue()

pq.insert(10, 3)
pq.insert(20, 1)
pq.insert(30, 2)
pq.insert(40, 2)

print("Display the priority queue:")
pq.display()

pq.delete()

print("Display updated priority queue")
pq.display()
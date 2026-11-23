"""
It follows three simple rules:
1. The left child contains a value smaller than the parent node.
2. The right child contains a value greater than the parent node.
3. Each node can have a maximum of two children.
"""
"""
class Node:
    def __init__(self, data): #here __init__ is called constructor, it runs automatically whenever you create an object using the class
                              #self refers to the current object being created or used.
                              #self -> root object, data -> 50
        self.data = data #"Store the value of data inside the current object's data variable.
                         #data = the value received by the constructor.
                         # self.data = the variable belonging to the object.
        self.left = None 
        self.right = None
root = Node(50) #Here, root is the object., We are passing 50 inside the Node class.That 50 is received by the parameter data.
print(root.data) #Python accesses the data stored inside the root object.
print(root.left)
print(root.right)
"""

"""
#50 is the parent (root); 30 and 70 are its children.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
root = Node(50) #Creates the root node containing 50.

root.left = Node(30) #Creates a new node containing 30 and connects it to the left side of root.
root.right = Node(70) #Creates a new node containing 70 and connects it to the right side of root.

print(root.data)
print(root.left.data)
print(root.right.data)
"""

#Write a Python program to create a binary tree with five nodes using a 
# class and constructor. Establish parent-child relationships and display all node values.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(100)
root.left = Node(50)
root.right = Node(150)
root.left.left = Node(25)
root.left.right = Node(75)

print(root.data)
print(root.left.data)
print(root.right.data)
print(root.left.left.data)
print(root.left.right.data)
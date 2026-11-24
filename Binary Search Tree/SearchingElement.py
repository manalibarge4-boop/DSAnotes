#Searching for an element in a binary search tree
#Question: Write a Python program to implement a Binary Search Tree (BST)
#and search for a given element in the BST. Display whether the element is found or not.

#creating a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
#inserting elements into BST
def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root

#Searching an element in BST
def search(root, data):
    if root is None:
        return False
    if data == root.data:
        return True
    elif data < root.data:
        return search(root.left, data)
    else:
        return search(root.right, data)

#Creating the BST
root = None

root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 40)

#Searching an element 
element = 60
result = search(root, element)
if result:
    print(element,"The element is found")
else:
    print(element, "Is not found in BST")


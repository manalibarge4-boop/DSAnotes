class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right= None

def insert(root, data): #We have two parameters:
                        #- root = the current node where we are checking.
                        #- data = the new value we want to insert.
    if root is None: #This means:If the current position is empty, create a new node there.
                     #For example, when inserting 50 into an empty tree, root is initially None.
        return Node(data)
    if data < root.data: #If the new value is smaller than the current node, move towards the left side.
        root.left = insert(root.left, data)
    elif data > root.data: #If the new value is greater than the current node, move towards the right side.
        root.right = insert(root.right, data)
    return root 

root = None #Initially, we haven't inserted anything into our tree.Therefore:No root node exists, The tree is empty, So we assign None to root.
root = insert(root, 50)#insert() calls our insertion function.root passes the current root value (None).50 is the new value we want to insert.
root = insert(root, 30)#This time:- root contains 50.- data contains 30.
                       #Since root.left is currently None, the function creates Node(30) and returns it.
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 40)

print("Root:", root.data)
print("Left child:", root.left.data)
print("Right child:", root.right.data)
print("Left child of 30:", root.left.left.data)
print("Right child of 30:", root.left.right.data)
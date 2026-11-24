class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root
def find_min(root):
    if root is None:
        return None
    while root.left is not None:
        root = root.left
    return root.data
def find_max(root):
    if root is None:
        return None
    while root.right is not None:
        root = root.right
    return root.data

root = None

root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 80)
root = insert(root, 10)

print("The minimum node value is:",find_min(root))

print("The maximum node value is:", find_max(root))

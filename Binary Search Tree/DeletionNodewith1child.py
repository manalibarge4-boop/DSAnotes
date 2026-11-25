#Case 2 – Deletion of a Node with One Child

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert a node into BST
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# Delete a node with one child
def delete(root, data):
    if root is None:
        return None

    if data < root.data:
        root.left = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)

    else:
        # Case 2: Node has only a right child
        if root.left is None:
            return root.right

        # Case 2: Node has only a left child
        elif root.right is None:
            return root.left

    return root


# Inorder traversal
def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


# Main program
root = None

root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 10)

print("BST before deletion:")
inorder(root)

root = delete(root, 20)

print("\nBST after deletion:")
inorder(root)

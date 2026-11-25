# Case 3 – Deletion of a Node with Two Children

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


# Delete a node from BST
def delete(root, data):

    if root is None:
        return None

    if data < root.data:
        root.left = delete(root.left, data)

    elif data > root.data:
        root.right = delete(root.right, data)

    else:

        # Case 1: Node has no children (Leaf Node)
        if root.left is None and root.right is None:
            return None

        # Case 2: Node has only a right child
        elif root.left is None:
            return root.right

        # Case 2: Node has only a left child
        elif root.right is None:
            return root.left

        # Case 3: Node has two children
        else:

            # Find the inorder successor
            successor = root.right

            while successor.left is not None:
                successor = successor.left

            # Replace the node's value
            root.data = successor.data

            # Delete the original successor
            root.right = delete(root.right, successor.data)

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

# Insert nodes into BST
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 60)
root = insert(root, 80)

print("BST before deletion:")
inorder(root)

# Delete node 50 (two children)
root = delete(root, 50)

print("\nBST after deletion:")
inorder(root)

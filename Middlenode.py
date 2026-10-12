class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, val):
        new_node = Node(val)

        if self.head == None:
            self.head = new_node
        else:
            curr = self.head

            while curr.next != None:
                curr = curr.next

            curr.next = new_node

    def traversal(self):
        if self.head == None:
            print("SLL is empty")
        else:
            curr = self.head

            while curr != None:
                print(curr.val, end=" ")
                curr = curr.next

            print()

    # --------------------------------------------------
    # FIND MIDDLE USING COUNT
    # --------------------------------------------------

    def find_middle_count(self):
        n = 0
        temp = self.head

        # Count number of nodes
        while temp != None:
            temp = temp.next
            n = n + 1

        # Move to middle
        temp = self.head

        for i in range(0, n // 2):
            temp = temp.next

        print("Middle Node:", temp.val)


    # --------------------------------------------------
    # FIND MIDDLE USING TORTOISE-HARE
    # --------------------------------------------------

    def find_middle_tortoise(self):
        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        print("Middle Node:", slow.val)


    # --------------------------------------------------
    # REVERSE USING STACK
    # --------------------------------------------------

    def reverse_using_stack(self):
        temp = self.head
        stack = []

        # Store values in stack
        while temp != None:
            stack.append(temp.val)
            temp = temp.next

        # Put values back into nodes
        temp = self.head

        while temp != None:
            e = stack.pop()
            temp.val = e
            temp = temp.next


    # --------------------------------------------------
    # REVERSE USING LINKS - OPTIMAL
    # --------------------------------------------------

    def reverse(self):
        temp = self.head
        prev = None

        while temp != None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        self.head = prev


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------

SLL = SinglyLinkedList()

SLL.append(10)
SLL.append(20)
SLL.append(30)
SLL.append(40)
SLL.append(1)

print("Original List:")
SLL.traversal()


print("\nMiddle using count:")
SLL.find_middle_count()


print("\nMiddle using Tortoise-Hare:")
SLL.find_middle_tortoise()


print("\nReverse using stack:")
SLL.reverse_using_stack()
SLL.traversal()


print("\nReverse again using links:")
SLL.reverse()
SLL.traversal()
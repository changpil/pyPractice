class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:  # If head node is null
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node  # add new node to end of list

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

#######################################################

def helperFunction(myLinkedList, current, previous):  # This function reverses the linked list recursively
    # Base case
    if current.next is None:
        myLinkedList.head = current
        current.next = previous
        return

    next = current.next
    current.next = previous

    # Recursive case
    helperFunction(myLinkedList, next, current)


def reverse(myLinkedList):
    # Check if the head node of the linked list is null or not
    if myLinkedList.head is None:
        return

    # Call the helper function --> main recursive function
    helperFunction(myLinkedList, myLinkedList.head, None)


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.printList()
reverse(ll)
ll.printList()
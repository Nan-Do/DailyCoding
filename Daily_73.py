class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_list(head):
    last = head
    # Get the original last element of the list
    while last.next is not None:
        last = last.next

    # To reverse the list we need three pointers:
    #  One that will mark the end of the new list and will be updated as we "reverse" elements
    #  Another one to the previous element of the original last element.
    #  (This element will be reversed by appending it after the last element of the new list)
    #  Another one to previous one which will be the next one to be "reversed"
    # We repeat this process until the head points to the last element in which case we reverse it outside
    # the loop
    current_last = last
    while head.next != last:
        current = head
        ant = head
        while current.next != last:
            ant = current
            current = current.next
        ant.next = last
        current_last.next = current
        current_last = current

    head.next = None
    current_last.next = head

    return last


def print_list(head):
    while head is not None:
        print(head.value, end=" ")
        head = head.next
    print()


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print_list(head)
head = reverse_list(head)
print_list(head)

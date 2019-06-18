class DoublyLinkedList:
    def __init__(self, value):
        self.value = value
        self.next = self.prev = None


def updateList(values):
    root = DoublyLinkedList(values[0])

    current = root
    for v in values[1:]:
        n = DoublyLinkedList(v)
        current.next = n
        n.prev = current
        current = n

    return root


# Cost O(n): We check each element twice
# Keep two pointers one at the begginig of the list and another at the end.
# Check if the values match and update the pointers.
# Repeat this process length / 2 times
def isPalindrome(root):
    length = 1
    last = root

    while last.next is not None:
        length += 1
        last = last.next

    init = root
    for _ in range(int(length / 2)):
        if init.value != last.value:
            return False

        init = init.next
        last = last.prev

    return True


root = updateList([1, 2, 3, 3, 1])
print(isPalindrome(root))
current = root
while current is not None:
    print(current.value)
    current = current.next

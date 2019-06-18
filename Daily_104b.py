class SinglyLinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def updateList(values):
    root = SinglyLinkedList(values[0])

    current = root
    for v in values[1:]:
        n = SinglyLinkedList(v)
        current.next = n
        current = n

    return root


# O(n^2):
# Compute the length and keep a pointer and a counter with the number of hops
# that we need from than pointer to the pointer we need to check if is a palindrome
# For the first time this value is lenght - 1 and then at each iteration we subtract
# 2, we repeat this process length / 2 times
def isPalindrome(root):
    length = 0
    last = root

    while last is not None:
        length += 1
        last = last.next

    init = root
    num_hops = length - 1
    for x in range(int(length / 2)):
        last = init
        for _ in range(num_hops):
            last = last.next

        if init.value != last.value:
            return False

        init = init.next
        num_hops -= 2

    return True


root = updateList([1, 2, 3, 4, 2, 1])
print(isPalindrome(root))
current = root
while current is not None:
    print(current.value)
    current = current.next

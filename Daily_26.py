class Node:
    def __init__(self, x):
        self.value = x
        self.next = None

class List:
    def __init__(self):
        self.root = None

    def add(self, x):
        if self.root is None:
            self.root = Node(x)
            return

        temp = self.root

        while temp.next != None:
            temp = temp.next

        temp.next = Node(x)

    def kth_last(self, k):
        fast = slow = self.root

        while k > 0:
            fast = fast.next
            k -= 1
            
        while fast != None:
            slow = slow.next
            fast = fast.next

        return slow.value


l = List()

for x in xrange(1, 11):
    l.add(x)

print l.kth_last(3)

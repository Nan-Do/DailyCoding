class Node:
    def __init__(self, value):
        self.value = value
        self.next = self.prev = None

class Queue:
    def __init__(self, k):
        self.head = self.tail = None
        self.current = 0
        self.size = k

    def add(self, v):
        if self.current == self.size:
            self.tail = self.tail.prev
            self.current -=1

        t = Node(v)
        if self.head is None:
            self.tail = self.head = t
        else:
            self.head.prev = t
            t.next = self.head
            self.head = t
        self.current += 1
        return t

    def move_to_head(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        if node is self.tail:
            self.tail = self.tail.prev

        node.next = self.head
        node.prev = None

        self.head = node

    def is_full(self):
        return (self.current == self.size)

class LRU:
    def __init__(self, size):
        self.size = size
        self.q = Queue(size)
        self.hash = dict()
        self.rev_hash = dict()

    def get(self, key):
        if key not in self.hash:
            return None

        n = self.hash[key]        
        self.q.move_to_head(n)

        return n.value
    
    def add(self, key, value):
        print "Adding key:", key, "value:", value

        if self.q.is_full():
            key = self.rev_hash[self.q.tail]
            print "Removing LRU key", key
            del self.hash[key]
            del self.rev_hash[self.q.tail]

        t = self.q.add(value)
        self.hash[key] = t
        self.rev_hash[t] = key


l = LRU(3)
print l.get(3)
print l.add(1, "one")
print l.add(2, "two")
print l.add(3, "three")
print l.get(1)
print l.add(4, "four")
print l.get(1)

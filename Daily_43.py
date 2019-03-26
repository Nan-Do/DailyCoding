import heapq

class max_heap:
    def __init__(self):
        self.h = []
        self.max_values = []

    def push(self, val):
        heapq.heappush(self.h, -val)
        new_max = val
        if len(self.max_values):
            new_max = max(self.max_values[-1], val)
        self.max_values.append(new_max)

    def pop(self):
        if len(self.h) == 0:
            return None

        self.max_values.pop()
        return -heapq.heappop(self.h)

    def max(self):
        return self.max_values[-1]


a = max_heap()

a.push(10)
a.push(3)
a.push(8)
a.push(2)
a.push(1)
a.push(11)

print a.max()
print a.pop()
print a.max()

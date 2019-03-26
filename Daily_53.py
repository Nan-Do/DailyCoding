class TSQ:
    def __init__(self):
        self.input = []
        self.output = []

    def enqueue(self, value):
        self.input.append(value)

    def dequeue(self):
        if len(self.output) == 0:
            while len(self.input):
                self.output.append(self.input.pop())

        if len(self.output) == 0:
            return None

        return self.output.pop()


a = TSQ()

a.enqueue(1)
a.enqueue(2)
a.enqueue(3)

print(a.dequeue())
print(a.dequeue())
print(a.dequeue())
print(a.dequeue())

import heapq


class LFU:
    def __init__(self, n):
        self.n = n

        self.vector = []
        self.hash = {}

    def get(self, key):
        if key in self.hash:
            node = self.hash[key]
            node[0] += 1
            heapq.heapify(self.vector)
            return node[2]
        return None

    def set(self, key, value):
        if key in self.hash:
            node = self.hash[key]
            node[0] += 1
            node[2] = value
            heapq.heapify(self.vector)
        else:
            print("Adding", key, len(self.vector))
            node = [1, key, value]
            self.hash[key] = node
            if len(self.vector) == self.n:
                remove_node = heapq.heapreplace(self.vector, node)
                print("Removing", remove_node[1])
                del self.hash[remove_node[1]]
            else:
                heapq.heappush(self.vector, node)


l = LFU(3)

l.set('A', 1)
l.set('B', 1)
l.set('C', 1)
l.get('B')
l.get('B')
l.get('C')
l.get('C')
l.get('A')

l.set('D', 1)

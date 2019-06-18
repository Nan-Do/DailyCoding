import heapq
from operator import itemgetter


# Basic solution: HashTable with a list of (timestamp, values) pairs sorted
# decreasingly.
# The algorithim works as follows:
# To add a value with a time we check if the time is present on the list
# for the given key, if this is the case we update the value, if not, we
# add the new pair to the list on its rightful position to keep it sorted.
# Cost O(n)
# To get a value we traverse the list and return the first value in which
# the stored time is value is less or equal than the querying time.
# Cost O(n)
class TimedHash_array:
    def __init__(self):
        self.d = dict()

    def __find_time(self, array, time):
        lo = 0
        hi = len(array) - 1

        while lo <= hi:
            mid = int((lo + hi) / 2)

            if array[mid][0] == time:
                return mid
            if time > array[mid][0]:
                hi = mid - 1
            else:
                lo = mid + 1

        return -1

    def set(self, key, value, time):
        if key not in self.d:
            self.d[key] = []

        s = self.d[key]
        v = self.__find_time(s, time)
        if v != -1:
            s[v] = (time, value)
        else:
            s.append((time, value))
            s.sort(key=itemgetter(0), reverse=True)

    def get(self, key, time):
        if key not in self.d:
            return None

        for stored_time, value in self.d[key]:
            if time >= stored_time:
                return value

        return None


# Alternative implementation using a DoubleLinkedList
class DoubleLinkedList:
    def __init__(self, value, time):
        self.data = (time, value)
        self.next = self.prev = None


class TimedHash:
    def __init__(self):
        self.d = dict()

    def set(self, key, value, time):
        if key not in self.d:
            self.d[key] = DoubleLinkedList(value, time)
            return

        temp = self.d[key]
        if time > temp.data[0]:
            new_node = DoubleLinkedList(value, time)
            temp.prev = new_node
            new_node.next = temp
            self.d[key] = new_node
            return

        while temp is not None:
            stored_time, _ = temp.data
            if stored_time == time:
                temp.data = (time, value)
                break
            elif time > stored_time:
                new_node = DoubleLinkedList(value, time)
                new_node.prev = temp.prev
                new_node.next = temp
                temp.prev = new_node
                break
            if temp.next is None:
                new_node = DoubleLinkedList(value, time)
                temp.next = new_node
                new_node.prev = temp
                break

            temp = temp.next

    def get(self, key, time):
        if key not in self.d:
            return None

        temp = self.d[key]
        while temp is not None:
            temp = temp.next
        temp = self.d[key]
        while temp is not None:
            stored_time, value = temp.data
            if time >= stored_time:
                return value
            temp = temp.next

        return None


d = TimedHash()
d.set(1, 1, 0)
d.set(1, 2, 2)
d.set(1, 5, 5)
print(d.get(1, 1))
print(d.get(1, 3))

d = TimedHash()
d.set(1, 1, 5)
print(d.get(1, 0))
print(d.get(1, 10))

d.set(1, 1, 0)
d.set(1, 2, 0)
print(d.get(1, 0))

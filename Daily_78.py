import heapq


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Cost n * k. At each point we iterate through each head of the list
# keeping track of the minimum value, then we add that value to the
# returning list.
def _merge_k_lists(lists):
    last = None
    head = None

    all_lists_ended = False
    while not all_lists_ended:
        all_lists_ended = True
        k = 0
        min_val = float('inf')

        for x in range(len(lists)):
            if lists[x] is not None:
                all_lists_ended = False
            if lists[x] is not None and\
               lists[x].value < min_val:
                k = x
                min_val = lists[x].value

        if all_lists_ended:
            break

        c = Node(lists[k].value)
        lists[k] = lists[k].next
        if head is None:
            head = last = c
        else:
            last.next = c
            last = c

    return head


# Cost n log n (n is the sum of the length of each list).
# Put the value of each list into a heap
def merge_k_lists(lists):
    heap = []

    for x in range(len(lists)):
        head = lists[x]
        while head is not None:
            value = head.value
            heapq.heappush(heap, value)
            head = head.next

    head = last = None
    while len(heap):
        v = heapq.heappop(heap)
        if head is None:
            head = last = Node(v)
        else:
            last.next = Node(v)
            last = last.next

    return head


def print_list(h):
    while h is not None:
        print(h.value, end=" ")
        h = h.next
    print()


h1 = Node(1)
h1.next = Node(3)
h1.next.next = Node(5)
print_list(h1)

h2 = Node(2)
h2.next = Node(4)
h2.next.next = Node(5)
print_list(h2)

h3 = Node(2)
h3.next = Node(7)
print_list(h3)

h = merge_k_lists([h1, h2, h3])
print_list(h)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None


def compute_sum(a, b):
    if a == b:
        return b.value
    if a is None:
        return float('-inf')

    l1 = compute_sum(a.left, b)
    l2 = compute_sum(a.right, b)

    return max(l1, l2) + a.value


# Cost O(n) at worst we visit each node 3 times
# Solution:
# To compute a path that not necesarily traverses the root we have
# three options: a is descendant of b, b is descendant of a or the
# path goes trough the root. To solve the problem we just simply
# compute each possibility and return the appropriate one.
# The auxiliary function compute_sum returns -inf if there is not
# a path between the specified nodes.
# The solution will be the maximum value.
def compute_max_path(root, a, b):
    if root is None:
        return 0

    l2 = compute_sum(a, b)
    l3 = compute_sum(b, a)

    # This has to be computed after checking that there is not a
    # path between a and b otherwise we will compute the wrong
    # answer as the root always reaches.
    # We subtract the root.value as is included in both
    # calls to compute_sum
    if l2 == float('-inf') and l3 == float('-inf'):
        return compute_sum(root, a) + compute_sum(root, b) - root.value
    return max(l2, l3)


root = Node(3)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(1)
root.left.right.left = Node(8)
root.right.left = Node(9)
root.right.right = Node(7)

a = root.left
b = root.left.right.left
print(compute_max_path(root, a, b))

b = root.right.left
print(compute_max_path(root, a, b))

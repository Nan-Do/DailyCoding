class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None


# To find if t is a subtree of s we have the next cases:
# t is empty: True an empty tree is a subtree of any tree
# t is not empty but s is: False an empty tree can't have subtrees (other
# than the empty subtree which was tested on the previous condition)
# if s == t we have to check that the subtrees are equal
# we always have to check the posibility that a descendant of s
# is equal to t
def find_subtree(s, t):
    if t is None:
        return True

    if s is None:
        return False

    if s.value == t.value:
        return (find_subtree(s.left, t.left)
                and find_subtree(s.right, t.right)) or find_subtree(
                    s.left, t) or find_subtree(s.right, t)
    else:
        return find_subtree(s.left, t) or \
                find_subtree(s.right, t)


# s
#        1
#     2     3
#   4   5 6   7
# 8   9
s = Node(1)
s.left = Node(2)
s.right = Node(3)
s.left.left = Node(4)
s.left.right = Node(5)
s.right.left = Node(6)
s.right.right = Node(7)
s.left.left.left = Node(8)
s.left.left.right = Node(9)

# t
t = Node(10)
t.left = Node(5)
t.right = Node(6)
print(find_subtree(s, t))

# t
t = Node(3)
t.left = Node(6)
t.right = Node(7)
print(find_subtree(s, t))

# t
t = Node(4)
t.right = Node(9)
print(find_subtree(s, t))

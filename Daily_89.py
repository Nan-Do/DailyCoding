class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None


# Cost: O(n) Each node is visited once or 2^(log(n))
# This function solves the problem as it is proposed, that is,
# it satisfies the constraint that the key in the left child must
# be less than or equal to the root and the key in the right child
# must be greater than or equal to the root.
# This would make a tree like the next valid...
#     5
#  3    8
# 1  4 2
def isValidBST(root):
    if root is None:
        return True

    if root.left and root.right:
        if not root.left.value <= root.value <= root.right.value:
            return False
    elif root.left:
        if not root.left.value <= root.value:
            return False
    elif root.right:
        if not root.value <= root.right.value:
            return False

    return isValidBST(root.left) and isValidBST(root.right)


# Cost: O(n) Each node is visited once or 2^(log(n))
# This function solves the probem of the previous function by keeping
# a maximum value and a minimum value that the current node can take
# The root can take any value, then the inmidiate left node can take
# any value between ]-inf, root.value], likewise the inmidiate right
# node can take a value from [root.value, inf[.
def isValidBST2(root, min_val, max_val):
    if root is None:
        return True
    if not min_val <= root.value <= max_val:
        return False

    return isValidBST2(root.left, min_val, root.value) and\
            isValidBST2(root.right, root.value, max_val)


min_inf = float('-inf')
max_inf = float('inf')

a = Node(5)
a.left = Node(3)
a.left.left = Node(1)
a.left.right = Node(4)
print(isValidBST2(a, min_inf, max_inf))
a.right = Node(1)
print(isValidBST2(a, min_inf, max_inf))
a.right = Node(8)
a.right.left = Node(2)
print(isValidBST2(a, min_inf, max_inf))

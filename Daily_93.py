class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None


# Auxiliary function to compute the height of a Tree
def max_height(root):
    if root is None:
        return 0
    return max(max_height(root.left), max_height(root.right)) + 1


# Auxiliary function to compute if a Tree is a BST
# Implemented iteratively, Daily_89 contains more implementations
def is_bst(root):
    stack = []
    current = root
    last = None

    while len(stack) or current:
        while current is not None:
            stack.append(current)
            current = current.left

        temp = stack.pop()
        if last is not None:
            if temp.value < last:
                return False
        last = temp.value

        current = temp.right

    return True


# Cost n^2 for each node we visit all the others (triangle numbers)
# Solution:
# To solve the problem we need two Auxiliary functions, one to check
# if the subtree is a valid binary search tree and another one to
# compute the height of the subtrees.
# The algorithm works as follows, if the root is a valid BST that is
# the biggest subtree that we can possibly have so we just return
# it, if not we check if either of the children are valid BSTs in
# case both are return the tallest one if none of the children are
# valid BSTs return None
def max_bst(root):
    if is_bst(root):
        return root

    a = max_bst(root.left)
    b = max_bst(root.right)

    if a is not None and b is not None:
        a_h = max_height(a)
        b_h = max_height(b)
        return a if a_h >= b_h else b
    elif a is not None:
        return root.left
    elif b is not None:
        return root.right
    else:
        return None


root = Node(8)
root.left = Node(32)
root.right = Node(1)
root.right.left = Node(3)
root.right.left.left = Node(2)
root.right.right = Node(7)
root.right.right.left = Node(5)

print(max_bst(root).value)

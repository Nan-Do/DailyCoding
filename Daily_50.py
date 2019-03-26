class Node:
    def __init__(self, v):
        self.value = v
        self.left = self.right = None

def compute_tree(root):
    if root is None:
        return None

    a = compute_tree(root.left)
    b = compute_tree(root.right)

    if a is None and b is None:
        return root.value

    if root.value == '+':
        return a + b
    if root.value == '-':
        return a - b
    if root.value == '*':
        return a * b
    if root.value == '/':
        return a / b

    return None


r = Node('*')
r.left = Node('+')
r.right = Node('+')

r.left.left = Node(3)
r.left.right = Node(2)

r.right.left = Node(4)
r.right.right = Node(5)

print compute_tree(r)

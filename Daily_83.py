class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None


# Cost linear
# Traverse the tree in indorder and swicth the links to the children in a bottom up fashion
def invert_tree(node):
    if node is None:
        return

    invert_tree(node.left)
    invert_tree(node.right)

    node.left, node.right = node.right, node.left


# Print the tree in inorder
def print_tree(node):
    if node is None:
        return

    print_tree(node.left)
    print_tree(node.right)

    print(node.value, end=' ')


root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.left = Node('f')

print_tree(root)
print()
invert_tree(root)
print_tree(root)
print()

class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None


# Cost Exponential in a complete and balanced binary tree the worse case
# there are 2 ^ (n-1)
# Solution:
# The function return a list of lists, at each step we will update the
# current solution wiht the solutions coming from the children, we
# update the solution by adding the root value in the front of all
# the paths coming from its children
def compute_paths_tree(root):
    res = [[root]]

    a = []
    if root.left:
        a = compute_paths_tree(root.left)

    b = []
    if root.left:
        b = compute_paths_tree(root.right)

    if a:
        res.extend(list(map(lambda x: [root.value] + x, a)))
    if b:
        res.extend(list(map(lambda x: [root.value] + x, b)))

    return res


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

print(compute_paths_tree(root))

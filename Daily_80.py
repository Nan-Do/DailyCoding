class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None


# Cost O(n) -> log(2^n) calls
# Algorithm:
# Pass the root along the computed height to each node.
# Check the children, if it is a leaf (both none) return the current node and height
# If the node is not a leaf check which children has higher height and return it.
def _get_deepest_node(root, c):
    if root is None:
        return None, c

    n1 = n2 = None
    l1 = l2 = 0
    if root.left is not None:
        n1, l1 = _get_deepest_node(root.left, c + 1)
    if root.right is not None:
        n2, l2 = _get_deepest_node(root.right, c + 1)

    if n1 is None and n2 is None:
        return root.value, c
    else:
        if l1 > l2:
            return n1, l1
        else:
            return n2, l2


def get_deepest_node(root):
    n, _ = _get_deepest_node(root, 0)
    return n


root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
print(_get_deepest_node(root, 0))

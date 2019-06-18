class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = self.parent = None


def get_path_to_the_root(n):
    res = []

    temp = n
    while temp is not None:
        res.append(temp.value)
        temp = temp.parent

    return res


# Cost: Log(n) * Log(n)
# Solution obtain the path from each node to the root
# and return the first value that appears on both lists
# Computing each path takes log(n) and each least contains
# log(n) elements so to compare both lists to return the
# first element repeated in both is log(n) * log(n)
def find_LCA(n1, n2):
    l1 = get_path_to_the_root(n1)
    l2 = get_path_to_the_root(n2)

    for x in l1:
        for y in l2:
            if x == y:
                return x

    return -1


root = Node(1)
root.left = Node(2)
root.left.parent = root
root.right = Node(3)
root.right.parent = root

root.left.left = Node(4)
root.left.left.parent = root.left
root.left.right = Node(5)
root.left.right.parent = root.left
root.left.left.left = Node(8)
root.left.left.left.parent = root.left.left
root.left.left.right = Node(8)
root.left.left.right.parent = root.left.left

root.right.left = Node(6)
root.right.left.parent = root.right
root.right.right = Node(7)
root.right.right.parent = root.right

a = root.left.left.right  # 8
b = root.right.right  # 7
print(find_LCA(a, b))

a = root.left.left  # 4
b = root.left.right  # 5
print(find_LCA(a, b))

a = root.left.left  # 4
b = root.left.left  # 5
print(find_LCA(a, b))

print(find_LCA(None, b))

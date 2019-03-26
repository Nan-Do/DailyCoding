class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

def find_second_biggest(root):
    father = root
    temp = root

    while temp.right is not None:
        father = temp
        temp = temp.right

    if father.left is None:
        return father.value
    else:
        temp = father.left
        while temp.right is not None:
            temp = temp.right
        return temp.value


root = Node(2)
root.left = Node(1)
root.right = Node(7)
root.right.left = Node(4)
root.right.right = Node(9)
root.right.right.left = Node(10)
root.right.right.right = Node(12)
root.right.right.left.right = Node(11)

print find_second_biggest(root)

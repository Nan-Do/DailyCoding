class BTree:
    def __init__(self, v):
        self.value = v
        self.left = self.right = None


# Cost O(n)
# Use a queue (or a stack depending on how you want to print the values by level)
# We need two queues, one to hold the nodes from the current level and another one
# to hold tne nodes for the next level.
# The algorithim is simple extract the nodes from the current queue, print its values
# and insert the children on the queue for the next level, once the current queue is
# empty switch the current queue with the next until both are empty.
def print_level(root):
    if root is None:
        return

    current = [root]
    next_level = []

    # This is an uncommon pattern we need two while loops
    # The first one is just used to check that both queues are not empty
    while len(current):
        while len(current):
            node = current.pop(0)

            print(node.value)

            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        current = next_level
        next_level = []


root = BTree(1)
root.left = BTree(2)
root.right = BTree(3)
root.left.left = BTree(4)
root.left.right = BTree(5)
root.right.right = BTree(6)

print_level(root)

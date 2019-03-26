class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print node.value
    inorder(node.right)


def in_pre_to_tree(inorder, preorder):
    if len(preorder) == 0 or len(inorder) != len(preorder):
        return None

    node = Node(preorder[0])
    if len(preorder) == 1:
        return node

    inorder_pivot = inorder.index(preorder[0])
    preorder_pivot = preorder.index(inorder[inorder_pivot-1])

    node.left = in_pre_to_tree(inorder[:inorder_pivot], 
                               preorder[1:preorder_pivot+1])

    node.right = in_pre_to_tree(inorder[inorder_pivot+1:], 
                                preorder[preorder_pivot+1:])

    return node


a = in_pre_to_tree(['d','b','e','a','f','c','g'], ['a','b','d','e','c','f','g'])
inorder(a)

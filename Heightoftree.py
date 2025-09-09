class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def Height(root):
    if root is None:
        return -1  
    left_height = Height(root.left)
    right_height = Height(root.right)
    return max(left_height, right_height) + 1
root = Node(11)
root.left = Node(32)
root.right = Node(23)
root.left.left = Node(41)
root.right.left = Node(58)
root.right.right = Node(27)
root.left.left.left = Node(39)
print("Height of the binary tree is:", Height(root))
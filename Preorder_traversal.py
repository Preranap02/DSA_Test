class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)
root = Node(6)
root.left = Node(12)
root.right = Node(24)
root.left.left = Node(18)
root.left.right = Node(3)
print("Preorder Traversal:")
preorder(root)
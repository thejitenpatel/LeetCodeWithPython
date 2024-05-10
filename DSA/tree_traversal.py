class Node:
    def __init__(self, item) -> None:
        self.left = None
        self.right = None
        self.data = item


def inorder(root):
    if root:
        inorder(root=root.left)
        print(str(root.data) + "->", end="")
        inorder(root=root.right)

def postorder(root):
    if root:
        postorder(root=root.left)
        postorder(root=root.right)
        print(str(root.data) + "->", end="")

def preorder(root):
    if root:
        print(str(root.data) + "->", end="")
        preorder(root=root.left)
        preorder(root=root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal ")
inorder(root)

print("\nPreorder traversal ")
preorder(root)

print("\nPostorder traversal ")
postorder(root)

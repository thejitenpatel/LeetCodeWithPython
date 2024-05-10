class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.data = key

    def traverse_preorder(self):
        print(self.data, end=' ')
        if self.left:
            self.left.traverse_preorder()
        if self.right:
            self.right.traverse_preorder()

    def traverse_inorder(self):
        if self.left:
            self.left.traverse_inorder()
        print(self.data, end=' ')
        if self.right:
            self.right.traverse_inorder()

    def traverse_postorder(self):
        if self.left:
            self.left.traverse_postorder()
        if self.right:
            self.right.traverse_postorder()
        print(self.data, end=' ')


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)

print("Pre order Traversal: ", end="")
root.traverse_preorder()
print("\nIn order Traversal: ", end="")
root.traverse_inorder()
print("\nPost order Traversal: ", end="")
root.traverse_postorder()

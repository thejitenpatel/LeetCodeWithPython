class TreeNode:
    def __init__(self, key=0, left=None, right=None) -> None:
        self.key = key
        self.left = left
        self.right = right


class BST:

    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(key=value)
        else:
            self._insert(self.root, value)

    def _insert(self, root, value):
        if value < root.key:
            if root.left is None:
                root.left = TreeNode(key=value)
            else:
                self._insert(root=root.left, value=value)
        else:
            if root.right is None:
                root.right = TreeNode(key=value)
            else:
                self._insert(root=root.right, value=value)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root=root.left, key=key)
        else:
            return self._search(root=root.right, key=key)


bst = BST()
# Insert elements
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

# Search for an element
print(bst.search(40))  # Output: Node object with val 40
print(bst.search(90))  # Output: None

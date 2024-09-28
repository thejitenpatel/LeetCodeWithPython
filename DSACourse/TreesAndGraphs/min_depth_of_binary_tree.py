# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if root.left is None:
            return 1 + self.minDepth(root.right)

        elif root.right is None:
            return 1 + self.minDepth(root.left)

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        return min(left, right) + 1

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, min_val, max_val):
            if not node:
                return max_val - min_val

            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)

            left = dfs(node.left, min_val, max_val)
            right = dfs(node.right, min_val, max_val)
            return max(left, right)

        return dfs(root, root.val, root.val)

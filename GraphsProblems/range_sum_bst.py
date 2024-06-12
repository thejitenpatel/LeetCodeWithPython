# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            if node.val < low:
                # If current node's value is less than low, go to the right subtree
                return dfs(node.right)
            elif node.val > high:
                # If current node's value is greater than high, go to the left subtree
                return dfs(node.left)
            else:
                # Current node's value is within the range, sum its value and continue to both subtrees
                return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)

    # def dfs(self, node: Optional[TreeNode], low: int, high: int):
    #     if not node:
    #         return 0

    #     if node.val < low:
    #         return self.dfs(node=node.right)
    #     elif node.val > high:
    #         return self.dfs(node=node.left)
    #     else:
    #         return node.val + self.dfs(node=node.left) + self.dfs(node=node.right)


sol = Solution()
sol.rangeSumBST(root=[10, 5, 15, 3, 7, None, 18], low=7, high=15)

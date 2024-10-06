# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder_list = []

        def dfs(node):
            if not node:
                return []

            dfs(node.left)
            inorder_list.append(node.val)
            dfs(node.right)
        dfs(root)
        return inorder_list
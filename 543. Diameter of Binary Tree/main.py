from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def fn(node):
            nonlocal result
            if not node:
                return 0
            m1 = 1 + fn(node.left)
            m2 = 1 + fn(node.right)
            result = max(result, m1 + m2 - 2)

            return max(m1, m2)

        fn(root)
        return result

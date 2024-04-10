from typing import Optional
import sys
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        result = sys.maxsize
        max_height = -1

        def fn(node, height):
            nonlocal result, max_height
            if not node:
                return
            if not node.left and not node.right:
                if height > max_height:
                    result = node.val
                    max_height = height

            fn(node.left, height + 1)
            fn(node.right, height + 1)

        fn(root, 0)
        if result == sys.maxsize:
            return root.val
        return result

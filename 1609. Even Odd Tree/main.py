from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        isValid = True
        m = {}

        def fn(node, height):
            nonlocal isValid
            if not isValid:
                return
            if not node:
                return
            if not m.get(height):
                if (height % 2 == 0 and node.val % 2 == 0) or (height % 2 == 1 and node.val % 2 == 1):
                    isValid = False
                    return
            else:
                if height % 2 == 1:
                    if node.val >= m[height] or node.val % 2 == 1:
                        isValid = False
                        return
                else:
                    if node.val <= m[height] or node.val % 2 == 0:
                        isValid = False
                        return
            m[height] = node.val
            fn(node.left, height + 1)
            fn(node.right, height + 1)
        fn(root, 0)
        return isValid

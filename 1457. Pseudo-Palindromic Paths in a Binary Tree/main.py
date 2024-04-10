from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        result = 0

        def traversal(node, c: defaultdict):
            nonlocal result
            if not node:
                return
            c[node.val] += 1
            if not node.left and not node.right:
                odds = 0
                for v in c.values():
                    if v % 2 == 1:
                        odds += 1
                if odds == 1 or odds == 0:
                    result += 1
            else:
                traversal(node.left, c.copy())
                traversal(node.right, c.copy())
        traversal(root, defaultdict(int))
        return result

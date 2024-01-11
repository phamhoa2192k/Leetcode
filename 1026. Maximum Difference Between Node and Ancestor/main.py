# Definition for a binary tree node.
from typing import Optional
import sys
from functools import cache
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        result = -1

        @cache
        def traversal(node):
            nonlocal result
            if not node:
                return (1, sys.maxsize)
            ma = max(node.val, traversal(node.left)
                     [0], traversal(node.right)[0])
            mi = min(node.val, traversal(node.left)
                     [1], traversal(node.right)[1])

            result = max(result, abs(node.val - mi), abs(node.val - ma))
            return (ma, mi)

        traversal(root)
        return result

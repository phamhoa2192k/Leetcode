# Definition for a binary tree node.
from typing import Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def traversal(n):
            nonlocal result
            curr_node = (0, 0)
            if n:
                left = traversal(n.left)
                right = traversal(n.right)
                curr_node = (left[0] + right[0] + n.val,
                             left[1] + right[1] + 1)
                if math.floor(curr_node[0] / curr_node[1]) == n.val:
                    result += 1
            return curr_node

        traversal(root)
        return result

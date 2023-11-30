# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = {}
        if not root.left and not root.right:
            return [root.val]
        def traversal(n):
            if not n:
                return
            else:
                counter[n.val] = 1 if not counter.get(n.val) else counter[n.val] + 1
            traversal(n.left)
            traversal(n.right)

        traversal(root)
        max_key, result = max(counter, key = counter.get), []
        for key, value in counter.items():
            if value == counter[max_key]:
                result.append(key)
        return result

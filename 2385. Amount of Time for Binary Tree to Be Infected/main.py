from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        start_node = None
        check = defaultdict(bool)

        def traversal(node, parent=None):
            nonlocal start_node
            if not node:
                return
            node.parent = parent
            if node.val == start:
                start_node = node
            traversal(node.left, node)
            traversal(node.right, node)

        traversal(root)

        def find_deep(node):
            if not node or check[node.val]:
                return -1
            check[node.val] = True
            return max(find_deep(node.left) + 1, find_deep(node.right) + 1, find_deep(node.parent) + 1)

        return find_deep(start_node)


root = TreeNode(1, left=TreeNode(5, right=TreeNode(4, left=TreeNode(
    9), right=TreeNode(2))), right=TreeNode(3, left=TreeNode(10), right=TreeNode(6)))

print(Solution().amountOfTime(root, 3))
# root = TreeNode(5, left=TreeNode(2, left=TreeNode(
#     4, left=TreeNode(1))), right=TreeNode(3))

# root = TreeNode(4, left=TreeNode(3, left=TreeNode(5)),
#                 right=TreeNode(1, right=TreeNode(2)))

# print(Solution().amountOfTime(root, 3))

`# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        s = 0

        def traversal(node, isLeft = False):
            nonlocal s
            if not node:
                return
            if not node.left and not node.right:
                if isLeft:
                    s += node.val
                else:
                    return
            traversal(node.left, True)
            traversal(node.right, False)
        traversal(root)
        return s`
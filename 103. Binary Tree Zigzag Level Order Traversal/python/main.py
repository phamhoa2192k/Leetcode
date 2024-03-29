# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def travelsal(node, d):
            if not node:
                return
            nonlocal result
            if len(result) <= d:
                result.append([])
            if d % 2 == 1:
                result[d].insert(0, node.val)     
            else:
                result[d].append(node.val)
            travelsal(node.left, d + 1)
            travelsal(node.right, d + 1)

        travelsal(root, 0)

        return result


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        result = TreeNode(root.val)
        def travelsal(node1, node2, isleft):
            if not node1:
                return
            if isleft:
                node2.right = TreeNode(node1.val)
                node2 = node2.right
            else:
                node2.left = TreeNode(node1.val)
                node2 = node2.left
            travelsal(node1.left, node2, True)
            travelsal(node1.right, node2, False)
        travelsal(root.left, result, True)
        travelsal(root.right, result, False)
        return result


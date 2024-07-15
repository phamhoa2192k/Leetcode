from typing import List, Optional
from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        m = {}
        c = {}
        check = {}
        for des in descriptions:
            if not m.get(des[0]):
                m[des[0]] = [-1, -1]
            if des[2] == 0:
                m[des[0]][1] = des[1]
            else:
                m[des[0]][0] = des[1]
            c[des[1]]= True
            check[des[1]] = True
        root = TreeNode(0)
        check[root] = True
        for k in m.keys():
            if not c.get(k):
                root.val = k
                break
        
        def test(node):
            if not node:
                return
            left, right = None, None
            if m.get(node.val):
                if m[node.val][0] != -1:
                    left = TreeNode(m[node.val][0])
                if m[node.val][1] != -1:
                    right = TreeNode(m[node.val][1])
            check[node.val] = True
            if left and check[left.val]:
                node.left = left
                test(left)
            if right and check[right.val]:
                node.right = right
                test(right)

        test(root)
        return root


r = Solution().createBinaryTree(descriptions=[[20, 15, 1], [
    20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]])
print(r.val)
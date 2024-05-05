# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        tmp = node.next.val
        pre = node
        while node.next:
            node.val = tmp
            pre = node
            node = node.next
            if node.next:
                tmp = node.next.val
        pre.next = None

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        a = head
        b = head.next
        a.next = None
        while b:
            tmp = b.next
            b.next = a
            a, b = b, tmp
        return a


h = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(Solution().reverseList(h))

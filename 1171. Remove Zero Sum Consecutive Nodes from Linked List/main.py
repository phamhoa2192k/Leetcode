# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def remove(i_, j_, h):
            curr1, curr2, i, j = h, h, 0, 0
            if i_ == 0 and j_ == 0:
                return None
            while i < i_ and curr1:
                curr1 = curr1.next
                i += 1
            while j <= j_ and curr2:
                curr2 = curr2.next
                j += 1
            curr1.next = curr2
            return h

        arr = []
        head = ListNode(0, head)
        curr = head
        while curr:
            if curr.next:
                if curr.next.val == 0:
                    curr.next = curr.next.next
                    continue
            arr.append(curr.val)
            curr = curr.next

        if not arr:
            return []

        arr_sum = [arr[0]]
        for val in arr[1:]:
            arr_sum.append(arr_sum[-1] + val)
        if arr_sum[-1] == 0:
            return None
        max_i = len(arr_sum) - 1
        for j in range(len(arr_sum) - 1, -1, -1):
            if j > max_i:
                continue
            for i in range(0, j):
                if arr_sum[j] - arr_sum[i] == 0:
                    head = remove(i, j, head)
                    max_i = i
                    break
        return head.next

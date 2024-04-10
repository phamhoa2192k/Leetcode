# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        end_of_list2 = list2
        while end_of_list2.next:
            end_of_list2 = end_of_list2.next

        pa_list1, pb_list1 = list1, list1

        for _ in range(b - a + 2):
            pb_list1 = pb_list1.next

        for _ in range(a - 1):
            pb_list1 = pb_list1.next
            pa_list1 = pa_list1.next

        pa_list1.next = list2
        end_of_list2.next = pb_list1

        return list1

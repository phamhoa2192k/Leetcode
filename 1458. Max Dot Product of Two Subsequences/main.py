from typing import List
from functools import cache

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1) , len(nums2)
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)
        @cache
        def dp(i, j):
            if i == l1 or j == l2:
                return 0
            use = nums1[i] * nums2[j] + dp(i + 1, j + 1)
            return max(use, dp(i + 1, j), dp(i, j + 1))
        return dp(0, 0)


tc = (
    [5, -4, -3],
    [-4, -3, 0, -4, 2]
)
print(Solution().maxDotProduct(tc[0], tc[1]))

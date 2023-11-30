from typing import List
import math
from functools import cache

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = len(nums), -1, 
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]
        if len(nums) == 0:
            return [-1, -1]

        def binary_search(s, e):
            nonlocal start, end
            if s == e - 1:
                if nums[s] == target:
                    start = min(start, s)
                    end = max(s, end)
                if nums[e] == target:
                    start = min(start, e)
                    end = max(e, end)
                return

            if nums[s] > target or nums[e] < target:
                return
            m = math.floor((s + e) / 2)
            if nums[m] == target:
                start = min(start, m)
                end = max(m, end)
                binary_search(s, m)
                binary_search(m, e)

            elif nums[m] > target:
                binary_search(s, m)
            else:
                binary_search(m, e)

        binary_search(0, len(nums) - 1)
        if start > end:
            return [-1, -1]
        return [start, end]


tc = ([], 7)
print(Solution().searchRange(tc[0], tc[1]))

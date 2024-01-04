from typing import List
from collections import Counter
from math import floor, ceil


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = 0
        c = Counter(nums)
        for v in c.values():
            if v == 1:
                return -1
            else:
                if v % 3 == 0:
                    result += floor(v / 3)
                if v % 3 == 2 or v % 3 == 1:
                    result += ceil(v / 3) + 1
        return result

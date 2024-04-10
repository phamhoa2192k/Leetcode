import sys
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        arr = [-1 for i in range(len(nums))]

        mi = sys.maxsize
        ma = 0

        for num in nums:
            if 0 < num < mi:
                mi = num
            if num > 0 and num > ma:
                ma = num

        if mi > 1:
            return 1

        for num in nums:
            if 0 <= num - mi < len(nums):
                arr[num - mi] = 1

        for i, num in enumerate(arr):
            if num < 0:
                return i + mi

        return ma + 1


print(Solution().firstMissingPositive(nums=[-10, -3, -100, -1000, -239, 1]))

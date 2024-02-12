from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        n = nums[0]

        for num in nums:
            if num == n:
                c += 1
            else:
                c -= 1
                if c < 0:
                    n = num
                    c = 1
        return n

from typing import List
from collections import defaultdict

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        l = len(nums)
        result = 0
        for i in range(0, l):
            m = defaultdict(int)
            count_even = 0
            count_odd = 0
            for j in range(i, l):
                if m[nums[j]] == 0 and nums[j] % 2 == 0:
                    count_even += 1
                    m[nums[j]] += 1
                if m[nums[j]] == 0 and nums[j] % 2 == 1:
                    count_odd += 1
                    m[nums[j]] += 1
                if count_even == count_odd:
                    result = max(result, j - i + 1)
        return result

print(Solution().longestBalanced([1, 2, 2, 1]))
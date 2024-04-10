from typing import List
from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        m = defaultdict(int)
        result = 0
        curr_sum = 0
        m[0] = 1

        for val in nums:
            curr_sum += val
            result += m[curr_sum - goal]
            m[curr_sum] += 1

        return result


print(Solution().numSubarraysWithSum(nums=[1, 0, 1, 0, 1], goal=2))  # 4
print(Solution().numSubarraysWithSum([1, 1, 1, 1, 1], 5))  # 15

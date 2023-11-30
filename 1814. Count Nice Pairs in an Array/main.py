from typing import List
from collections import Counter
import math


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # Ý tưởng nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
        # Tương đương với: nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        # Sau đó tìm số khả năng có thể ghép cặp

        def rev(n):
            return int((str(n)[::-1]))
        MOD = 10**9 + 7

        n = [val - rev(val) for val in nums]
        count = Counter(n)

        result = 0
        for v in count.values():
            result += math.comb(v, 2) % MOD

        return result % MOD


print(Solution().countNicePairs(nums=[13, 10, 35, 24, 76]))

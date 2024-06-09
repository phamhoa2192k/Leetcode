from typing import List
from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        m = defaultdict(int)
        current_sum = 0
        result = 0
        nums.insert(0, 0)
        for num in nums:
            current_sum += num
            result += m[current_sum % k]
            m[current_sum % k] += 1
        return result


print(Solution().subarraysDivByK(nums=[4, 5, 0, -2, -3, 1], k=5))
print(Solution().subarraysDivByK(nums=[5], k=9))

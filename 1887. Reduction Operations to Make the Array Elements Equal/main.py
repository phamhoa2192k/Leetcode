from typing import List
from collections import Counter


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        result, current = 0, 0
        counts = Counter(nums)
        for _, v in sorted(counts.items())[:0:-1]:
            result += current + v
            current += v
        return result


print(Solution().reductionOperations(nums=[1, 1, 2, 2, 3]))

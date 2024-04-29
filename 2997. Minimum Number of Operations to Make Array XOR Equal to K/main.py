from collections import Counter
from functools import reduce
from typing import List

# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/description/


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return Counter(bin(reduce((lambda x, y: x ^ y), nums) ^ k))['1']


print(Solution().minOperations(nums=[2, 1, 3, 4], k=1))

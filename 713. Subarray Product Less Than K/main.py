import math
from typing import List
import bisect
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        def find_smallest_larger(arr, x, hi):
            index = bisect.bisect_right(arr, x, hi=hi)
            if index < len(arr):
                if x == arr[index]:
                    return index + 1
                return index
            else:
                return hi - 1

        if k == 0:
            return 0
        arr = [0 for _ in range(len(nums) + 1)]
        curr = 1
        result = 0
        arr[0] = 1
        for i, num in enumerate(nums):
            curr *= num
            arr[i + 1] = curr

        for i, num in enumerate(arr):
            x = find_smallest_larger(arr, num // k, i + 1)
            result += i - x
        return max(result, 0)

print(Solution().numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100))
print(Solution().numSubarrayProductLessThanK(nums = [1,1,1], k = 1))


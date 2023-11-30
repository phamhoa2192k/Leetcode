from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # Sort mảng, sau đó tham lam
        result = 0
        nums.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            result = max(result, nums[i] + nums[j])
            i, j = i + 1, j - 1
        return result


print(Solution().minPairSum(nums=[3, 5, 4, 2, 4, 6]))

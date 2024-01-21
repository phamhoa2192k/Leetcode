from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [0] * l
        if l == 1:
            return nums[0]
        dp[0], dp[1] = nums[0], nums[1]
        for i in range(2, l):
            val1, val2 = 0, 0
            if i - 2 >= 0:
                val1 = dp[i - 2] + nums[i]
            if i - 3 >= 0:
                val2 = dp[i - 3] + nums[i]
            dp[i] = max(val1, val2)
        return max(dp[l - 2], dp[l - 1])

print(Solution().rob(nums=[2, 7]))

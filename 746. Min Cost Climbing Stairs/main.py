from typing import List
import sys

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [sys.maxsize for _ in range(len(cost))]
        dp[0], dp[1] = cost[0], cost[1]
        for i, c in enumerate(cost[2:], 2):
            dp[i] = min(dp[i - 1] + c, dp[i - 2] + c)
        return min(dp[len(cost) - 2], dp[len(cost) - 1])
            
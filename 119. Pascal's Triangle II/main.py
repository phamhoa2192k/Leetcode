from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1 for _ in range(rowIndex)] for _ in range(rowIndex)]
        if rowIndex == 0:
            return [1]
        dp[0][0] = 1
        dp[0][1], dp[1][1] = 1, 1
        for row in range(1, rowIndex + 1):
            for col in range(1, row):
                dp[row][col] = dp[row - 1][col] + dp[row - 1][col - 1]

        print(dp)
        return dp[rowIndex]


print(Solution().getRow(5))

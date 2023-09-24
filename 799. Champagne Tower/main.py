from typing import List
import math


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0.0 for _ in range(102)] for _ in range(102)]
        dp[0][0] = poured
        for i in range(query_row + 1):
            # Vì hàng i có i + 1 cột
            for j in range(i + 1):
                if dp[i][j] > 1:
                    dp[i + 1][j] += (dp[i][j] - 1) / 2
                    dp[i + 1][j + 1] += (dp[i][j] - 1) / 2
        return min(1.0, dp[query_row][query_glass])


tc = (25, 6, 1)
# tc = (2, 1, 1)
print(Solution().champagneTower(tc[0], tc[1], tc[2]))

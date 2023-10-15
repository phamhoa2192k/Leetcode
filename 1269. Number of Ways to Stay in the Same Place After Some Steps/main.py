class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        if arrLen == 1:
            return 1

        mod = 10 ** 9 + 7
        # Chúng ta không cần duyệt hết độ dài của arrLen vì chúng ta ko để đi quá được số steps
        max_length = min(steps // 2 + 1, arrLen)
        dp = [[0 for _ in range(steps + 1)] for _ in range(max_length + 1)]
        dp[0][1] = 1
        dp[1][1] = 1

        for j in range(2, steps + 1):
            dp[0][j] += dp[1][j - 1] + dp[0][j - 1]
            dp[0][j] %= mod
            dp[max_length - 1][j] += dp[max_length -
                                        2][j - 1] + dp[max_length - 1][j - 1]
            dp[max_length - 1][j] %= mod
            for i in range(1, max_length - 1):
                dp[i][j] += dp[i - 1][j - 1] + dp[i + 1][j - 1] + dp[i][j - 1]
                dp[i][j] %= mod
        return dp[0][steps] % mod


tc = (4, 3)
print(Solution().numWays(tc[0], tc[1]))

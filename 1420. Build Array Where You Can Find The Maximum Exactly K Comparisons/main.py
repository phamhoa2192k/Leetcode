from functools import cache


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = 10 ** 9 + 7

        @cache
        def dp(i, max_so_far, remain):
            if i == n:
                if remain == 0:
                    return 1
                return 0

            ans = dp(i + 1, max_so_far, remain) * max_so_far
            for num in range(max_so_far + 1, m + 1):
                ans += dp(i + 1, num, remain - 1)
            return ans

        return dp(0, 0, k) % mod


print(Solution().numOfArrays(2, 3, 1))

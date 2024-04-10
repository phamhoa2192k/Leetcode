from functools import cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7

        @cache
        def fn(n_, target_):
            if n_ == 1 and 1 <= target_ <= k:
                return 1
            elif n_ == 1 and (target_ > k or target_ < 1):
                return 0
            result = 0
            for i in range(1, k + 1):
                result += fn(n_ - 1, target_ - i)
                result %= MOD
            return result % MOD

        return fn(n, target)


# print(Solution().numRollsToTarget(n=1, k=6, target=3))
print(Solution().numRollsToTarget(n=2, k=6, target=7))
print(Solution().numRollsToTarget(n=30, k=30, target=500))

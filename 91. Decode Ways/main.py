from functools import cache


class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)

        @cache
        def backtrack(k):
            if k >= l:
                return 1
            ones, twos = 0, 0
            if s[k] != '0':
                if k < l:
                    ones = backtrack(k + 1)
            if 9 < int(s[k: k + 2]) <= 26:
                if k < l - 1:
                    twos = backtrack(k + 2)
            return ones + twos
        return backtrack(0)


print(Solution().numDecodings("12"))
print(Solution().numDecodings("226"))
print(Solution().numDecodings("06"))

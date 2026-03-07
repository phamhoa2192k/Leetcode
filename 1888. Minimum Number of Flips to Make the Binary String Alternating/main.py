from typing import List
from collections import defaultdict


class Solution:
    def minFlips(self, s: str) -> int:
        l = len(s)

        ones_odd = 0
        ones_even = 0
        zeros_odd = 0
        zeros_even = 0

        for i in range(l):
            if i % 2 == 0:
                if s[i] == '0':
                    zeros_even += 1
                else:
                    ones_even += 1
            else:
                if s[i] == '0':
                    zeros_odd += 1
                else:
                    ones_odd += 1

        result = min(ones_odd + zeros_even, ones_even + zeros_odd)
        for i in range(l - 1):
            if s[i] == '0':
                zeros_even -= 1
                zeros_odd, zeros_even, ones_odd, ones_even = zeros_even, zeros_odd, ones_even, ones_odd
                if (l - 1) % 2 == 0:
                    zeros_even += 1
                else:
                    zeros_odd += 1
            else:
                ones_even -= 1
                zeros_odd, zeros_even, ones_odd, ones_even = zeros_even, zeros_odd, ones_even, ones_odd
                if (l - 1) % 2 == 0:
                    ones_even += 1
                else:
                    ones_odd += 1
            result = min(result, ones_odd + zeros_even, ones_even + zeros_odd)
        return result

print(Solution().minFlips(s = "101"))
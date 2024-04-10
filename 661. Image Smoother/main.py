from typing import List
from itertools import product
import math


class Solution:
    def maxScore(self, s: str) -> int:
        result = 0
        for i in range(1, len(s)):
            result = max(result, s[0:i].count("0") + s[i:len(s)].count("1"))
        return result


print(Solution().maxScore("00111"))

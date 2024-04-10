from math import log2


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return True if n == 1 << round(log2(n)) == n else False


print(Solution().isPowerOfTwo(8))

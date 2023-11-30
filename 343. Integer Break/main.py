import math


class Solution:
    def integerBreak(self, n: int) -> int:
        result = 0
        for num_of_break in range(2, n + 1):
            mod = n % num_of_break
            product = 1
            for _ in range(num_of_break):
                product *= math.floor(n / num_of_break) + 1 if mod - 1 >= 0 else math.floor(n / num_of_break)
                mod -= 1
                result = max(result, product)
        return result


print(Solution().integerBreak(15))

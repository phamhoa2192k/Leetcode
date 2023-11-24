from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        result = 0
        n = int(len(piles) / 3)
        for val in piles[-2::-2]:
            if n == 0: break
            result += val
            n -= 1
        return result

print(Solution().maxCoins(piles = [9,8,7,6,5,1,2,3,4]))
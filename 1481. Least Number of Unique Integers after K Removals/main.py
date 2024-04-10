from typing import List
from typing import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        s = sorted(Counter(arr).values())[::-1]
        while s and k >= s[-1]:
            k -= s.pop()
        return len(s)


print(Solution().findLeastNumOfUniqueInts(arr=[4, 3, 1, 1, 3, 3, 2], k=3))

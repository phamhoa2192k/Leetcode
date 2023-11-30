from typing import List
import math


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # Ý tưởng là chúng ta sẽ tham lam, bắn những con sẽ tiếp cận base trước
        n = len(dist)
        time = [math.ceil(dist[i] / speed[i]) for i in range(n)]
        time.sort()

        result = 1
        for index, val in enumerate(time[1:], 1):
            if val > index:
                result += 1
            else:
                break
        return result

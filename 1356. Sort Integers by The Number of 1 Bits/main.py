
import functools
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def cmp(x, y):
            x_1, y_1 = list(bin(x)).count("1"), list(bin(y)).count("1")
            if x_1 > y_1:
                return 1
            elif x_1 < y_1:
                return -1
            else:
                if x < y:
                    return -1
                else:
                    return 1
        return sorted(arr, key=functools.cmp_to_key(cmp))


print(Solution().sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]))

from typing import List
from collections import Counter


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # Simple loop
        def findLast(arr, condition):
            for index, val in enumerate(arr[::-1]):
                if condition in val:
                    return len(arr) - index - 1
            return -1

        result = 0
        last_g = findLast(garbage, "G")
        last_m = findLast(garbage, "M")
        last_p = findLast(garbage, "P")

        for index,  gar in enumerate(garbage):
            counter = Counter(gar)
            if index <= last_g and index > 0:
                result += travel[index - 1]
            if index <= last_m and index > 0:
                result += travel[index - 1]
            if index <= last_p and index > 0:
                result += travel[index - 1]
            result += counter["G"] + counter["M"] + counter["P"]
        return result


print(Solution().garbageCollection(
    garbage=["G", "P", "GP", "GG"], travel=[2, 4, 3]))

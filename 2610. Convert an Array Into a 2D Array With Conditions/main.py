from typing import List
from collections import Counter


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        result_2d = []
        while True:
            row = []
            del_key = []
            if len(counter.keys()) == 0:
                break
            for k in counter.keys():
                row.append(k)
                if counter[k] == 1:
                    del_key.append(k)
                else:
                    counter[k] -= 1
            for k in del_key:
                del counter[k]
            result_2d.append(row)
        return result_2d


print(Solution().findMatrix(nums=[1, 3, 4, 1, 2, 3, 1]))

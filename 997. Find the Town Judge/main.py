from typing import List
from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_map = defaultdict(list)

        for t in trust:
            trust_map[t[0]].append(t[1])

        count, result = 0, 0

        for i in range(1, n+1):
            if len(trust_map[i]) == 0:
                count += 1
                result = i
        if count == 1:
            for i in range(1, n + 1):
                if i != result and result not in trust_map[i]:
                    return -1
            return result
        else:
            return -1

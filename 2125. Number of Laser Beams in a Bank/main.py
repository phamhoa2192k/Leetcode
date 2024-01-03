from typing import List
from collections import Counter


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        counters = []
        rows = len(bank)
        for i in range(rows):
            counters.append(Counter(bank[i]))
        last = None
        result = 0
        for i in range(rows):
            if counters[i]['1'] > 0:
                if last != None:
                    result += counters[i]['1'] * counters[last]['1']
                last = i
        return result


print(Solution().numberOfBeams(bank=["011001", "000000", "010100", "001000"]))

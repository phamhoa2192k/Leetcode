from collections import defaultdict


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        m = defaultdict(int)
        for index, c in enumerate(order):
            m[c] = index
        return "".join(sorted(s, key=lambda x: m[x]))


print(Solution().customSortString(order = "cba", s = "abcd" ))

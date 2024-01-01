from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        len_g = len(g)
        len_s = len(s)

        i, j = 0, 0
        result = 0
        while i < len_g and j < len_s:
            if g[i] <= s[j]:
                result += 1
                i += 1
                j += 1
            else:
                j += 1
            
        return result

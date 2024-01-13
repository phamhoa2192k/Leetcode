from collections import Counter, defaultdict


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1 = Counter(s)
        c2 = Counter(t)

        result = 0
        for key, value in c1.items():
            if not c2.get(key):
                result += value
            else:
                diff = value - c2[key]
                if diff > 0:
                    result += diff

        return result


print(Solution().minSteps(s="leetcode", t="practice"))

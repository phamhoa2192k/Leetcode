from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result = 0
        colors += "%"
        l = len(colors)
        s = sum(neededTime)
        last = [neededTime[0], colors[0]]
        for i in range(1, l):
            if colors[i] == last[1]:
                last[0] = max(neededTime[i], last[0])
            if colors[i] != last[1] or i == l - 1:
                result += last[0]
                if i == l - 1:
                    return s - result
                last = [neededTime[i], colors[i], 1]


print(Solution().minCost(colors="abaac", neededTime=[1,2,3,4,5]))

from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])

        l = len(points)
        result = 0
        for i in range(1, l):
            result = max(result, points[i][0] - points[i - 1][0])
        return result


Solution().maxWidthOfVerticalArea([[8, 7], [9, 9], [7, 4], [9, 7]])

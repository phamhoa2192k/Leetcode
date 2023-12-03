from typing import List


class Solution:
    # Chebyshev distance
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def fn(pA, pB):
            return max(abs(pA[0] - pB[0]), abs(pA[1] - pB[1]))
        result = 0
        for i, point in enumerate(points[1:], 1):
            result += fn(point, points[i - 1])
        return result


print(Solution().minTimeToVisitAllPoints(points=[[1, 1], [3, 4], [-1, 0]]))

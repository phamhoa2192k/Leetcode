from typing import List
from bisect import bisect_right
from sys import maxsize

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.insert(0, [-maxsize, -maxsize])
        intervals.append([maxsize, maxsize])
        i = bisect_right(intervals, newInterval[0], key=lambda x: x[0]) - 1
        j = bisect_right(intervals, newInterval[1], key=lambda x: x[1])
        result = []
        for i_ in range(i):
            result.append(intervals[i_])
        if newInterval[0] <= intervals[i][1]:
            if newInterval[1] >= intervals[j][0]:
                result.append([intervals[i][0], intervals[j][1]])
            else:
                result.append([intervals[i][0], newInterval[1]])
                result.append(intervals[j])
        else:
            result.append(intervals[i])
            if newInterval[1] >= intervals[j][0]:
                result.append([newInterval[0], intervals[j][1]])
            else:
                result.append(newInterval)
                result.append(intervals[j])

        for j_ in range(j + 1, len(intervals)):
            result.append(intervals[j_])
        return result[1:len(result) - 1]



print(Solution().insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
print(Solution().insert(intervals=[[1, 5]], newInterval=[0, 3]))
print(Solution().insert(intervals=[[1, 2], [3, 5], [
      6, 7], [8, 10], [12, 16]], newInterval=[4, 8]))

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        m = {}
        m[0] = -1

        curr_0, curr_1 = 0, 0
        max_result = 0
        for i, num in enumerate(nums):
            if num == 0:
                curr_0 += 1
            if num == 1:
                curr_1 += 1

            if m.get(curr_0 - curr_1) != 0 and not m.get(curr_0 - curr_1):
                m[curr_0 - curr_1] = i
            max_result = max(max_result, i - m[curr_0 - curr_1])

        return max_result


print(Solution().findMaxLength(nums=[0, 1, 0]))

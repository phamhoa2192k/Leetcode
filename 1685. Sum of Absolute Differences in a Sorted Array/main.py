from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        s, l, current_sum_left = sum(nums), len(nums), 0

        sum_left = []
        for val in nums:
            current_sum_left += val
            sum_left.append(current_sum_left)
        sum_right = [s - val for val in sum_left]

        result = []
        for i in range(len(nums)):
            result.append((2 * i - l + 2) *
                          nums[i] + sum_right[i] - sum_left[i])
        return result


print(Solution().getSumAbsoluteDifferences(nums=[2, 3, 5]))

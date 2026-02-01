from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]

        tmp_second = 99999999
        tmp_i_second = 1
        for i in range(1, len(nums)):
            if nums[i] <= tmp_second:
                tmp_second = nums[i]
                tmp_i_second = i
        # print(tmp_second, tmp_i_second)

        if tmp_i_second == len(nums) - 1:
            return first + tmp_second + min(nums[1: len(nums)-1])
        elif tmp_i_second == 1:
            return first + tmp_second + min(nums[2: len(nums)])
        else:
            return first + tmp_second + min(min(nums[1: tmp_i_second]), min(nums[tmp_i_second + 1:]))

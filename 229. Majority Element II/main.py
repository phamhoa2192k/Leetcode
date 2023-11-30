import math
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Giải thuật Boyer-Moore
        majority1 , majority2, count1, count2 = 0, 0, 0, 0
        for num in nums:
            if majority1 == num:
                count1 += 1
            elif majority2 == num:
                count2 += 1
            elif count1 == 0:
                majority1 = num
                count1 = 1
            elif count2 == 0:
                majority2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        res, count1, count2 = [], 0, 0
        # Kiểm tra lại giá trị của count, vì có thể count đã bị giảm, không còn chính xác là giá trị trong vòng lặp đầu tiên
        for num in nums:
            if num ==majority1:
                count1 += 1
            if num == majority2:
                count2 += 1
        # Kiểm tra lại kết quả
        if count1 > math.floor(len(nums) / 3):
            res.append(majority1)
        if count2 > math.floor(len(nums) / 3) and majority2 != majority1:
            res.append(majority2)
        return res



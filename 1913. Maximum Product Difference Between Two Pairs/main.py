from typing import List
import sys

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        m1, m2, ma1, ma2 = sys.maxsize, sys.maxsize, 0, 0

        for num in nums:
            if num >= ma2:
                ma1 = ma2
                ma2 = num
            elif ma1 <= num < ma2:
                ma1 = num
            
            if num <= m2:
                m1 = m2
                m2 = num
            elif m1 >= num > m2:
                m1 = num

        return ma1 * ma2 - m1 * m2 
	

Solution().maxProductDifference(nums = [5,6,2,7,4])
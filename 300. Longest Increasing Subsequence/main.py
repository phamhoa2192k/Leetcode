from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [nums[0]]
        len = 1
        for num in nums:
            if arr[-1] < num:
                arr.append(num)
                len += 1
            else:
                index = bisect.bisect_left(arr, num)
                arr[index] = num

        return len    
    

             
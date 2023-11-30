from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        l = len(arr)
        max_val = 0
        arr.sort()
        for i in range(l):
            if arr[i] >= max_val + 1 and max_val <= l:
                arr[i] = max_val + 1
                max_val = arr[i]
        return arr[-1]
    
print(Solution().maximumElementAfterDecrementingAndRearranging([100,1,1000]))
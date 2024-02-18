from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []
        curr = []
        for num in nums:
            if len(curr) == 0:
                curr.append(num)
            elif len(curr) < 3:
                if abs(num - curr[0]) <= k:
                    curr.append(num)
                else:
                    return []
            if len(curr) == 3:
                result.append(curr)
                curr = []
        return result


print(Solution().divideArray(nums = [1,3,4,8,7,9,3,5,1], k = 2))

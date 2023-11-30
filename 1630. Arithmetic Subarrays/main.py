from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # Vì giới hạn dữ liệu khá nhỏ nên bài này có thể làm bình thường
        def check(arr):
            arr.sort()
            if len(arr) < 2:
                return True
            diff = arr[1] - arr[0]
            for index in range(2, len(arr)):
                if arr[index] - arr[index - 1] != diff:
                    return False
            return True
        length = len(l)
        result = []
        for i in range(length):
            result.append(check(nums[l[i]:r[i] + 1]))

        return result


print(Solution().checkArithmeticSubarrays(
    nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5]))

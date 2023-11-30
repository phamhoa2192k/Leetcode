from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums.sort()
        possible_answer = 0
        for num in nums:
            if possible_answer != int(num, 2):
                break
            else:
                possible_answer += 1

        # Chuyển sang dạng string
        possible_answer = str(bin(possible_answer)[2:])
        while len(possible_answer) < len(nums):
            possible_answer = "0" + possible_answer
        return possible_answer


print(Solution().findDifferentBinaryString(nums=["01", "10"]))

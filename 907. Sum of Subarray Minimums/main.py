from typing import List
import sys


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        sumOfMinimums = 0

        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                leftBoundary = stack[-1] if stack else -1
                rightBoundary = i

                count = (mid - leftBoundary) * (rightBoundary - mid) % MOD

                sumOfMinimums += (count * arr[mid]) % MOD
                sumOfMinimums %= MOD
            stack.append(i)

        return int(sumOfMinimums)



print(Solution().sumSubarrayMins(arr=[3, 1, 2, 4]))
print(Solution().sumSubarrayMins(arr = [11,81,94,43,3]))

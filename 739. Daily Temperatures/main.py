from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        stack = []

        for index, temperature in enumerate(temperatures[::-1]):
            while stack and temperature > stack[-1][0]:
                stack.pop()
            if stack:
                result.append(index - stack[-1][1])
            else:
                result.append(0)
            stack.append((temperature, index))
        
        return result[::-1]
    

print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
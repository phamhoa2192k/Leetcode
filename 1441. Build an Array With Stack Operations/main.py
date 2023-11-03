from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        current_target = 0
        result, stack = [], []
        for val in range(1, n + 1):
            if current_target >= len(target):
                break
            if val == target[current_target]:
                while stack and stack[-1] != target[current_target - 1]:
                    result.append("Pop")
                    stack.pop()
                stack.append(val)
                result.append("Push")
                current_target += 1
            else:
                stack.append(val)
                result.append("Push")
        return result


print(Solution().buildArray(target=[1, 3], n=3))

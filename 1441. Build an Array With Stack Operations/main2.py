from typing import List

class Solution:
    def buildArray(self, targets: List[int], n: int) -> List[str]:
        result = []
        before_target = 0
        for target in targets:
            diff = target - before_target - 1
            result += ["Push" for _ in range(diff)] + ["Pop" for _ in range(diff)]
            result.append("Push")
            before_target = target

        return result
    
print(Solution().buildArray(targets = [1,3], n = 3))
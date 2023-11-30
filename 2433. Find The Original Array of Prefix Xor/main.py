from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        curr = pref[0]
        result = [curr]
        for i in pref[1:]:
            result.append(curr ^ i)
            curr ^= result[-1]
        return result
    
print(Solution().findArray([5,2,0,3,1]))

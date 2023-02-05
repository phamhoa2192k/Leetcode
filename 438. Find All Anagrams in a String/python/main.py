from collections import Counter
from typing import List

class Solution:
     def findAnagrams(self, s2: str, s1: str) -> List[int]:
        cntr, w = Counter(s1), len(s1)
        result = []
        for i in range(len(s2)):

            # Trừ đoạn cửa sổ
            if s2[i] in cntr:
                cntr[s2[i]] -= 1

            # Phục hồi cửa sổ trượt
            if i >= w and s2[i-w] in cntr:
                cntr[s2[i-w]] += 1

            # Kiểm tra tất cả các đoạn trên cửa sổ trượt
            if all([cntr[i] == 0 for i in cntr]):
                result.append(i - len(s1) + 1)

        return result

s = Solution()
print(s.findAnagrams("cbaebabacd", "abc"))

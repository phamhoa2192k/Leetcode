from typing import List
from collections import defaultdict


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        m = {}
        l = len(paths)
        result = ""
        for path in paths:
            if not m.get(path[0]):
                m[path[0]] = 1
            else:
                m[path[0]] = 2
            if not m.get(path[1]):
                m[path[1]] = 3
                result = path[1]
            else:
                m[path[1]] = 2
            
        return result

# print(Solution().destCity(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
print(Solution().destCity(paths = [["B","C"],["D","B"],["C","A"]]))
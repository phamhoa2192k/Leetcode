from typing import List
from collections import defaultdict


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        m = {}

        for item in matches:
            win = item[0]
            lose = item[1]

            if not m.get(win):
                m[win] = 0
            
            if not m.get(lose):
                m[lose] = 1
            else:
                m[lose] += 1
        
        m0, m1 = [], []
        
        for k, v in m.items():
            if v == 0:
                m0.append(k)
            if v == 1:
                m1.append(k)
        
        return [sorted(m0), sorted(m1)]
            
			
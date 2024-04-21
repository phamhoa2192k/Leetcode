from typing import List
from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        v = defaultdict(list)
        for e in edges:
            v[e[0]].append(e[1])
            v[e[1]].append(e[0])

        check = [False for _ in range(n)]

        def bfs(curr):
            if check[curr]:
                return
            check[curr] = True
            for v_ in v[curr]:
                bfs(v_)

        bfs(source)
        return check[destination]

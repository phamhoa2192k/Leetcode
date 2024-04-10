from typing import List
import itertools


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        n = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            s = sum(mat[i])
            for j in range(cols):
                n[i][j] += s

        for i in range(cols):
            s = 0
            for j in range(rows):
                s += mat[j][i]
            for j in range(rows):
                n[j][i] += s
        result = 0
        for i, j in itertools.product(range(rows), range(cols)):
            if n[i][j] == 2 and mat[i][j] == 1:
                result += 1
        return result


Solution().numSpecial(mat=[[1, 0, 0], [0, 0, 1], [1, 0, 0]])

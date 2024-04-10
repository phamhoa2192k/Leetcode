from typing import List
import itertools

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        n = [[0 for _ in range(cols)] for _ in range(rows)]
        result = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            s = sum(grid[i])
            for j in range(cols):
                n[i][j] += s

        for i in range(cols):
            s = 0
            for j in range(rows):
                s += grid[j][i]
            for j in range(rows):
                n[j][i] += s
        
        for i, j in itertools.product(range(rows), range(cols)):
            result[i][j] = 2 * n[i][j] - rows - cols
        return result

print(Solution().onesMinusZeros(grid = [[1,1,1],[1,1,1]]))
from typing import List
import itertools

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        def largest(i, j):
            tmp = 0
            for x, y in itertools.product(range(3), range(3)):
                tmp = max(grid[i + x][j + y], tmp)

            return tmp

        n = len(grid)
        result = [[0 for _ in range(n - 2)] for _ in range(n - 2)]
        for i, j in itertools.product(range(n - 2), range(n - 2)):
            result[i][j] = largest(i, j)
        
        return result
    
print(Solution().largestLocal(grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))

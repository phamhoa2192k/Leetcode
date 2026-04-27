from collections import defaultdict
from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = set()
        def dfs(i, j):
            nonlocal visited
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if (i, j) in visited:
                return
            visited.add((i, j))
            next_cells = []
            if grid[i][j] == 1:
                if j > 0 and grid[i][j - 1] in [1, 4, 6]:
                    next_cells.append((i, j - 1))
                if j < n - 1 and grid[i][j + 1] in [1, 3, 5]:
                    next_cells.append((i, j + 1))
            elif grid[i][j] == 2:
                if i > 0 and grid[i - 1][j] in [2, 3, 4]:
                    next_cells.append((i - 1, j))
                if i < m - 1 and grid[i + 1][j] in [2, 5, 6]:
                    next_cells.append((i + 1, j))
            elif grid[i][j] == 3:
                if j > 0 and grid[i][j - 1] in [1, 4, 6]:
                    next_cells.append((i, j - 1))
                if i < m - 1 and grid[i + 1][j] in [2, 5, 6]:
                    next_cells.append((i + 1, j))
            elif grid[i][j] == 4:
                if j < n - 1 and grid[i][j + 1] in [1, 3, 5]:
                    next_cells.append((i, j + 1))
                if i < m - 1 and grid[i + 1][j] in [2, 5, 6]:
                    next_cells.append((i + 1, j))
            elif grid[i][j] == 5:
                if j > 0 and grid[i][j - 1] in [1, 4, 6]:
                    next_cells.append((i, j - 1))
                if i > 0 and grid[i - 1][j] in [2, 3, 4]:
                    next_cells.append((i - 1, j))
            else:
                if j < n - 1 and grid[i][j + 1] in [1, 3, 5]:
                    next_cells.append((i, j + 1))
                if i > 0 and grid[i - 1][j] in [2, 3, 4]:
                    next_cells.append((i - 1, j))
            for ni, nj in next_cells:
                dfs(ni, nj)

        dfs(0, 0)
        return (m - 1, n - 1) in visited      
     

s = Solution()
print(s.hasValidPath([["c","a","d"],["a","a","a"],["a","a","d"],["a","c","d"],["a","b","c"]]))



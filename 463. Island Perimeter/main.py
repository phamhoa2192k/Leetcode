from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        def check(i, j):
            count = 0
            for i_ in range(-1, 2, 2):
                if i + i_ < 0:
                    count += 1
                elif i + i_ >= row:
                    count += 1
                else:
                    if grid[i + i_][j] == 0:
                        count += 1
            
            for j_ in range(-1, 2, 2):
                if j + j_ < 0:
                    count += 1
                elif j + j_ >= col:
                    count += 1
                else:
                    if grid[i][j + j_] == 0:
                        count += 1

            return count

        result = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    result += check(i, j)

        return result             
        
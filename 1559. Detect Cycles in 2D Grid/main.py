from collections import defaultdict
from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        count = 1
        check = {}
        find = False

        def goo( parent_i, parent_j,i, j, current_cycle, step = 0):
            nonlocal find
            nonlocal check
            if find:
                return
            if step >=4 and check.get(i) and check.get(i).get(j) == current_cycle:
                find = True
                return
            if not check.get(i) or not check[i].get(j):
                next_move = []
                if not check.get(i):
                    check[i] = {}
                    check[i][j] = current_cycle
                else:
                    check[i][j] = current_cycle
                if i - 1 >= 0 and grid[i][j] == grid[i - 1][j] and (i - 1 != parent_i or j != parent_j):
                    next_move.append((i - 1, j))
                if j - 1 >= 0 and grid[i][j] == grid[i][j - 1]and (i != parent_i or j - 1 != parent_j) :
                    next_move.append((i, j - 1))
                if i + 1 < len(grid) and grid[i][j] == grid[i + 1][j] and (i + 1 != parent_i or j != parent_j):
                    next_move.append((i + 1, j))
                if j + 1 < len(grid[0]) and grid[i][j] == grid[i][j + 1]and (i != parent_i or j + 1 != parent_j):
                    next_move.append((i, j + 1))
                for n in next_move:
                    goo(i, j, n[0], n[1], current_cycle, step + 1)
            else:
                return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (not check.get(i) or not check[i].get(j)) and find is False:
                    goo(i, j, i, j, count)
                    count += 1
        return find
      

s = Solution()
print(s.containsCycle([["c","a","d"],["a","a","a"],["a","a","d"],["a","c","d"],["a","b","c"]]))



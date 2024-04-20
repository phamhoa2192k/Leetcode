from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        result = []
        row = len(land)
        col = len(land[0])
        check = [[0 for _ in range(col)] for _ in range(row)]
        ones_arr = []
        for i in range(row):
            for j in range(col):
                if land[i][j] == 1:
                    ones_arr.append((i, j))

        def find(x, y):
            tmp = [x, y]
            if check[x][y]:
                return None
            i, j = 1, 1
            while x + i < row:
                if land[x + i][y] == 1:
                    i += 1
                else:
                    break
            while y + j < col:
                if land[x][y + j] == 1:
                    j += 1
                else:
                    break
            for i_ in range(i):
                for j_ in range(j):
                    check[x + i_][y + j_] = True
            tmp += [x + i - 1, y + j - 1]
            return tmp

        for (x, y) in ones_arr:
            find_result = find(x, y)
            if find_result:
                result.append(find_result)

        return result


print(Solution().findFarmland(land=[[1, 0, 0], [0, 1, 1], [0, 1, 1]]))

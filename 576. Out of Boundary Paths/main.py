class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        if maxMove == 0:
            return 0
        steps = [[[0 for _ in range(n)]
                  for _ in range(m)] for _ in range(maxMove)]

        for i in range(n):
            steps[0][0][i] += 1
            steps[0][-1][i] += 1
        for i in range(m):
            steps[0][i][0] += 1
            steps[0][i][-1] += 1
        result = steps[0][startRow][startColumn]
        for step in range(1, maxMove):
            for i in range(m):
                for j in range(n):
                    val1, val2, val3, val4, val5 = 0, 0, 0, 0, 0
                    if j >= 1:
                        val1 = steps[step - 1][i][j - 1]
                    if j < n - 1:
                        val2 = steps[step - 1][i][j + 1]
                    if i >= 1:
                        val3 = steps[step - 1][i - 1][j]
                    if i < m - 1:
                        val4 = steps[step - 1][i + 1][j]
                    steps[step][i][j] = val1 + val2 + val3 + val4
                    steps[step][i][j] %= MOD
            result += steps[step][startRow][startColumn] % MOD
            result %= MOD
        return result


print(Solution().findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0))
print(Solution().findPaths(m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1))
print(Solution().findPaths(m=1, n=2, maxMove=50, startRow=0, startColumn=0))

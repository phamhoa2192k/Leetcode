from typing import List
import itertools


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        result = [[0 for _ in range(rows)] for _ in range(cols)]
        for i , j in itertools.product(range(rows), range(cols)):
            result[j][i] = matrix[i][j]
        return result

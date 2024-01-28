from typing import List
from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(1, cols):
                matrix[row][col] += matrix[row][col - 1]

        count = 0

        for col1 in range(cols):
            for col2 in range(col1, cols):

                sum_val = 0
                prefix_sum = defaultdict(int)
                prefix_sum[0] = 1

                for row in range(rows):
                    sum_val += matrix[row][col2] - (matrix[row][col1 - 1]
                                if col1 >= 1 else 0)
                    
                    count += prefix_sum[sum_val - target]
                    prefix_sum[sum_val] += 1

        return count

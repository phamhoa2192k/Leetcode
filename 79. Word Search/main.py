from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        find = False

        check = [[False for _ in range(col)] for _ in range(row)]
        def traversal(i, j, current, k):
            nonlocal find
            if find:
                return
            if i >= row or i < 0 or j < 0 or j >= col:
                return
            if check[i][j]:
                return
            if board[i][j] != word[k + 1]:
                return
            if current + board[i][j] == word:
                find = True
                return
            if len(current) >= len(word):
                return

            check[i][j] = True
            traversal(i - 1, j, current + board[i][j], k + 1)
            traversal(i + 1, j, current + board[i][j], k + 1)
            traversal(i, j + 1, current + board[i][j], k + 1)
            traversal(i, j - 1, current + board[i][j], k + 1)
            check[i][j] = False

        for i in range(row):
            for j in range(col):
                if find:
                    return True
                traversal(i, j, "", -1)
        return find


print(Solution().exist( board = [["a"]], word = "a"))
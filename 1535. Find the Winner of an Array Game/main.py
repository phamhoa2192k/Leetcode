from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        m = max(arr)

        if k > len(arr):
            return m

        ones, twos = 0, 1
        win_consecutive = (0, 0)
        while True:
            if win_consecutive[1] >= k:
                return win_consecutive[0]
            if arr[ones] > arr[twos]:
                if win_consecutive[0] == arr[ones]:
                    win_consecutive = (win_consecutive[0], win_consecutive[1] + 1)
                else:
                    win_consecutive = (arr[ones], 1)
                arr.append(arr[twos])
                twos += 1
            elif arr[ones] < arr[twos]:
                if win_consecutive[0] == arr[twos]:
                    win_consecutive = (win_consecutive[0], win_consecutive[1] + 1)
                else:
                    win_consecutive = (arr[twos], 1)
                arr.append(arr[ones])
                ones = twos
                twos += 1


print(Solution().getWinner(arr=[2, 1, 3, 5, 4, 6, 7], k=2))

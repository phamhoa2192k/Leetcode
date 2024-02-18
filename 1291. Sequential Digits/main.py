from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        n1 = len(str(low))
        n2 = len(str(high))
        tmp = []
        digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        for i in range(n1, n2 + 1):
            for j in range(1, 11 - i):
                num = ""
                for k in range(j, j + i):
                    num += digit[k]
                tmp.append(num)

        result = []
        for num in tmp:
            val = int(num)
            if low <= val:
                if val <= high:
                    result.append(val)
                else:
                    break
        return result


print(Solution().sequentialDigits(low=100, high=300))
print(Solution().sequentialDigits(low=1000, high=13000))

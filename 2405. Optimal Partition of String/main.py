class Solution:
    def partitionString(self, s: str) -> int:
        result, di = 1, {}
        for i in s:
            if di.get(i):
                di = {}
                result += 1
            di[i] = True
        return result


print(Solution().partitionString("ssssss"))

class Solution:
    def countHomogenous(self, s: str) -> int:
        # Coi các chữ cái tương đương nhau, ta chỉ cần quan tâm đến các khoảng chữ cái giống nhau
        result = 0
        curr_length = 1
        MOD = 10 ** 9 + 7
        s += "%"
        for index, char in enumerate(s[1:], 1):
            if char != s[index - 1]:
                result += round((1 + curr_length) * curr_length / 2) % MOD
                curr_length = 1
            else:
                curr_length += 1
        return result % MOD


print(Solution().countHomogenous("abbcccaa"))
print(Solution().countHomogenous("zzzzz"))

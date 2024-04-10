class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return j - i + 1
            tmp = s[i]
            while s[i] == tmp:
                i += 1
            while s[j] == tmp:
                j -= 1
        if i > j:
            return 0
        return j - i + 1


print(Solution().minimumLength(s="ca"))
print(Solution().minimumLength(s="cabaabac"))
print(Solution().minimumLength(
    s="bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"))

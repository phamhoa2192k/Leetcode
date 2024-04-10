class Solution:
    def makeGood(self, s: str) -> str:
        s = [c for c in s]

        i = 0
        l = len(s)
        while i < l - 1:
            if ord(s[i]) == ord(s[i + 1]) + 32 or ord(s[i]) + 32 == ord(s[i + 1]):
                del s[i: i + 2]
                i = -1
                l -= 2
            i += 1
        return "".join(s)

print(Solution().makeGood("leEeetcode"))
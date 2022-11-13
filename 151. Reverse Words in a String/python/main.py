class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()[::-1]
        return ' '.join(s)

s = Solution()
print(s.reverseWords("the sky is blue"))
from collections import deque


class Solution:
    def reverseParentheses(self, s: str) -> str:
        s1 = []
        for c in s:
            if c != ")":
                s1.append(c)
            else:
                tmp = []
                while s1 and s1[-1] != "(":
                    tmp.append(s1.pop())
                if s1:
                    s1.pop()
                s1 += tmp

        return "".join(s1)


print(Solution().reverseParentheses("(abcd)"))
print(Solution().reverseParentheses("(u(love)i)"))

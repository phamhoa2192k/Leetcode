import re


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_, t_ = [], []
        for i in s:
            if i == '#':
                if s_:
                    s_.pop()
            else:
                s_.append(i)
        for i in t:
            if i == '#':
                if t_:
                    t_.pop()
            else:
                t_.append(i)
        return "".join(s_) == "".join(t_)

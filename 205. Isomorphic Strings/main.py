class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = {}
        m_ = {}

        if len(s) != len(t):
            return False

        for i, ch in enumerate(s):
            if not m.get(ch):
                m[ch] = t[i]
            if not m_.get(t[i]):
                m_[t[i]] = ch

            if m[ch] != t[i] or m_.get(t[i]) != ch:
                return False

        return True
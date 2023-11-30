import string

class Solution:
    def countPalindromicSubsequence(self, s):
        res = 0

        #string.ascii_lowercase = {a,b,c,d ... x,y,z}
        for k in string.ascii_lowercase:
            first, last = s.find(k), s.rfind(k)
            if first > -1:
                res += len(set(s[first + 1: last]))
        return res
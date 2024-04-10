class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        l, r = bin(left)[2:], bin(right)[2:]
        size = max(len(l), len(r))
        while len(l) < size:
            l = "0" + l
        while len(r) < size:
            r = "0" + r
        
        result = ""
        for i in range(size):
            if l[i] == r[i]:
                result += l[i]
            else:
                break
        while len(result) < size:
            result += "0"

        return int("0b" + result, 2)  
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)

        # Check 1
        for key in c1.keys():
            if not c2.get(key):
                return False
        for key in c2.keys():
            if not c1.get(key):
                return False
        
        # Check 2
        c1 = sorted(c1.values())
        c2 = sorted(c2.values())

        for i in range(len(c1)):
            if c1[i] != c2[i]:
                return False
        return True

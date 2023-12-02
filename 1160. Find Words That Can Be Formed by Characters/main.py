from typing import List
from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        counter = Counter(chars)

        for word in words:
            c = Counter(word)
            satisfy = True
            for key, val in c.items():
                if val > counter[key]:
                    satisfy = False
                    break
            if satisfy:
                result += len(word)
        return result

from typing import List
from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = sorted(deck)[::-1]
        d = deque([])
        for val in deck:
            if d:
                d.appendleft(d.pop())
            d.appendleft(val)
        return list(d)


print(Solution().deckRevealedIncreasing(deck = [17,13,11,2,3,5,7]))


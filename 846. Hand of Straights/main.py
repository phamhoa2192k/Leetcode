from typing import List
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
            counter = Counter(hand)
            keys_sorted = sorted(counter.keys())
            if len(hand) % groupSize != 0:
                return False
            for k in keys_sorted:
                  count = counter[k]
                  if count > 0:
                    for i in range(groupSize):
                            if counter[k + i] < count:
                                return False
                            else:
                                counter[k + i] -= count
            return True
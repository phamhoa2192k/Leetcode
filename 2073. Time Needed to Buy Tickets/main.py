from typing import List

from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque(tickets)
        current_k = k
        count = 0
        while True:
            if current_k == 0 and q[0] == 1:
                return count + 1
            if q[0] == 1:
                current_k -= 1
                q.popleft()
            else:
                q.append(q.popleft() - 1)

                current_k -= 1
                if current_k < 0:
                    current_k = len(q) - 1
            count += 1

print(Solution().timeRequiredToBuy(tickets = [5,1,1,1], k = 0))
print(Solution().timeRequiredToBuy(tickets = [2,3,2], k = 2))

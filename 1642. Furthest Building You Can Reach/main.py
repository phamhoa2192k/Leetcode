from typing import List
import sys

from queue import PriorityQueue

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        result = 0
        use_ladder = PriorityQueue()

        for i in range(1, len(heights)):
            diff = heights[i] - heights[i - 1]
            if diff <= 0:
                result += 1
            else:
                if use_ladder.qsize() < ladders:
                    use_ladder.put(diff)
                    result += 1
                else:
                    mi = sys.maxsize if use_ladder.empty() else use_ladder.get()

                    if diff >= mi and bricks >= mi:
                        bricks -= mi
                        use_ladder.put(diff)
                        result += 1
                    elif mi >= diff and bricks >= diff:
                        bricks -= diff
                        use_ladder.put(mi)
                        result += 1
                    else:
                        break

        return result


# print(Solution().furthestBuilding(
#     heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1))
# print(Solution().furthestBuilding(
#     heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2))

# print(Solution().furthestBuilding(
#     heights=[14, 3, 19, 3], bricks=17, ladders=0))

print(Solution().furthestBuilding(heights=[1,100,10,11,12,14], bricks=99, ladders=2))
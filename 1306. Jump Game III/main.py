from collections import defaultdict
from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        l = len(arr)
        m = {}
        for i in range(l):
            m[i] = []
            if i - arr[i] >= 0:
                m[i].append(i - arr[i])
            if i + arr[i] < l:
                m[i].append(i + arr[i])
        target = []
        for i in range(l):
            if arr[i] == 0:
                target.append(i)
        # print(m)
        # print(target)

        def test(st):
            check = defaultdict(bool)
            queue = [st]
            check[st] = True
            while len(queue) > 0:
                curr = queue.pop(0)
                if curr in target:
                    return True
                for neighbor in m[curr]:
                    if not check[neighbor]:
                        check[neighbor] = True
                        queue.append(neighbor)
        return test(start)

s = Solution().canReach([4,2,3,0,3,1,2], 5)
print(s)
from typing import List
from collections import defaultdict, deque
import sys


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        if "0000" == target:
            return 0
        m = defaultdict(bool)
        for d in deadends:
            m[d] = True
        check = defaultdict(lambda: sys.maxsize)

        def next_prev(c):
            if c == "9":
                return ["8", "0"]
            if c == "0":
                return ["9", "1"]
            return [str(int(c) - 1), str(int(c) + 1)]

        def make_possible(n):
            result = []
            for i in range(4):
                tmp = list(n)
                for c in next_prev(n[i]):
                    tmp[i] = c
                    result.append("".join(tmp))
            return result

        q = deque([("0000", 0)])

        result = sys.maxsize

        while q:
            curr, count = q.popleft()
            if curr == target:
                return check[curr]
            possible_case = make_possible(curr)

            for p in possible_case:
                should_add = False
                if check[p] == sys.maxsize and not m[p]:
                    should_add = True
                check[p] = min(check[p], count + 1)
                if should_add:
                    q.append((p, check[p]))
        return -1 if result == sys.maxsize else result


print(Solution().openLock(
    deadends=["0201", "0101", "0102", "1212", "2002"], target="0200"))

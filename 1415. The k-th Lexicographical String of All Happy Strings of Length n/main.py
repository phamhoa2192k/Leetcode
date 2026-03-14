from typing import List


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        find = False
        result = ""
        curr_k = 0
        def dfs(curr):
            nonlocal find, result, curr_k
            # print(curr, curr_k)
            if find:
                return
            if curr_k == k - 1 and len(curr) == n:
                find = True
                result = "".join(curr)
                return
            if len(curr) == n:
                curr_k += 1
            else:
                if len(curr) == 0:
                    for NEXT in ["a", "b", "c"]:
                        dfs([NEXT])
                else:
                    if curr[-1] == "a":
                        for NEXT in ['b', 'c']:
                            dfs(curr + [NEXT])
                    elif curr[-1] == "b":
                        for NEXT in ['a', 'c']:
                            dfs(curr + [NEXT])
                    else:
                        for NEXT in ['a', 'b']:
                            dfs(curr + [NEXT])

        dfs([])
        return result

print(Solution().getHappyString( 3, 9))
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        direction = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
        current = (0, 0)
        s = set((0, 0))
        for p in path:
            current = (current[0] + direction[p][0],
                       current[1] + direction[p][1])
            l = len(s)
            s.add(current)
            if len(s) == l:
                return True
        return False

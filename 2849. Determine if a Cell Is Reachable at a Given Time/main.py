import sys


class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        delta_x = abs(fx - sx)
        delta_y = abs(fy - sy)
        min_step = sys.maxsize
        if delta_x == 0 and delta_y == 0:
            if t == 0:
                return True
            else:
                min_step = 2
        else:
            min_step = min(delta_x, delta_y) + abs(delta_x - delta_y)
        return True if min_step <= t else False

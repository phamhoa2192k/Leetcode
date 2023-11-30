class Solution:
    def numberOfWays(self, corridor: str) -> int:
        result = 1
        nums_seat_last = 0
        possible_position = 0
        MOD = 10**9 + 7
        total_seat = 0
        for val in corridor:
            if nums_seat_last == 2:
                possible_position += 1
            if val == 'S':
                total_seat += 1
                if nums_seat_last < 2:
                    nums_seat_last += 1
                else:
                    if result == 0:
                        result = possible_position
                    else:
                        result *= possible_position
                        result %= MOD
                    nums_seat_last = 1
                    possible_position = 0
        if total_seat % 2 != 0:
            return 0
        if result == 0 and total_seat == 2:
            return 1
        return result % MOD


print(Solution().numberOfWays(corridor="PPSPSP"))

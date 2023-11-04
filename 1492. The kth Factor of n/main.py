class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        curr = 0
        for i in range(1, n + 1):
            if n % i == 0:
                curr += 1
            
            if curr == k:
                return i
        return -1
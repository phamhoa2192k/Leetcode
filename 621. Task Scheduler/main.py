from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        freq.sort()
        chunk = freq[25] - 1
        idle = chunk * n

        for i in range(24, -1, -1):
            idle -= min(chunk, freq[i])

        return len(tasks) + idle if idle >= 0 else len(tasks)

# print(Solution().leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))
# print(Solution().leastInterval(tasks = ["A","C","A","B","D","B"], n = 1))
# print(Solution().leastInterval(tasks = ["A","A","A"], n = 1))
print(Solution().leastInterval(tasks=["A","A","A","B","B","B","C","D","E","F","G","H","I","J","K"], n=7))
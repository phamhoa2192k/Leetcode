from typing import List

from queue import Queue
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = Queue()
        current_students = len(students)
        for s in students:
            q.put(s)

        i = 0
        j = 0
        while True:
            if j == current_students:
                return current_students
            if sandwiches[i] == q.queue[0]:
                i += 1
                current_students -= 1
                q.get()
                j = 0
            else:
                j += 1
                q.put(q.get())


print(Solution().countStudents(students = [1,1,0,0], sandwiches = [0,1,0,1]))
print(Solution().countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]))
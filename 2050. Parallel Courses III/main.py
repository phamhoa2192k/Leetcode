from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]

        # Tạo ma trận liền kề mới
        for prev, next in relations:
            graph[prev - 1].append(next - 1)

        memo = [-1] * n

        def calculateTime(course):
            # Điểm dừng nếu khóa học đó đã được tính toán. Ta có thể thay bằng @cache cũng được
            if memo[course] != -1:
                return memo[course]

            # Điểm dừng khóa học cuối cùng
            if not graph[course]:
                memo[course] = time[course]
                return memo[course]

            max_prerequisite_time = 0
            for prereq in graph[course]:
                # Khóa học kế tiếp sẽ lấy giá trị đường đi lớn nhất có thể đến đỉnh tiếp
                max_prerequisite_time = max(
                    max_prerequisite_time, calculateTime(prereq))

            # Thời gian hoàn thành khóa học tiếp sẽ tính bằng cách 
            memo[course] = max_prerequisite_time + time[course]
            return memo[course]

        overall_min_time = 0
        for course in range(n):
            overall_min_time = max(overall_min_time, calculateTime(course))

        return overall_min_time

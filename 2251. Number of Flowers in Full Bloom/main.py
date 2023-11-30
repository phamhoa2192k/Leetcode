from typing import List
from bisect import bisect_right, bisect_left


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        result = []
        start_arr = [flower[0] for flower in flowers]
        start_arr.sort()
        end_arr = [flower[1] for flower in flowers]
        end_arr.sort()

        # Để ý rằng số hoa nở trong ngày thứ i sẽ bằng số hoa bắt đầu nở trước ngày i trừ đi số hoa tàn trước ngày i
        for person in people:
            # Tìm kiếm nhị phân số ngày mà nở trước ngày đến
            start = bisect_left(start_arr, person + 1)
            #Tìm kiếm nhị phân số ngày mà hoa tàn trước ngày đến
            end = bisect_right(end_arr, person - 1)
            result.append(start - end)
        return result


tc = ([[1, 6], [3, 7], [9, 12], [4, 13]],  [2, 3, 7, 11])
Solution().fullBloomFlowers(tc[0], tc[1])

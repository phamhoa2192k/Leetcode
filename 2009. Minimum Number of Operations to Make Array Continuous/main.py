from typing import List
import sys
import bisect


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length_nums = len(nums)
        result = sys.maxsize
        nums = sorted(set(nums))

        for current_index, current_val in enumerate(nums):
            # Mảng kết quả bắt đầu từ vị trí current_val
            # Từ đó tính được giá trị cuối cùng của mảng
            ele = current_val + length_nums - 1

            # Hàm bisect_right sẽ tìm index mà tại đó ele được điền vào mảng
            index_ele = bisect.bisect_right(nums, ele)
            # Như vậy, số phần tử phải điền lại giá trị sẽ được tính là chiều dài của nums, bỏ đi khoảng [current_index, index_ele]
            result = min(result, length_nums - (index_ele - current_index))

        return result


tc = [1, 10, 100, 1000]
print(Solution().minOperations(tc))

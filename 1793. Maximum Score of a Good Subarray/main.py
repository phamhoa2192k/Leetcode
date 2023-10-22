from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left, right = k, k
        min_val_of_good_array = nums[k]
        result = nums[k]

        # Chúng ta sử dụng 2 con trỏ và 1 chút tham làm để dịch 2 con trỏ left, right về 2 đầu của mảng
        while left > 0 or right < len(nums) - 1:
            # Tham lam 1 chút vs 2 con trỏ ở 2 đầu
            if left == 0 or (right < len(nums) - 1 and nums[right + 1] > nums[left - 1]):
                right += 1
            else:
                left -= 1

            # Cập nhật giá trị và kết quả
            min_val_of_good_array = min(
                min_val_of_good_array, nums[right], nums[left])
            result = max(result, min_val_of_good_array * (right - left + 1))

        return result


print(Solution().maximumScore(nums=[5, 5, 4, 5, 4, 1, 1, 1], k=0))

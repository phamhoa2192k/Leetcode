from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # Mảng nums sẽ đóng vai trò là mảng dp luôn
        dq = deque()
        for i in range(len(nums)):
            nums[i] += nums[dq[0]] if dq else 0
            # Các giá trị nằm ngoài k sẽ bị xóa ở đằng trước
            # Các giá trị dp cuối mảng sẽ bị xóa cho đến khi lớn hơn giá trị nums[i]
            # Việc này sẽ làm cho mảng dq luôn giữ được được giá trị giảm dần
            while dq and (i - dq[0] >= k or nums[i] >= nums[dq[-1]]):
                dq.pop() if nums[i] >= nums[dq[-1]] else dq.popleft()
            if nums[i] > 0:
                dq.append(i)
        return max(nums)


print(Solution().constrainedSubsetSum([10, 2, -10, 5, 20], k=2))

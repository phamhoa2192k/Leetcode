from collections import Counter

# Counter : đếm số phần tử trong List
# all: kiểm tra nếu có 1 phần tử == 0 || == False, return False
# Ý tưởng: Dùng cửa sổ trượt. Nghĩa là trượt trên s2 ...1 đoạn s1.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, w = Counter(s1), len(s1)
        for i in range(len(s2)):

            # Trừ đoạn cửa sổ
            if s2[i] in cntr:
                cntr[s2[i]] -= 1

            # Phục hồi cửa sổ trượt
            if i >= w and s2[i-w] in cntr:
                cntr[s2[i-w]] += 1

            # Kiểm tra tất cả các đoạn trên cửa sổ trượt
            if all([cntr[i] == 0 for i in cntr]):
                return True

        return False

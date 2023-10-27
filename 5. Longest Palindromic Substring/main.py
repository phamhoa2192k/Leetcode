class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        result, start, end = 0, 0, 0

        # Chúng ta bắt đầu xây dựng chuỗi palindromic từ một ví trí i, sau đó mở rộng về 2 phía
        for i in range(l):
            # Trường hợp cho palindromic có độ dài là lẻ
            for j in range(1, l):
                if i - j >= 0 and i + j < l and s[i - j] == s[i + j]:
                    if result < j * 2 + 1:
                        result, start, end = j * 2 + 1, i - j, i + j
                else:
                    break

            # Trường hợp cho palindromic có độ dài là chẵn
            if i + 1 < l and s[i] == s[i + 1]:
                if result < 2:
                    result, start, end = 2, i, i + 1
                for j in range(1, l):
                    if i - j >= 0 and i + j + 1 < l and s[i - j] == s[i + 1 + j]:
                        if result < j * 2 + 2:
                            result, start, end = j * 2 + 2, i - j, i + j + 1
                    else:
                        break

        return s[start: end + 1]


print(Solution().longestPalindrome("xaabacxcabaaxcabaax"))

class Solution:
    def getLastMoment(self, n, left, right):
        ans = 0
        # Khi 2 con kiến chạm nhau, hãy nhìn nhận rằng 2 con kiến đó đang đổi vị trí cho nhau và đi xuyên qua nhau.

        # Như vậy max time là thời gian max để 1 con kiến chạm vào đầu bên kia
        for i in left:
            ans = max(ans, abs(0 - i))
        for i in right:
            ans = max(ans, abs(n - i))
        return ans
from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # Kiểm tra đồ thị có liên thông không
        def checkGraphIsConnected():
            di = [False for _ in range(n)]
            s = [0]
            neighbor = {}
            for i in range(n):
                if not neighbor.get(i):
                    neighbor[i] = set([])
                if leftChild[i] >= 0:
                    neighbor[i].add(leftChild[i])
                if rightChild[i] >= 0:
                    neighbor[i].add(rightChild[i])

                if leftChild[i] >= 0:
                    if not neighbor.get(leftChild[i]):
                        neighbor[leftChild[i]] = set([i])
                    else:
                        neighbor[leftChild[i]].add(i)

                if rightChild[i] >= 0:
                    if not neighbor.get(rightChild[i]):
                        neighbor[rightChild[i]] = set([i])
                    else:
                        neighbor[rightChild[i]].add(i)
            while s:
                node = s.pop()
                if di[node]:
                    continue
                else:
                    di[node] = True
                for i in neighbor[node]:
                    s.append(i)
            for i in range(n):
                if not di[i]:
                    return False

            return True

        if not checkGraphIsConnected():
            return False

        # Là một cây nhị phân nếu mỗi node chỉ có 1 cha và cả đồ thị chỉ có nhiều nhất một node không có cha
        parent = [-1 for _ in range(n)]
        for i in range(n):
            if leftChild[i] >= 0:
                if parent[leftChild[i]] == -1 or parent[leftChild[i]] == i:
                    parent[leftChild[i]] = i
                else:
                    return False

            if rightChild[i] >= 0:
                if parent[rightChild[i]] == -1 or parent[rightChild[i]] == i:
                    parent[rightChild[i]] = i
                else:
                    return False
        peak = 0
        for i in range(n):
            if parent[i] == -1:
                peak += 1
        if peak != 1:
            return False
        return True


print(Solution().validateBinaryTreeNodes(
    n=4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1]))

# Dù hơi chậm 1 tí cơ mà cũng là một lời giải chấp nhận được

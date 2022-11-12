class MedianFinder:

    def __init__(self):
        self.n = []

    def addNum(self, num: int) -> None:
        self.n.append(num)

    def findMedian(self) -> float:
        if len(self.n) % 2 == 1:
            return self.n[int(len(self.n) / 2) + 1]
        else:
            x1 = self.n[int(len(self.n) / 2) + 1] 
            x2 = self.n[int(len(self.n) / 2)] 
            return (x1 + x2) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        heappush(self.max_heap, -num)

        if len(self.max_heap) >= len(self.min_heap) + 2:
            heappush(self.min_heap, -(heappop(self.max_heap)))
        elif self.max_heap and self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            heappush(self.min_heap, -(heappop(self.max_heap)))
            heappush(self.max_heap, -(heappop(self.min_heap)))

    def findMedian(self):
        if len(self.max_heap) - len(self.min_heap) == 1:
            return -self.max_heap[0]
        else:
            return float(self.min_heap[0] - self.max_heap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

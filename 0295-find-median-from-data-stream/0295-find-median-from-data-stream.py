import heapq

class MedianFinder:

    def __init__(self):

      self.smaller = []
      self.larger = []
      heapq.heapify(self.smaller)
      heapq.heapify(self.larger)

    def addNum(self, num: int) -> None:
      # the largest number in smaller
      sLargest = None
      if len(self.smaller):
        sLargest = -(self.smaller[0])
      # the smallest number in largest
      lSmallest = None
      if len(self.larger):
        lSmallest = self.larger[0]

      # if both heaps are empty
      if not sLargest and not lSmallest:
        heapq.heappush(self.smaller, -num)
      # if larger is empty
      elif not lSmallest:
        # if num is greater than or equal to the largest number in smaller
        if num >= sLargest:
          # push num to larger
          heapq.heappush(self.larger, num)
        else:
          # pop the largest number in smaller
          heapq.heappop(self.smaller)
          # push the largest number in smaller to larger
          heapq.heappush(self.larger, sLargest)
          # push num to smaller
          heapq.heappush(self.smaller, -num)
      # if both heaps contain elements
      else:
        # if num is smaller than the largest number in smaller
        if num < sLargest:
          # balance the number of elements in smaller and larger
          if (len(self.smaller) + 1) - len(self.larger) > 1:
            if num >= sLargest:
              heapq.heappush(self.larger, num)
            else:
              # pop the largest number in smaller
              heapq.heappop(self.smaller)
              # push it to larger
              heapq.heappush(self.larger, sLargest)
              # push num to smaller
              heapq.heappush(self.smaller, -num)
          else:
            # push num to smaller
            heapq.heappush(self.smaller, -num)
        else:
          # balance the number of elements in smaller and larger
          if (len(self.larger) + 1) - len(self.smaller) > 1:
            # if num is less than the smallest number in larger
            if num <= lSmallest:
              # push num to smaller
              heapq.heappush(self.smaller, -num)
            else:  
              # pop the smallest number in larger
              heapq.heappop(self.larger)
              # push it to smaller
              heapq.heappush(self.smaller, -lSmallest)
              # push num to larger
              heapq.heappush(self.larger, num)
          else:
            # push num to larger
            heapq.heappush(self.larger, num)

    def findMedian(self) -> float:
        # if both heaps are empty
        if len(self.smaller) == 0 and len(self.larger) == 0:
          return None
        # if the number of elements is even
        if len(self.smaller) == len(self.larger):
          sLargest = -(self.smaller[0])
          lSmallest = self.larger[0]
          return (sLargest + lSmallest) / 2
        # if the number of elements is odd
        else:
          # if smaller has more elements than larger
          if len(self.smaller) > len(self.larger):
            # the median is the largest number of smaller
            return -(self.smaller[0])
          else:
            # the median is the smallest number of larger
            return self.larger[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
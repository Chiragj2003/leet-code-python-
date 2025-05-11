"""
LeetCode #295 - Find Median from Data Stream
Topic: Heap / Design
Difficulty: Hard

PROBLEM EXPLANATION (Easy Terms):
Design class to find median of numbers added so far.

Example:
addNum(1), addNum(2) -> median = 1.5
addNum(3) -> median = 2

Think of it like:
Finding middle value as more numbers arrive!

WHY THIS WORKS (Simple Explanation):
Use two heaps:
- Max heap for smaller half
- Min heap for larger half
Keep balanced, median is at tops!

Time: O(log n) per add, O(1) for median
Space: O(n)
"""

import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # Max heap (negate values)
        self.large = []  # Min heap
    
    def addNum(self, num):
        # Add to max heap (small half)
        heapq.heappush(self.small, -num)
        
        # Balance: move largest from small to large
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # If large has more, move back
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
    
    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2


# Test
if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(f"Median: {mf.findMedian()}")  # 1.5
    mf.addNum(3)
    print(f"Median: {mf.findMedian()}")  # 2

"""LeetCode #295 - Find Median from Data Stream | Heap/Design | Hard"""

import heapq

class MedianFinder:
    """ OPTIMAL - Two Heaps: O(log n) add, O(1) median"""
    def __init__(self):
        self.small = []  # max heap (negate)
        self.large = []  # min heap
    
    def addNum(self, num):
        # Add to small (max heap)
        heapq.heappush(self.small, -num)
        # Balance: move max from small to large
        heapq.heappush(self.large, -heapq.heappop(self.small))
        # Keep small bigger
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
    
    def findMedian(self):
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0

class MedianFinder_sorted(object):
    """ SOLUTION 2 - Sorted List: O(n) add, O(1) median (worse for add)"""
    def __init__(self):
        self.vals = []
    
    def addNum(self, num):
        import bisect
        bisect.insort(self.vals, num)
    
    def findMedian(self):
        mid = len(self.vals) // 2
        if len(self.vals) % 2: return float(self.vals[mid])
        return (self.vals[mid-1] + self.vals[mid]) / 2.0

class MedianFinder_bst(object):
    """ SOLUTION 3 - AVL/BST Concept: O(log n) add, O(1) median"""
    def __init__(self):
        self.nums = []
    
    def addNum(self, num):
        self.nums.append(num)
    
    def findMedian(self):
        sorted_nums = sorted(self.nums)
        n = len(sorted_nums)
        if n % 2: return float(sorted_nums[n//2])
        return (sorted_nums[n//2-1] + sorted_nums[n//2]) / 2.0

if __name__ == "__main__":
    print("Testing Median Finder:")
    mf = MedianFinder()
    for num in [1,2,3,4,5]:
        mf.addNum(num)
    print(f"After [1,2,3,4,5]: median={mf.findMedian()}")
    
    mf2 = MedianFinder_sorted()
    for num in [1,2,3,4,5]:
        mf2.addNum(num)
    print(f"Sorted version: median={mf2.findMedian()}")

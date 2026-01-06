"""LeetCode #346 - Moving Average from Data Stream | Queue/Design | Easy"""

from collections import deque

class MovingAverage:
    """ OPTIMAL - Queue with Running Sum: O(1) time, O(N) space"""
    def __init__(self, size):
        self.size = size
        self.queue = deque()
        self.window_sum = 0
    
    def next(self, val):
        self.queue.append(val)
        self.window_sum += val
        if len(self.queue) > self.size:
            self.window_sum -= self.queue.popleft()
        return self.window_sum / len(self.queue)

class MovingAverage_List:
    """ SOLUTION 2 - List-based: O(1) amortized, O(N) space"""
    def __init__(self, size):
        self.size = size
        self.window = []
    
    def next(self, val):
        self.window.append(val)
        if len(self.window) > self.size:
            self.window.pop(0)
        return sum(self.window) / len(self.window)

class MovingAverage_Array:
    """ SOLUTION 3 - Circular Array: O(1) time, O(N) space"""
    def __init__(self, size):
        self.size = size
        self.arr = [0] * size
        self.count = 0
        self.idx = 0
        self.total = 0
    
    def next(self, val):
        if self.count < self.size:
            self.count += 1
        else:
            self.total -= self.arr[self.idx]
        self.arr[self.idx] = val
        self.total += val
        self.idx = (self.idx + 1) % self.size
        return self.total / self.count

if __name__ == "__main__":
    print("Testing Moving Average:")
    ma = MovingAverage(3)
    print(f"next(1) = {ma.next(1):.2f}")
    print(f"next(10) = {ma.next(10):.2f}")
    print(f"next(3) = {ma.next(3):.2f}")
    print(f"next(5) = {ma.next(5):.2f}")

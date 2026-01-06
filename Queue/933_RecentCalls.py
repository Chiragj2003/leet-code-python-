"""LeetCode #933 - Number of Recent Calls | Queue | Easy"""

from collections import deque

class RecentCounter:
    """ OPTIMAL - Queue/Deque: O(1) amortized, O(N) space"""
    def __init__(self):
        self.queue = deque()
    
    def ping(self, t):
        self.queue.append(t)
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)

class RecentCounter_List:
    """ SOLUTION 2 - List: O(N) per ping, O(N) space"""
    def __init__(self):
        self.calls = []
    
    def ping(self, t):
        self.calls.append(t)
        self.calls = [x for x in self.calls if x >= t - 3000]
        return len(self.calls)

class RecentCounter_BinarySearch:
    """ SOLUTION 3 - Binary Search: O(log N) per ping, O(N) space"""
    def __init__(self):
        self.calls = []
    
    def ping(self, t):
        self.calls.append(t)
        import bisect
        idx = bisect.bisect_left(self.calls, t - 3000)
        return len(self.calls) - idx

if __name__ == "__main__":
    print("Testing Recent Counter:")
    rc = RecentCounter()
    print(f"ping(1): {rc.ping(1)}")
    print(f"ping(100): {rc.ping(100)}")
    print(f"ping(3001): {rc.ping(3001)}")
    print(f"ping(3002): {rc.ping(3002)}")

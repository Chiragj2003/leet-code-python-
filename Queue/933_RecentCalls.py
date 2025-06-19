"""
LeetCode #933 - Number of Recent Calls
Topic: Queue
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Count number of requests in the last 3000 milliseconds.

Each time ping(t) is called, count how many pings happened
between [t-3000, t] inclusive.

Example:
ping(1) -> 1 (only this ping)
ping(100) -> 2 (pings at 1 and 100)
ping(3001) -> 3 (all three pings)
ping(3002) -> 3 (ping at 1 is too old, only 100, 3001, 3002)

Think of it like:
Counting website visits in the last 5 minutes.
Old visits expire and don't count anymore!

WHY THIS WORKS (Simple Explanation):
Use a queue to store timestamps:
1. Add new timestamp to queue
2. Remove old timestamps (older than t-3000)
3. Return queue size (recent pings)

Queue is perfect because we remove from front (oldest first)!

Time Complexity: O(1) amortized per ping
Space Complexity: O(w) where w = 3000 (max window size)
"""

from collections import deque

class RecentCounter:
    """
    Count recent pings in last 3000ms
    
    Visual example:
    ping(1):    queue=[1]           -> count=1
    ping(100):  queue=[1,100]       -> count=2
    ping(3001): queue=[1,100,3001]  -> count=3
    ping(3002): queue=[100,3001,3002] -> count=3 (removed 1, too old!)
    """
    
    def __init__(self):
        """Initialize empty queue for timestamps"""
        self.queue = deque()
    
    def ping(self, t):
        """
        Add new ping at time t
        Return count of pings in [t-3000, t]
        """
        # Add current timestamp
        self.queue.append(t)
        
        # Remove old timestamps (older than t-3000)
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        
        # Return count of recent pings
        return len(self.queue)


class RecentCounterVerbose:
    """Verbose version showing the process"""
    
    def __init__(self):
        self.queue = deque()
        print("Created RecentCounter")
        print("Window size: 3000ms\n")
    
    def ping(self, t):
        print(f"=== ping({t}) ===")
        
        # Add current timestamp
        self.queue.append(t)
        print(f"Added timestamp {t}")
        
        # Show removal process
        removed = []
        while self.queue and self.queue[0] < t - 3000:
            old = self.queue.popleft()
            removed.append(old)
        
        if removed:
            print(f"Removed old timestamps: {removed} (older than {t-3000})")
        else:
            print("No old timestamps to remove")
        
        print(f"Current queue: {list(self.queue)}")
        print(f"Count of recent pings: {len(self.queue)}")
        print()
        
        return len(self.queue)


def demonstrate_sliding_window():
    """
    Demonstrate the sliding window concept
    """
    print("=== Sliding Window Demonstration ===\n")
    
    counter = RecentCounter()
    test_times = [1, 100, 3001, 3002]
    
    for t in test_times:
        count = counter.ping(t)
        window_start = t - 3000
        print(f"Time: {t}ms")
        print(f"  Window: [{window_start}, {t}]")
        print(f"  Recent pings: {count}")
        print(f"  Queue: {list(counter.queue)}")
        print()


# Test cases
if __name__ == "__main__":
    print("=== Test Case 1: Basic Usage ===")
    counter = RecentCounter()
    
    inputs = [1, 100, 3001, 3002]
    expected = [1, 2, 3, 3]
    
    for t, exp in zip(inputs, expected):
        result = counter.ping(t)
        status = "✓" if result == exp else "✗"
        print(f"{status} ping({t}) = {result} (expected {exp})")
    
    print("\n" + "="*50)
    print("=== Test Case 2: Verbose Example ===")
    print("="*50 + "\n")
    
    counter2 = RecentCounterVerbose()
    counter2.ping(1)
    counter2.ping(100)
    counter2.ping(3001)
    counter2.ping(3002)
    
    print("="*50)
    demonstrate_sliding_window()
    
    # Additional test
    print("="*50)
    print("=== Test Case 3: Many Pings ===\n")
    
    counter3 = RecentCounter()
    
    # Simulate pings every 100ms for 10 seconds
    for t in range(0, 10001, 100):
        count = counter3.ping(t)
        if t % 1000 == 0:  # Print every second
            print(f"Time {t}ms: {count} recent pings")
    
    print(f"\nFinal queue size: {len(counter3.queue)} (should be ~30)")

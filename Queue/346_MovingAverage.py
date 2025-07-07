"""
LeetCode #346 - Moving Average from Data Stream
Topic: Queue / Design
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Calculate moving average of last N numbers from a stream.

Example (size=3):
next(1) = 1/1 = 1.0
next(10) = (1+10)/2 = 5.5
next(3) = (1+10+3)/3 = 4.67
next(5) = (10+3+5)/3 = 6.0  (1 dropped, window full)

Think of it like:
Average temperature of last 7 days.
As new day comes, oldest day drops out!

WHY THIS WORKS (Simple Explanation):
Use a queue to maintain window of last N numbers:
1. Add new number to queue and sum
2. If queue size > N, remove oldest and subtract from sum
3. Return sum / queue_size

Queue maintains order, sum avoids recalculating!

Time Complexity: O(1) per operation
Space Complexity: O(N) for queue
"""

from collections import deque

class MovingAverage:
    """
    Calculate moving average of last N numbers
    
    Visual example (size=3):
    next(1):  queue=[1], sum=1  -> avg=1.0
    next(10): queue=[1,10], sum=11 -> avg=5.5
    next(3):  queue=[1,10,3], sum=14 -> avg=4.67
    next(5):  queue=[10,3,5], sum=18 -> avg=6.0 (removed 1)
    """
    
    def __init__(self, size):
        """
        Initialize with window size
        """
        self.size = size
        self.queue = deque()
        self.window_sum = 0
    
    def next(self, val):
        """
        Add new value and return moving average
        """
        # Add new value
        self.queue.append(val)
        self.window_sum += val
        
        # Remove oldest if window full
        if len(self.queue) > self.size:
            removed = self.queue.popleft()
            self.window_sum -= removed
        
        # Return average
        return self.window_sum / len(self.queue)


class MovingAverageVerbose:
    """Verbose version with detailed output"""
    
    def __init__(self, size):
        self.size = size
        self.queue = deque()
        self.window_sum = 0
        print(f"Created MovingAverage with window size {size}\n")
    
    def next(self, val):
        print(f"=== next({val}) ===")
        
        # Add new value
        self.queue.append(val)
        self.window_sum += val
        print(f"Added {val} to queue")
        
        # Remove oldest if needed
        if len(self.queue) > self.size:
            removed = self.queue.popleft()
            self.window_sum -= removed
            print(f"Removed {removed} (window full)")
        
        # Calculate average
        avg = self.window_sum / len(self.queue)
        
        print(f"Current queue: {list(self.queue)}")
        print(f"Sum: {self.window_sum}")
        print(f"Count: {len(self.queue)}")
        print(f"Average: {self.window_sum}/{len(self.queue)} = {avg:.2f}")
        print()
        
        return avg


class MovingAverageSimple:
    """
    Simple version using list (easier to understand)
    But less efficient for large windows
    """
    
    def __init__(self, size):
        self.size = size
        self.numbers = []
    
    def next(self, val):
        # Add new number
        self.numbers.append(val)
        
        # Keep only last N numbers
        if len(self.numbers) > self.size:
            self.numbers.pop(0)  # Remove first (oldest)
        
        # Calculate and return average
        return sum(self.numbers) / len(self.numbers)


# Test cases
if __name__ == "__main__":
    print("=== Test Case 1: Basic Usage ===\n")
    
    ma = MovingAverage(3)
    
    test_values = [1, 10, 3, 5]
    expected = [1.0, 5.5, 4.67, 6.0]
    
    for val, exp in zip(test_values, expected):
        result = ma.next(val)
        status = "✓" if abs(result - exp) < 0.01 else "✗"
        print(f"{status} next({val}) = {result:.2f} (expected {exp:.2f})")
    
    print("\n" + "="*50)
    print("=== Test Case 2: Verbose Example ===")
    print("="*50 + "\n")
    
    ma2 = MovingAverageVerbose(3)
    ma2.next(1)
    ma2.next(10)
    ma2.next(3)
    ma2.next(5)
    
    # Test with different window size
    print("="*50)
    print("=== Test Case 3: Larger Window (size=5) ===\n")
    
    ma3 = MovingAverage(5)
    
    values = [1, 2, 3, 4, 5, 6, 7, 8]
    print("Adding values: [1, 2, 3, 4, 5, 6, 7, 8]\n")
    
    for val in values:
        avg = ma3.next(val)
        print(f"After adding {val}: average = {avg:.2f}, window = {list(ma3.queue)}")
    
    # Compare implementations
    print("\n" + "="*50)
    print("=== Test Case 4: Comparing Implementations ===\n")
    
    ma_queue = MovingAverage(3)
    ma_simple = MovingAverageSimple(3)
    
    test_vals = [1, 10, 3, 5, 20, 7]
    
    print("Values: [1, 10, 3, 5, 20, 7]\n")
    
    for val in test_vals:
        avg1 = ma_queue.next(val)
        avg2 = ma_simple.next(val)
        match = "✓" if abs(avg1 - avg2) < 0.001 else "✗"
        print(f"next({val}): Queue={avg1:.2f}, Simple={avg2:.2f} {match}")

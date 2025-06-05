"""
LeetCode #622 - Design Circular Queue
Topic: Queue / Design
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Design a circular queue (ring buffer) with fixed size.
When queue is full and you add, it wraps around to the beginning.

Operations: enQueue, deQueue, Front, Rear, isEmpty, isFull

Example:
CircularQueue(3) -> Create queue of size 3
enQueue(1) -> [1, _, _]
enQueue(2) -> [1, 2, _]
enQueue(3) -> [1, 2, 3] (full!)
deQueue() -> [_, 2, 3]
enQueue(4) -> [4, 2, 3] (wrapped to front!)

Think of it like:
A circular parking lot - when you reach the end, continue from start!

WHY THIS WORKS (Simple Explanation):
Use an array with two pointers:
- front: where to dequeue from
- rear: where to enqueue next

Use modulo (%) to wrap around when reaching end!

Time Complexity: O(1) for all operations
Space Complexity: O(k) where k is queue size
"""

class MyCircularQueue:
    """
    Circular Queue implementation using array
    
    Visual example (size=3):
    Initial: [_, _, _]  front=0, rear=0, size=0
    
    enQueue(1): [1, _, _]  front=0, rear=1, size=1
    enQueue(2): [1, 2, _]  front=0, rear=2, size=2
    enQueue(3): [1, 2, 3]  front=0, rear=0, size=3 (wrapped!)
    deQueue():  [_, 2, 3]  front=1, rear=0, size=2
    enQueue(4): [4, 2, 3]  front=1, rear=1, size=3 (wrapped to start!)
    """
    
    def __init__(self, k):
        """
        Initialize queue with size k
        """
        self.queue = [0] * k  # Fixed size array
        self.max_size = k
        self.front = 0  # Front pointer
        self.rear = 0   # Rear pointer
        self.size = 0   # Current number of elements
    
    def enQueue(self, value):
        """
        Add element to queue
        Return True if successful, False if full
        """
        if self.isFull():
            return False
        
        # Add element at rear
        self.queue[self.rear] = value
        
        # Move rear pointer (wrap around using modulo)
        self.rear = (self.rear + 1) % self.max_size
        
        self.size += 1
        return True
    
    def deQueue(self):
        """
        Remove element from front of queue
        Return True if successful, False if empty
        """
        if self.isEmpty():
            return False
        
        # Move front pointer (wrap around)
        self.front = (self.front + 1) % self.max_size
        
        self.size -= 1
        return True
    
    def Front(self):
        """
        Get front element without removing
        Return -1 if empty
        """
        if self.isEmpty():
            return -1
        return self.queue[self.front]
    
    def Rear(self):
        """
        Get rear element without removing
        Return -1 if empty
        """
        if self.isEmpty():
            return -1
        
        # Rear points to NEXT position, so we need previous
        rear_index = (self.rear - 1 + self.max_size) % self.max_size
        return self.queue[rear_index]
    
    def isEmpty(self):
        """Check if queue is empty"""
        return self.size == 0
    
    def isFull(self):
        """Check if queue is full"""
        return self.size == self.max_size


# Verbose version for learning
class MyCircularQueueVerbose:
    """Circular Queue with detailed output"""
    
    def __init__(self, k):
        self.queue = [None] * k
        self.max_size = k
        self.front = 0
        self.rear = 0
        self.size = 0
        print(f"Created circular queue of size {k}")
        self.print_state()
    
    def print_state(self):
        """Print current state of queue"""
        print(f"Queue: {self.queue}")
        print(f"Front={self.front}, Rear={self.rear}, Size={self.size}/{self.max_size}")
        print()
    
    def enQueue(self, value):
        if self.isFull():
            print(f"❌ Cannot enQueue({value}) - Queue is FULL")
            return False
        
        self.queue[self.rear] = value
        print(f"✓ enQueue({value}) at position {self.rear}")
        
        self.rear = (self.rear + 1) % self.max_size
        self.size += 1
        
        self.print_state()
        return True
    
    def deQueue(self):
        if self.isEmpty():
            print(f"❌ Cannot deQueue - Queue is EMPTY")
            return False
        
        value = self.queue[self.front]
        print(f"✓ deQueue() removed {value} from position {self.front}")
        
        self.queue[self.front] = None  # Clear for visualization
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        
        self.print_state()
        return True
    
    def Front(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]
    
    def Rear(self):
        if self.isEmpty():
            return -1
        rear_index = (self.rear - 1 + self.max_size) % self.max_size
        return self.queue[rear_index]
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.max_size


# Test cases
if __name__ == "__main__":
    print("=== Testing Circular Queue ===\n")
    
    # Test 1: Basic operations
    print("Test 1: Basic operations")
    queue = MyCircularQueue(3)
    
    print(f"enQueue(1): {queue.enQueue(1)}")  # True
    print(f"enQueue(2): {queue.enQueue(2)}")  # True
    print(f"enQueue(3): {queue.enQueue(3)}")  # True
    print(f"enQueue(4): {queue.enQueue(4)}")  # False (full)
    print(f"Rear(): {queue.Rear()}")          # 3
    print(f"isFull(): {queue.isFull()}")      # True
    print(f"deQueue(): {queue.deQueue()}")    # True
    print(f"enQueue(4): {queue.enQueue(4)}")  # True (now has space)
    print(f"Rear(): {queue.Rear()}")          # 4
    print()
    
    # Test 2: Verbose example
    print("="*50)
    print("Test 2: Verbose example showing wrap-around")
    print("="*50)
    queue2 = MyCircularQueueVerbose(3)
    
    queue2.enQueue(1)
    queue2.enQueue(2)
    queue2.enQueue(3)
    queue2.enQueue(4)  # Should fail
    queue2.deQueue()
    queue2.enQueue(4)  # Should succeed and wrap around
    queue2.deQueue()
    queue2.enQueue(5)
    
    print(f"Front element: {queue2.Front()}")
    print(f"Rear element: {queue2.Rear()}")

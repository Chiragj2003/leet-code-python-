"""
LeetCode #641 - Design Circular Deque
Topic: Queue / Deque / Design
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Design a circular double-ended queue (deque).
Can add/remove from BOTH front and rear!

Operations: insertFront, insertLast, deleteFront, deleteLast,
            getFront, getRear, isEmpty, isFull

Example:
CircularDeque(3)
insertLast(1)  -> [1]
insertLast(2)  -> [1, 2]
insertFront(3) -> [3, 1, 2]
insertFront(4) -> false (full!)
getRear()      -> 2

Think of it like:
A line where people can join from front OR back!
And leave from front OR back!

WHY THIS WORKS (Simple Explanation):
Use array with two pointers (front and rear).
Both can move in either direction with wrap-around!

Key: Use modulo (%) for circular indexing

Time Complexity: O(1) for all operations
Space Complexity: O(k) where k is deque size
"""

class MyCircularDeque:
    """
    Circular Deque implementation
    
    Visual (size=3):
    insertLast(1):  [1, _, _]  front=0, rear=1
    insertLast(2):  [1, 2, _]  front=0, rear=2
    insertFront(3): [1, 2, 3]  front=2, rear=2 (3 is at front!)
    
    Array: [1, 2, 3]
    But logically: [3, 1, 2] (front=2 points to 3)
    """
    
    def __init__(self, k):
        """Initialize deque with size k"""
        self.deque = [0] * k
        self.max_size = k
        self.front = 0
        self.rear = 0
        self.size = 0
    
    def insertFront(self, value):
        """Add element at front"""
        if self.isFull():
            return False
        
        if self.size == 0:
            # First element
            self.deque[self.front] = value
        else:
            # Move front backward (with wrap)
            self.front = (self.front - 1 + self.max_size) % self.max_size
            self.deque[self.front] = value
        
        self.size += 1
        return True
    
    def insertLast(self, value):
        """Add element at rear"""
        if self.isFull():
            return False
        
        if self.size == 0:
            # First element
            self.deque[self.rear] = value
        else:
            # Move rear forward (with wrap)
            self.rear = (self.rear + 1) % self.max_size
            self.deque[self.rear] = value
        
        self.size += 1
        return True
    
    def deleteFront(self):
        """Remove element from front"""
        if self.isEmpty():
            return False
        
        if self.size == 1:
            # Last element
            self.front = self.rear = 0
        else:
            # Move front forward
            self.front = (self.front + 1) % self.max_size
        
        self.size -= 1
        return True
    
    def deleteLast(self):
        """Remove element from rear"""
        if self.isEmpty():
            return False
        
        if self.size == 1:
            # Last element
            self.front = self.rear = 0
        else:
            # Move rear backward
            self.rear = (self.rear - 1 + self.max_size) % self.max_size
        
        self.size -= 1
        return True
    
    def getFront(self):
        """Get front element"""
        if self.isEmpty():
            return -1
        return self.deque[self.front]
    
    def getRear(self):
        """Get rear element"""
        if self.isEmpty():
            return -1
        return self.deque[self.rear]
    
    def isEmpty(self):
        """Check if deque is empty"""
        return self.size == 0
    
    def isFull(self):
        """Check if deque is full"""
        return self.size == self.max_size


class MyCircularDequeVerbose:
    """Verbose version with visual output"""
    
    def __init__(self, k):
        self.deque = [None] * k
        self.max_size = k
        self.front = 0
        self.rear = 0
        self.size = 0
        print(f"Created Circular Deque of size {k}")
        self.print_state()
    
    def print_state(self):
        """Visualize deque state"""
        print(f"Array: {self.deque}")
        print(f"Front={self.front}, Rear={self.rear}, Size={self.size}/{self.max_size}")
        
        # Show logical order
        if self.size > 0:
            logical = []
            idx = self.front
            for _ in range(self.size):
                logical.append(self.deque[idx])
                idx = (idx + 1) % self.max_size
            print(f"Logical order: {logical}")
        print()
    
    def insertFront(self, value):
        if self.isFull():
            print(f"❌ insertFront({value}) - Deque is FULL")
            return False
        
        if self.size == 0:
            self.deque[self.front] = value
        else:
            self.front = (self.front - 1 + self.max_size) % self.max_size
            self.deque[self.front] = value
        
        self.size += 1
        print(f"✓ insertFront({value})")
        self.print_state()
        return True
    
    def insertLast(self, value):
        if self.isFull():
            print(f"❌ insertLast({value}) - Deque is FULL")
            return False
        
        if self.size == 0:
            self.deque[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.max_size
            self.deque[self.rear] = value
        
        self.size += 1
        print(f"✓ insertLast({value})")
        self.print_state()
        return True
    
    def deleteFront(self):
        if self.isEmpty():
            print(f"❌ deleteFront() - Deque is EMPTY")
            return False
        
        value = self.deque[self.front]
        self.deque[self.front] = None
        
        if self.size == 1:
            self.front = self.rear = 0
        else:
            self.front = (self.front + 1) % self.max_size
        
        self.size -= 1
        print(f"✓ deleteFront() removed {value}")
        self.print_state()
        return True
    
    def deleteLast(self):
        if self.isEmpty():
            print(f"❌ deleteLast() - Deque is EMPTY")
            return False
        
        value = self.deque[self.rear]
        self.deque[self.rear] = None
        
        if self.size == 1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear - 1 + self.max_size) % self.max_size
        
        self.size -= 1
        print(f"✓ deleteLast() removed {value}")
        self.print_state()
        return True
    
    def getFront(self):
        return -1 if self.isEmpty() else self.deque[self.front]
    
    def getRear(self):
        return -1 if self.isEmpty() else self.deque[self.rear]
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.max_size


# Test cases
if __name__ == "__main__":
    print("=== Test Case 1: Basic Operations ===\n")
    
    deque = MyCircularDeque(3)
    
    print(f"insertLast(1): {deque.insertLast(1)}")
    print(f"insertLast(2): {deque.insertLast(2)}")
    print(f"insertFront(3): {deque.insertFront(3)}")
    print(f"insertFront(4): {deque.insertFront(4)}")  # False, full
    print(f"getRear(): {deque.getRear()}")
    print(f"isFull(): {deque.isFull()}")
    print(f"deleteLast(): {deque.deleteLast()}")
    print(f"insertFront(4): {deque.insertFront(4)}")
    print(f"getFront(): {deque.getFront()}")
    
    print("\n" + "="*50)
    print("=== Test Case 2: Verbose Example ===")
    print("="*50 + "\n")
    
    deque2 = MyCircularDequeVerbose(3)
    
    deque2.insertLast(1)
    deque2.insertLast(2)
    deque2.insertFront(3)
    deque2.insertFront(4)  # Should fail
    deque2.deleteLast()
    deque2.insertFront(4)
    deque2.deleteFront()
    deque2.insertLast(5)
    
    print(f"Front element: {deque2.getFront()}")
    print(f"Rear element: {deque2.getRear()}")

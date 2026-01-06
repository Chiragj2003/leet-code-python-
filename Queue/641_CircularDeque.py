"""LeetCode #641 - Design Circular Deque | Queue/Design | Medium"""

class MyCircularDeque:
    """ OPTIMAL - Array with Two Pointers: O(1) all ops, O(K) space"""
    def __init__(self, k):
        self.size = k
        self.arr = [0] * k
        self.front = 0
        self.rear = 0
        self.count = 0
    
    def insertFront(self, value):
        if self.isFull(): return False
        if self.count > 0:
            self.front = (self.front - 1 + self.size) % self.size
        self.arr[self.front] = value
        self.count += 1
        return True
    
    def insertLast(self, value):
        if self.isFull(): return False
        if self.count > 0:
            self.rear = (self.rear + 1) % self.size
        self.arr[self.rear] = value
        self.count += 1
        return True
    
    def deleteFront(self):
        if self.isEmpty(): return False
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True
    
    def deleteLast(self):
        if self.isEmpty(): return False
        self.rear = (self.rear - 1 + self.size) % self.size
        self.count -= 1
        return True
    
    def getFront(self):
        return -1 if self.isEmpty() else self.arr[self.front]
    
    def getRear(self):
        return -1 if self.isEmpty() else self.arr[self.rear]
    
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count == self.size

class MyCircularDeque_List:
    """ SOLUTION 2 - List-based: O(1) amortized, O(K) space"""
    def __init__(self, k):
        self.size = k
        self.deque = []
    
    def insertFront(self, value):
        if len(self.deque) == self.size: return False
        self.deque.insert(0, value)
        return True
    
    def insertLast(self, value):
        if len(self.deque) == self.size: return False
        self.deque.append(value)
        return True
    
    def deleteFront(self):
        if not self.deque: return False
        self.deque.pop(0)
        return True
    
    def deleteLast(self):
        if not self.deque: return False
        self.deque.pop()
        return True
    
    def getFront(self):
        return -1 if not self.deque else self.deque[0]
    
    def getRear(self):
        return -1 if not self.deque else self.deque[-1]
    
    def isEmpty(self):
        return len(self.deque) == 0
    
    def isFull(self):
        return len(self.deque) == self.size

if __name__ == "__main__":
    print("Testing Circular Deque:")
    cd = MyCircularDeque(3)
    print(f"insertLast(1): {cd.insertLast(1)}")
    print(f"insertLast(2): {cd.insertLast(2)}")
    print(f"insertFront(3): {cd.insertFront(3)}")
    print(f"insertFront(4): {cd.insertFront(4)} (should be False)")
    print(f"getFront: {cd.getFront()}, getRear: {cd.getRear()}")
    print(f"deleteFront: {cd.deleteFront()}")
    print(f"insertFront(4): {cd.insertFront(4)}")

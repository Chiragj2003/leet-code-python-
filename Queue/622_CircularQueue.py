"""LeetCode #622 - Design Circular Queue | Queue/Design | Medium"""

class MyCircularQueue:
    """ OPTIMAL - Array with Pointers: O(1) all ops, O(K) space"""
    def __init__(self, k):
        self.size = k
        self.arr = [0] * k
        self.front = 0
        self.rear = -1
        self.count = 0
    
    def enQueue(self, value):
        if self.isFull(): return False
        self.rear = (self.rear + 1) % self.size
        self.arr[self.rear] = value
        self.count += 1
        return True
    
    def deQueue(self):
        if self.isEmpty(): return False
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True
    
    def Front(self):
        return -1 if self.isEmpty() else self.arr[self.front]
    
    def Rear(self):
        return -1 if self.isEmpty() else self.arr[self.rear]
    
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count == self.size

class MyCircularQueue_List:
    """ SOLUTION 2 - List-based: O(1) ops, O(K) space"""
    def __init__(self, k):
        self.size = k
        self.queue = []
    
    def enQueue(self, value):
        if len(self.queue) == self.size: return False
        self.queue.append(value)
        return True
    
    def deQueue(self):
        if not self.queue: return False
        self.queue.pop(0)
        return True
    
    def Front(self):
        return -1 if not self.queue else self.queue[0]
    
    def Rear(self):
        return -1 if not self.queue else self.queue[-1]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def isFull(self):
        return len(self.queue) == self.size

if __name__ == "__main__":
    print("Testing Circular Queue:")
    cq = MyCircularQueue(3)
    print(f"enQueue(1): {cq.enQueue(1)}")
    print(f"enQueue(2): {cq.enQueue(2)}")
    print(f"enQueue(3): {cq.enQueue(3)}")
    print(f"enQueue(4): {cq.enQueue(4)} (should be False)")
    print(f"Front: {cq.Front()}, Rear: {cq.Rear()}")
    print(f"deQueue: {cq.deQueue()}")
    print(f"enQueue(4): {cq.enQueue(4)} (now True)")

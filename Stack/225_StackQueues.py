"""
LeetCode #225 - Implement Stack using Queues
Topic: Stack
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Implement a stack (LIFO - Last In First Out) using only queue operations.
Queue is FIFO (First In First Out), so we need to reverse the behavior!

Example:
stack.push(1);
stack.push(2);
stack.pop();    // returns 2 (last in, first out)
stack.top();    // returns 1

WHY THIS WORKS (Simple Explanation):
When we push a new element:
1. Add it to the queue
2. Rotate all previous elements to the back

Think of a circular conveyor belt:
- Add new item
- Rotate belt so new item is now at front
- This makes newest item accessible first (LIFO)!

Example:
push(1): queue=[1]
push(2): queue=[2] -> rotate -> queue=[2,1]
push(3): queue=[3,2,1] -> becomes queue=[3,2,1]
pop(): remove from front -> returns 3

Time Complexity: push O(n), pop/top O(1)
Space Complexity: O(n)
"""

from collections import deque

class MyStack:
    """
    Stack implemented using one queue
    
    Visual example:
    push(1): [1]
    push(2): add 2 -> [1,2] -> rotate -> [2,1]
    push(3): add 3 -> [2,1,3] -> rotate -> [3,2,1]
    pop(): remove from front -> returns 3
    """
    
    def __init__(self):
        """Initialize the stack using a queue"""
        self.queue = deque()
    
    def push(self, x):
        """
        Push element to top of stack
        
        Strategy:
        1. Add element to queue
        2. Rotate all previous elements to the back
        3. New element is now at front (making it LIFO)
        """
        self.queue.append(x)
        
        # Rotate: move all previous elements to back
        # This puts the new element at front
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
    
    def pop(self):
        """
        Remove and return top element from stack
        Simply pop from front (newest element is there)
        """
        return self.queue.popleft()
    
    def top(self):
        """
        Get top element without removing
        """
        return self.queue[0]
    
    def empty(self):
        """
        Check if stack is empty
        """
        return len(self.queue) == 0


# Test cases with step-by-step walkthrough
if __name__ == "__main__":
    stack = MyStack()
    
    # Push operations
    print("=== Pushing elements ===")
    stack.push(1)
    print(f"After push(1): queue={list(stack.queue)}")
    
    stack.push(2)
    print(f"After push(2): queue={list(stack.queue)}")
    
    stack.push(3)
    print(f"After push(3): queue={list(stack.queue)}")
    
    # Top and pop operations
    print("\n=== Stack operations ===")
    print(f"Top element: {stack.top()}")      # 3
    print(f"Pop: {stack.pop()}")              # 3
    print(f"Top element: {stack.top()}")      # 2
    print(f"Is empty: {stack.empty()}")       # False
    
    stack.pop()
    stack.pop()
    print(f"After popping all: empty={stack.empty()}")  # True

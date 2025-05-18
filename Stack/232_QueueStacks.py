"""
LeetCode #232 - Implement Queue using Stacks
Topic: Stack
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Implement a queue (FIFO - First In First Out) using only stack operations.
Stack is LIFO (Last In First Out), so we need to be clever!

Think of it like:
- Queue: People in a line - first person in line gets served first
- Stack: Stack of plates - last plate added is first plate removed

Example:
queue.push(1);
queue.push(2);
queue.pop();    // returns 1 (first in, first out)
queue.peek();   // returns 2

WHY THIS WORKS (Simple Explanation):
Use TWO stacks:
1. Input stack: for pushing elements
2. Output stack: for popping elements

When popping: if output stack empty, move all from input to output
This reverses the order, making it FIFO!

Time Complexity: O(1) amortized for all operations
Space Complexity: O(n) - two stacks
"""

class MyQueue:
    """
    Queue implemented using two stacks
    
    Visual example:
    push(1): input=[1], output=[]
    push(2): input=[1,2], output=[]
    pop():   move to output: input=[], output=[2,1]
             pop from output: returns 1
             state: input=[], output=[2]
    """
    
    def __init__(self):
        """Initialize two stacks"""
        self.input_stack = []   # For pushing
        self.output_stack = []  # For popping
    
    def push(self, x):
        """
        Push element to the back of queue
        Simply push to input stack
        """
        self.input_stack.append(x)
    
    def pop(self):
        """
        Remove and return element from front of queue
        
        If output stack empty, move all from input to output
        This reverses the order!
        """
        self._move_input_to_output()
        return self.output_stack.pop()
    
    def peek(self):
        """
        Get front element without removing
        """
        self._move_input_to_output()
        return self.output_stack[-1]
    
    def empty(self):
        """
        Check if queue is empty
        """
        return len(self.input_stack) == 0 and len(self.output_stack) == 0
    
    def _move_input_to_output(self):
        """
        Helper: Move elements from input to output stack
        Only do this if output stack is empty
        """
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())


# Test cases with explanations
if __name__ == "__main__":
    queue = MyQueue()
    
    queue.push(1)
    queue.push(2)
    print(f"Front element: {queue.peek()}")  # 1
    
    print(f"Pop: {queue.pop()}")             # 1
    print(f"Is empty: {queue.empty()}")      # False
    
    print(f"Front element: {queue.peek()}")  # 2
    print(f"Pop: {queue.pop()}")             # 2
    print(f"Is empty: {queue.empty()}")      # True

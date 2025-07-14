"""
LeetCode #155 - Min Stack
Topic: Stack
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Design a stack that supports push, pop, top, and retrieving minimum element
all in O(1) time (constant time - super fast!).

Example:
MinStack stack = new MinStack();
stack.push(-2);
stack.push(0);
stack.push(-3);
stack.getMin();   // return -3
stack.pop();
stack.top();      // return 0
stack.getMin();   // return -2

WHY THIS WORKS (Simple Explanation):
Use two stacks:
1. Main stack: stores all elements
2. Min stack: stores minimum values at each level

When pushing: also push current minimum to min_stack
When popping: pop from both stacks
To get min: just peek at top of min_stack!

Time Complexity: O(1) for all operations
Space Complexity: O(n) - extra stack for minimums
"""

class MinStack:
    """
    Stack with minimum tracking
    
    Simple idea:
    - Regular stack for all values
    - Extra stack to remember: "what's the minimum up to this point?"
    
    Example:
    Push -2: stack=[-2], min_stack=[-2] (min is -2)
    Push 0:  stack=[-2,0], min_stack=[-2,-2] (min still -2)
    Push -3: stack=[-2,0,-3], min_stack=[-2,-2,-3] (min now -3)
    """
    
    def __init__(self):
        """Initialize empty stacks"""
        self.stack = []
        self.min_stack = []  # Stores minimum at each level
    
    def push(self, val):
        """
        Push value to stack
        Also track minimum
        """
        self.stack.append(val)
        
        # Update minimum stack
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            # Min is either current value or previous min
            current_min = min(val, self.min_stack[-1])
            self.min_stack.append(current_min)
    
    def pop(self):
        """
        Remove top element
        Also remove from min_stack
        """
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
    
    def top(self):
        """
        Get top element
        """
        if self.stack:
            return self.stack[-1]
        return None
    
    def getMin(self):
        """
        Get minimum element in O(1) time
        """
        if self.min_stack:
            return self.min_stack[-1]
        return None


# Test cases with explanations
if __name__ == "__main__":
    stack = MinStack()
    
    stack.push(-2)
    print(f"After push(-2), min: {stack.getMin()}")  # -2
    
    stack.push(0)
    print(f"After push(0), min: {stack.getMin()}")   # -2
    
    stack.push(-3)
    print(f"After push(-3), min: {stack.getMin()}")  # -3
    
    stack.pop()
    print(f"After pop(), min: {stack.getMin()}")     # -2
    
    print(f"Top element: {stack.top()}")             # 0
    print(f"Current min: {stack.getMin()}")          # -2

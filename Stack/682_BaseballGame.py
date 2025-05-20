"""
LeetCode #682 - Baseball Game
Topic: Stack
Difficulty: Easy

PROBLEM EXPLANATION:
You're keeping score for a baseball game with these rules:
- Integer x: Add score x to record
- '+': Add sum of previous two scores
- 'D': Add double of previous score
- 'C': Remove previous score
Return the sum of all scores in the record.

Example:
Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
- "5": record = [5], sum = 5
- "2": record = [5, 2], sum = 7
- "C": record = [5], sum = 5 (removed 2)
- "D": record = [5, 10], sum = 15 (double of 5)
- "+": record = [5, 10, 15], sum = 30 (5 + 10)

APPROACH (Stack):
1. Use a stack to maintain the current valid scores
2. Process each operation:
   - Number: push to stack
   - '+': push sum of last two
   - 'D': push double of last
   - 'C': pop last score
3. Return sum of all scores in stack

Time Complexity: O(n)
Space Complexity: O(n)
"""

def calPoints(operations):
    """
    Returns the sum of all scores
    """
    stack = []
    
    for op in operations:
        if op == '+':
            # Add sum of previous two scores
            stack.append(stack[-1] + stack[-2])
        elif op == 'D':
            # Double of previous score
            stack.append(2 * stack[-1])
        elif op == 'C':
            # Remove previous score
            stack.pop()
        else:
            # It's a number, add to stack
            stack.append(int(op))
    
    return sum(stack)


# Test cases
if __name__ == "__main__":
    test1 = ["5", "2", "C", "D", "+"]
    print(f"Test 1: {calPoints(test1)}")  # Expected: 30
    
    test2 = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    print(f"Test 2: {calPoints(test2)}")
    # Expected: 27
    # Explanation: [5, -2, 4] -> [5, -2] -> [5, -2, -4] -> [5, -2, -4, 9] 
    # -> [5, -2, -4, 9, 5] -> [5, -2, -4, 9, 5, 14] = 27
    
    test3 = ["1", "C"]
    print(f"Test 3: {calPoints(test3)}")  # Expected: 0
    
    test4 = ["1"]
    print(f"Test 4: {calPoints(test4)}")  # Expected: 1

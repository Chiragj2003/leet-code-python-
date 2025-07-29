"""
LeetCode #946 - Validate Stack Sequences
Topic: Stack
Difficulty: Medium

PROBLEM EXPLANATION:
Given two integer arrays pushed and popped, each with distinct values,
return true if this could have been the result of a sequence of push and
pop operations on an initially empty stack.

Example:
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2

APPROACH (Simulate with Stack):
1. Simulate the push/pop operations with a stack
2. Push elements from pushed array
3. After each push, pop from stack if top matches next in popped
4. At the end, stack should be empty if sequence is valid

Time Complexity: O(n)
Space Complexity: O(n)
"""

def validateStackSequences(pushed, popped):
    """
    Returns True if the sequences are valid
    """
    stack = []
    pop_index = 0  # Index in popped array
    
    # Process each element in pushed array
    for num in pushed:
        # Push to stack
        stack.append(num)
        
        # Pop from stack if top matches next element in popped
        while stack and pop_index < len(popped) and stack[-1] == popped[pop_index]:
            stack.pop()
            pop_index += 1
    
    # Stack should be empty if sequence is valid
    return len(stack) == 0


# Test cases
if __name__ == "__main__":
    test1_pushed = [1, 2, 3, 4, 5]
    test1_popped = [4, 5, 3, 2, 1]
    print(f"Test 1: {validateStackSequences(test1_pushed, test1_popped)}")
    # Expected: True
    
    test2_pushed = [1, 2, 3, 4, 5]
    test2_popped = [4, 3, 5, 1, 2]
    print(f"Test 2: {validateStackSequences(test2_pushed, test2_popped)}")
    # Expected: False
    
    test3_pushed = [1, 0]
    test3_popped = [1, 0]
    print(f"Test 3: {validateStackSequences(test3_pushed, test3_popped)}")
    # Expected: True
    
    test4_pushed = [1, 2, 3]
    test4_popped = [3, 2, 1]
    print(f"Test 4: {validateStackSequences(test4_pushed, test4_popped)}")
    # Expected: True

"""
LeetCode #20 - Valid Parentheses
Topic: Stack
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Check if brackets are properly matched and closed in correct order.
Like checking if every opening bracket '(' has a matching closing bracket ')'.

Example:
Input: s = "()"
Output: true

Input: s = "([)]"
Output: false (wrong order - ')' comes before ']')

WHY THIS WORKS (Simple Explanation):
Use a stack (like a stack of plates):
- When you see opening bracket: push to stack
- When you see closing bracket: pop from stack and check if they match
- At the end, stack should be empty (all brackets matched)

Think of it like: every time you open a door, you must close it!

Time Complexity: O(n) - check each character once
Space Complexity: O(n) - worst case, all opening brackets
"""

def isValid(s):
    """
    Check if parentheses are valid
    
    Simple rules:
    1. Opening brackets: (, [, { -> push to stack
    2. Closing brackets: ), ], } -> pop and check match
    3. At end: stack should be empty
    """
    # Stack to store opening brackets
    stack = []
    
    # Map closing brackets to their opening pairs
    matching = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    for char in s:
        if char in matching:
            # It's a closing bracket
            # Check if it matches the last opening bracket
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()
        else:
            # It's an opening bracket, push to stack
            stack.append(char)
    
    # Valid only if all brackets are matched (stack is empty)
    return len(stack) == 0


# Test cases with explanations
if __name__ == "__main__":
    test1 = "()"
    print(f"Test 1: {isValid(test1)}")
    # Expected: True
    # '(' pushed, ')' pops and matches
    
    test2 = "()[]{}"
    print(f"Test 2: {isValid(test2)}")
    # Expected: True
    # All pairs match in correct order
    
    test3 = "(]"
    print(f"Test 3: {isValid(test3)}")
    # Expected: False
    # '(' pushed, ']' doesn't match '('
    
    test4 = "([)]"
    print(f"Test 4: {isValid(test4)}")
    # Expected: False
    # Stack: ['(', '['], then ')' tries to pop '[' but they don't match
    
    test5 = "{[]}"
    print(f"Test 5: {isValid(test5)}")
    # Expected: True
    # Properly nested

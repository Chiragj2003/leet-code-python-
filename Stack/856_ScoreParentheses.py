"""
LeetCode #856 - Score of Parentheses
Topic: Stack
Difficulty: Medium

PROBLEM EXPLANATION:
Given a balanced parentheses string, compute the score based on rules:
- "()" has score 1
- "AB" has score A + B (where A and B are balanced strings)
- "(A)" has score 2 * A

Example:
Input: s = "()"
Output: 1

Input: s = "(())"
Output: 2 (2 * 1)

Input: s = "()()"
Output: 2 (1 + 1)

Input: s = "(()(()))"
Output: 6 (2 * (1 + 2*1))

APPROACH (Stack):
1. Use stack to track scores at each nesting level
2. When we see '(': push 0 (start new level)
3. When we see ')': pop and calculate score
   - If popped value is 0, it's "()" -> score = 1
   - Otherwise, it's "(A)" -> score = 2 * A
   - Add score to previous level

Time Complexity: O(n)
Space Complexity: O(n)
"""

def scoreOfParentheses(s):
    """
    Returns the score of balanced parentheses
    """
    stack = [0]  # Initialize with 0 for base level
    
    for char in s:
        if char == '(':
            # Start new level
            stack.append(0)
        else:  # char == ')'
            # End current level
            current_score = stack.pop()
            
            if current_score == 0:
                # This was "()", score = 1
                stack[-1] += 1
            else:
                # This was "(A)", score = 2 * A
                stack[-1] += 2 * current_score
    
    return stack[0]


# Alternative: O(1) space using depth counting
def scoreOfParentheses_v2(s):
    """
    Count depth and add score when we see "()"
    """
    score = 0
    depth = 0
    
    for i in range(len(s)):
        if s[i] == '(':
            depth += 1
        else:
            depth -= 1
            # Check if this forms "()"
            if s[i-1] == '(':
                score += 2 ** depth
    
    return score


# Test cases
if __name__ == "__main__":
    print(f"Test 1: {scoreOfParentheses('()')}")          # Expected: 1
    print(f"Test 2: {scoreOfParentheses('(())')}")        # Expected: 2
    print(f"Test 3: {scoreOfParentheses('()()')}")        # Expected: 2
    print(f"Test 4: {scoreOfParentheses('(()(()))')}")    # Expected: 6
    print(f"Test 5: {scoreOfParentheses('(()())')}")      # Expected: 4
    print(f"Test 6: {scoreOfParentheses('((()))')}")      # Expected: 4

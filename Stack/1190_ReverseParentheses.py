"""
LeetCode #1190 - Reverse Substrings Between Each Pair of Parentheses
Topic: Stack
Difficulty: Medium

PROBLEM EXPLANATION:
Given a string with nested parentheses, reverse the strings in each pair
of matching parentheses, starting from the innermost one.

Example:
Input: s = "(abcd)"
Output: "dcba"

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: First reverse "love" -> "evol", then reverse "uevoli" -> "iloveu"

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: 
1. "oc" -> "co"
2. "etco" -> "octe"
3. "edocteel" -> "leetcode"

APPROACH (Stack):
1. Use stack to track characters and handle nesting
2. When we see '(': push current string to stack, start new string
3. When we see ')': reverse current string, pop from stack and append
4. Regular characters: add to current string

Time Complexity: O(n²) due to string reversal
Space Complexity: O(n)
"""

def reverseParentheses(s):
    """
    Returns string with parentheses content reversed
    """
    stack = []
    current = []
    
    for char in s:
        if char == '(':
            # Save current string and start new level
            stack.append(current)
            current = []
        elif char == ')':
            # Reverse current string
            current.reverse()
            # Pop previous level and append reversed string
            if stack:
                prev = stack.pop()
                current = prev + current
        else:
            # Regular character
            current.append(char)
    
    return ''.join(current)


# Test cases
if __name__ == "__main__":
    test1 = "(abcd)"
    print(f"Test 1: {reverseParentheses(test1)}")
    # Expected: "dcba"
    
    test2 = "(u(love)i)"
    print(f"Test 2: {reverseParentheses(test2)}")
    # Expected: "iloveu"
    
    test3 = "(ed(et(oc))el)"
    print(f"Test 3: {reverseParentheses(test3)}")
    # Expected: "leetcode"
    
    test4 = "a(bcdefghijkl(mno)p)q"
    print(f"Test 4: {reverseParentheses(test4)}")
    # Expected: "apmnolkjihgfedcbq"

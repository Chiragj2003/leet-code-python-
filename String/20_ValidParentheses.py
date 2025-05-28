"""
LeetCode #20 - Valid Parentheses (Enhanced)
Topic: String
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Check if string has valid matching brackets/parentheses.

Examples:
"()" -> True
"()[]{}" -> True
"(]" -> False
"([)]" -> False (wrong order)
"{[]}" -> True (properly nested)

Think of it like:
Opening brackets must be closed in the correct order.
Like nested boxes - you must close the inner box before the outer!

WHY THIS WORKS (Simple Explanation):
Use a STACK (Last In, First Out):
1. When you see opening bracket -> push to stack
2. When you see closing bracket -> it must match stack top!
3. At end, stack should be empty

Like Russian dolls - must close in reverse order of opening!

Time Complexity: O(n) - visit each character once
Space Complexity: O(n) - stack can hold all opening brackets
"""

def isValid(s):
    """
    Check if parentheses are valid
    
    Visual walkthrough for "{[]}":
    
    '{': stack = ['{']
    '[': stack = ['{', '[']
    ']': matches '[', pop -> stack = ['{']
    '}': matches '{', pop -> stack = []
    
    Stack empty at end -> Valid! ✓
    
    Visual walkthrough for "([)]":
    
    '(': stack = ['(']
    '[': stack = ['(', '[']
    ')': expected ']' but got ')' -> Invalid! ✗
    """
    # Stack to keep track of opening brackets
    stack = []
    
    # Mapping of closing to opening brackets
    closing_to_opening = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    for char in s:
        if char in closing_to_opening:
            # Closing bracket
            # Check if it matches stack top
            if not stack or stack[-1] != closing_to_opening[char]:
                return False
            stack.pop()
        else:
            # Opening bracket - push to stack
            stack.append(char)
    
    # Valid only if stack is empty
    return len(stack) == 0


def isValid_verbose(s):
    """
    Same logic with detailed comments for learning
    """
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for i, char in enumerate(s):
        if char in pairs:
            # This is a closing bracket
            if not stack:
                # No opening bracket to match
                print(f"Position {i}: Found '{char}' but stack is empty")
                return False
            
            if stack[-1] != pairs[char]:
                # Wrong type of opening bracket
                print(f"Position {i}: Expected '{pairs[char]}' but found '{stack[-1]}'")
                return False
            
            # Match found!
            stack.pop()
            print(f"Position {i}: Matched '{char}' with '{pairs[char]}'")
        else:
            # This is an opening bracket
            stack.append(char)
            print(f"Position {i}: Added opening '{char}' to stack")
    
    if stack:
        print(f"Unmatched opening brackets remaining: {stack}")
        return False
    
    print("All brackets matched!")
    return True


# Test cases with detailed output
if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("((", False),
        ("))", False),
        ("()[]", True),
    ]
    
    print("=== Testing Standard Solution ===")
    for s, expected in test_cases:
        result = isValid(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: '{s}' -> {result} (Expected: {expected})")
    
    print("\n=== Testing Verbose Solution (Example) ===")
    print("Input: '([)]'")
    result = isValid_verbose("([)]")
    print(f"Result: {result}\n")
    
    print("Input: '{[]}'")
    result = isValid_verbose("{[]}")
    print(f"Result: {result}")

"""

                 LeetCode #20 - Valid Parentheses                             
                 Topic: String/Stack | Difficulty: Easy                       
                 Company: Amazon, Microsoft, Google                           


PROBLEM: Check if string has valid matching brackets.

Examples:
  "()"  True
  "()[]{}"  True
  "(]"  False
  "([)]"  False
"""

#  SOLUTION 1: Stack (OPTIMAL)
def isValid(s):
    """
    Use stack for bracket matching
    Time: O(n), Space: O(n)
    
    Key: Opening brackets push, closing brackets must match stack top.
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:  # Closing bracket
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:  # Opening bracket
            stack.append(char)
    
    return len(stack) == 0


#  SOLUTION 2: Replace Method
def isValid_replace(s):
    """
    Repeatedly remove matching pairs
    Time: O(n), Space: O(n)
    
    Less efficient but intuitive approach.
    """
    while '()' in s or '{}' in s or '[]' in s:
        s = s.replace('()', '').replace('{}', '').replace('[]', '')
    return s == ''


#  SOLUTION 3: Counter-based (for single bracket type)
def isValid_simple(s):
    """
    Simple counter - works only for single bracket type
    Time: O(n), Space: O(1)
    
    Educational: shows limitation of naive approach.
    """
    if len(s) % 2 != 0:
        return False
    
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return False
    
    return count == 0


if __name__ == "__main__":
    print("Testing Valid Parentheses:\n")
    
    tests = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True)
    ]
    
    for s, expected in tests:
        r1 = isValid(s)
        r2 = isValid_replace(s)
        
        print(f'"{s}": Stack={r1} Replace={r2} (exp={expected}) {"" if r1 == expected else ""}')

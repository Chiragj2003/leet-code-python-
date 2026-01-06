"""

                 LeetCode #125 - Valid Palindrome                             
                 Topic: String/Two Pointers | Difficulty: Easy                
                 Company: Meta, Amazon, Microsoft                             


PROBLEM: Check if string is palindrome (alphanumeric only, case-insensitive).

Examples:
  "A man, a plan, a canal: Panama"  True
  "race a car"  False
"""

#  SOLUTION 1: Two Pointers (OPTIMAL)
def isPalindrome(s):
    """
    Two pointers from both ends
    Time: O(n), Space: O(1)
    
    Skip non-alphanumeric, compare case-insensitive.
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


#  SOLUTION 2: Filter and Reverse
def isPalindrome_filter(s):
    """
    Filter then compare with reverse
    Time: O(n), Space: O(n)
    
    More Pythonic but uses extra space.
    """
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


#  SOLUTION 3: Recursive
def isPalindrome_recursive(s):
    """
    Recursive two-pointer approach
    Time: O(n), Space: O(n) stack
    
    Educational: shows recursion pattern.
    """
    def helper(left, right):
        if left >= right:
            return True
        
        # Skip non-alphanumeric
        if not s[left].isalnum():
            return helper(left + 1, right)
        if not s[right].isalnum():
            return helper(left, right - 1)
        
        # Compare
        if s[left].lower() != s[right].lower():
            return False
        
        return helper(left + 1, right - 1)
    
    return helper(0, len(s) - 1)


if __name__ == "__main__":
    print("Testing Valid Palindrome:\n")
    
    tests = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("a", True)
    ]
    
    for s, expected in tests:
        r1 = isPalindrome(s)
        r2 = isPalindrome_filter(s)
        r3 = isPalindrome_recursive(s)
        
        print(f'"{s}": TwoPtr={r1} Filter={r2} Recursive={r3} (exp={expected}) {"" if r1 == expected else ""}')

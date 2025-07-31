"""
LeetCode #125 - Valid Palindrome
Topic: String / Two Pointers
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Check if a string is a palindrome, considering only alphanumeric characters
and ignoring case.

Example:
"A man, a plan, a canal: Panama" -> True
"race a car" -> False

Think of it like:
Ignore spaces and punctuation, only look at letters and numbers.
Does it read the same forwards and backwards?

WHY THIS WORKS (Simple Explanation):
Use two pointers from both ends:
1. Skip non-alphanumeric characters
2. Compare characters (case-insensitive)
3. If all match -> palindrome!

Like checking if a word is the same in a mirror!

Time Complexity: O(n) - visit each character once
Space Complexity: O(1) - only two pointers
"""

def isPalindrome(s):
    """
    Check if string is palindrome (alphanumeric only, case-insensitive)
    
    Visual example for "A man, a plan, a canal: Panama":
    
    Clean version: "amanaplanacanalpanama"
    
    left=0 'a', right=20 'a' ✓ match
    left=1 'm', right=19 'm' ✓ match
    left=2 'a', right=18 'a' ✓ match
    ...continue until pointers meet
    """
    # Two pointers from both ends
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


def isPalindrome_clean(s):
    """
    Alternative: Clean string first, then check
    
    Easier to understand but uses O(n) extra space
    """
    # Remove non-alphanumeric and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if cleaned string equals its reverse
    return cleaned == cleaned[::-1]


def isPalindrome_verbose(s):
    """
    Verbose version with detailed output for learning
    """
    left, right = 0, len(s) - 1
    
    print(f"Checking: '{s}'")
    
    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            print(f"  Skipping '{s[left]}' at position {left}")
            left += 1
        
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            print(f"  Skipping '{s[right]}' at position {right}")
            right -= 1
        
        # Compare
        left_char = s[left].lower()
        right_char = s[right].lower()
        
        print(f"  Comparing: '{left_char}' (pos {left}) with '{right_char}' (pos {right})")
        
        if left_char != right_char:
            print(f"  Mismatch! Not a palindrome.")
            return False
        
        left += 1
        right -= 1
    
    print(f"  All characters match! It's a palindrome.")
    return True


# Test cases with explanations
if __name__ == "__main__":
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),  # Empty after cleaning
        ("a", True),
        ("ab", False),
        ("aba", True),
        (".,", True),  # Empty after cleaning
        ("0P", False),
    ]
    
    print("=== Testing Two-Pointer Solution ===")
    for s, expected in test_cases:
        result = isPalindrome(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{s}' -> {result} (Expected: {expected})")
    
    print("\n=== Testing Clean-First Solution ===")
    for s, expected in test_cases:
        result = isPalindrome_clean(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{s}' -> {result} (Expected: {expected})")
    
    print("\n=== Verbose Example ===")
    isPalindrome_verbose("A man, a plan, a canal: Panama")
    print()
    isPalindrome_verbose("race a car")

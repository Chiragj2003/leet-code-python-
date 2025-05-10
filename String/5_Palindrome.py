"""
LeetCode #5 - Longest Palindromic Substring
Topic: String
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Find the longest substring that reads same forwards and backwards.

Example:
"babad" -> "bab" or "aba" (both length 3)
"cbbd" -> "bb" (length 2)

Think of it like:
A palindrome is like a mirror - same on both sides.
"racecar" reads same left-to-right and right-to-left!

WHY THIS WORKS (Simple Explanation):
Try every possible CENTER of a palindrome:
1. For each position, expand outward while characters match
2. Check BOTH odd-length ("aba") and even-length ("abba") palindromes
3. Track the longest one found

Like dropping a pebble in water - ripples expand equally!

Time Complexity: O(n²) - for each center, expand up to n times
Space Complexity: O(1) - only storing indices
"""

def longestPalindrome(s):
    """
    Find longest palindromic substring
    
    Visual example for "babad":
    
    Center at 'b' (index 0): "b" (length 1)
    Center at 'a' (index 1): expand -> "bab" (length 3) ✓
    Center at 'b' (index 2): "b" (length 1)
    Center at 'a' (index 3): expand -> "aba" (length 3) ✓
    Center at 'd' (index 4): "d" (length 1)
    
    Also check between characters:
    Between b,a: "ba" not palindrome
    Between a,b: "ab" not palindrome
    ...
    """
    if not s:
        return ""
    
    start = 0  # Start index of longest palindrome
    max_len = 0  # Length of longest palindrome
    
    def expandAroundCenter(left, right):
        """
        Expand while characters match
        Returns length of palindrome
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return length of palindrome
        return right - left - 1
    
    # Try each position as center
    for i in range(len(s)):
        # Odd length palindrome (single character center)
        len1 = expandAroundCenter(i, i)
        
        # Even length palindrome (between two characters)
        len2 = expandAroundCenter(i, i + 1)
        
        # Get maximum length
        current_len = max(len1, len2)
        
        # Update if longer palindrome found
        if current_len > max_len:
            max_len = current_len
            # Calculate start position
            start = i - (current_len - 1) // 2
    
    return s[start:start + max_len]


def longestPalindrome_dp(s):
    """
    Alternative: Dynamic Programming approach
    
    dp[i][j] = True if s[i:j+1] is palindrome
    
    Build up from smaller substrings:
    1. Single characters are palindromes
    2. Two same characters are palindromes
    3. Longer: if s[i]==s[j] and s[i+1:j] is palindrome
    
    Time: O(n²), Space: O(n²)
    """
    n = len(s)
    if n == 0:
        return ""
    
    # dp[i][j] = is substring from i to j a palindrome?
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1
    
    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True
    
    # Check two-character substrings
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2
    
    # Check longer substrings
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # Check if s[i:j+1] is palindrome
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_len = length
    
    return s[start:start + max_len]


# Test cases with visual explanations
if __name__ == "__main__":
    test_cases = [
        ("babad", ["bab", "aba"]),  # Either is valid
        ("cbbd", ["bb"]),
        ("a", ["a"]),
        ("ac", ["a", "c"]),  # Both single chars
        ("racecar", ["racecar"]),
        ("noon", ["noon"]),
    ]
    
    print("=== Testing Expand Around Center Solution ===")
    for s, expected in test_cases:
        result = longestPalindrome(s)
        is_valid = result in expected
        status = "✓" if is_valid else "✗"
        print(f"{status} Input: '{s}'")
        print(f"   Output: '{result}'")
        print(f"   Valid answers: {expected}")
        print()
    
    print("=== Testing Dynamic Programming Solution ===")
    for s, expected in test_cases:
        result = longestPalindrome_dp(s)
        is_valid = result in expected
        status = "✓" if is_valid else "✗"
        print(f"{status} Input: '{s}'")
        print(f"   Output: '{result}'")
        print(f"   Valid answers: {expected}")
        print()

"""

                LeetCode #5 - Longest Palindromic Substring                   
                Topic: String | Difficulty: Medium                            
                Company: Amazon, Meta, Microsoft                              


PROBLEM: Find the longest substring that reads the same forwards and backwards.

Examples:
  "babad"  "bab" or "aba" (length 3)
  "cbbd"  "bb" (length 2)
"""

#  SOLUTION 1: Expand Around Centers (OPTIMAL for interview)
def longestPalindrome(s):
    """
    Expand from each possible center
    Time: O(n), Space: O(1)
    
    Intuition: A palindrome mirrors around center.
    Check both odd-length (single center) and even-length (two centers).
    """
    if not s:
        return ""
    
    def expand_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1  # Adjust to valid range
    
    start, end = 0, 0
    
    for i in range(len(s)):
        # Odd-length palindrome (center is single char)
        l1, r1 = expand_center(i, i)
        # Even-length palindrome (center is between chars)
        l2, r2 = expand_center(i, i + 1)
        
        # Track longest
        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2
    
    return s[start:end + 1]


#  SOLUTION 2: Dynamic Programming
def longestPalindrome_dp(s):
    """
    DP table approach
    Time: O(n), Space: O(n)
    
    dp[i][j] = True if s[i:j+1] is palindrome
    
    Build from smaller to larger substrings.
    """
    if not s:
        return ""
    
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start, max_len = 0, 1
    
    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Check 2-character substrings
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start, max_len = i, 2
    
    # Check substrings of length 3+
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start, max_len = i, length
    
    return s[start:start + max_len]


#  SOLUTION 3: Manacher's Algorithm (OPTIMAL time)
def longestPalindrome_manacher(s):
    """
    Manacher's algorithm - linear time
    Time: O(n), Space: O(n)
    
    Advanced: Uses preprocessed string with separators.
    Interview: Usually expand-centers is sufficient.
    """
    # Preprocess: insert '#' between chars
    # "babad"  "#b#a#b#a#d#"
    t = '#'.join('^{}$'.format(s))
    n = len(t)
    p = [0] * n  # p[i] = radius of palindrome at i
    center, right = 0, 0
    
    for i in range(1, n - 1):
        # Mirror of i with respect to center
        mirror = 2 * center - i
        
        if i < right:
            p[i] = min(right - i, p[mirror])
        
        # Expand around i
        while t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1
        
        # Update center if expanded past right
        if i + p[i] > right:
            center, right = i, i + p[i]
    
    # Find longest palindrome
    max_len, center_idx = max((n, i) for i, n in enumerate(p))
    start = (center_idx - max_len) // 2
    return s[start:start + max_len]


if __name__ == "__main__":
    print("Testing Longest Palindromic Substring:\n")
    
    tests = [
        ("babad", ["bab", "aba"]),
        ("cbbd", ["bb"]),
        ("a", ["a"]),
        ("ac", ["a", "c"])
    ]
    
    for s, expected in tests:
        r1 = longestPalindrome(s)
        r2 = longestPalindrome_dp(s)
        r3 = longestPalindrome_manacher(s)
        
        check1 = r1 in expected
        check2 = r2 in expected
        check3 = r3 in expected
        
        print(f'"{s}": Expand={r1} DP={r2} Manacher={r3}')
        print(f'  Expected: {expected} - {"" if all([check1, check2, check3]) else ""}\n')

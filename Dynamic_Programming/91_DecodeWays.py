"""
LeetCode #91 - Decode Ways
Topic: Dynamic Programming / String
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Decode string where A=1, B=2, ..., Z=26

Example:
"12" -> 2 ways ("AB" or "L")
"226" -> 3 ways ("BZ", "VF", "BBF")

Think of it like:
Reading numbers as letters - how many valid readings?

WHY THIS WORKS (Simple Explanation):
At each position, check:
- Can decode as single digit (1-9)?
- Can decode with previous as two digits (10-26)?

dp[i] = ways to decode s[0:i]

Time: O(n)
Space: O(n), can optimize to O(1)
"""

def numDecodings(s):
    """Count decode ways"""
    if not s or s[0] == '0':
        return 0
    
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # Empty string
    dp[1] = 1  # First char (already checked not 0)
    
    for i in range(2, n + 1):
        # Single digit decode
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        
        # Two digit decode
        two_digit = int(s[i-2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i-2]
    
    return dp[n]


# Test
if __name__ == "__main__":
    tests = [
        ("12", 2),
        ("226", 3),
        ("06", 0),
    ]
    
    for s, exp in tests:
        result = numDecodings(s)
        print(f'"{s}" -> {result} ways (expected {exp})')

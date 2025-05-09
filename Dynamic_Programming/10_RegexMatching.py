"""
LeetCode #10 - Regular Expression Matching
Topic: Dynamic Programming / String
Difficulty: Hard

PROBLEM EXPLANATION (Easy Terms):
Match string with pattern containing '.' and '*'.
'.' matches any character
'*' matches zero or more of previous character

Example:
"aa" with "a*" -> True
"ab" with ".*" -> True

Think of it like:
Regex pattern matching!

WHY THIS WORKS:
DP table where dp[i][j] = does s[0:i] match p[0:j]

Time: O(m × n)
Space: O(m × n)
"""

def isMatch(s, p):
    """Regular expression matching"""
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    
    # Handle patterns like a*, a*b*, etc.
    for j in range(2, n + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j-1] == '*':
                # Zero occurrences OR one+ occurrences
                dp[i][j] = dp[i][j-2] or \
                          (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
            elif p[j-1] == '.' or s[i-1] == p[j-1]:
                dp[i][j] = dp[i-1][j-1]
    
    return dp[m][n]


# Test
if __name__ == "__main__":
    tests = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
    ]
    
    for s, p, exp in tests:
        result = isMatch(s, p)
        print(f'"{s}" matches "{p}": {result} (expected {exp})')

"""
LeetCode #72 - Edit Distance
Topic: Dynamic Programming / String
Difficulty: Hard

PROBLEM EXPLANATION (Easy Terms):
Minimum operations to convert word1 to word2.
Operations: insert, delete, replace

Example:
"horse" -> "ros" = 3 operations
(replace 'h'->'r', remove 'r', remove 'e')

Think of it like:
Spell checker corrections!

WHY THIS WORKS (Simple Explanation):
DP table where dp[i][j] = min ops to convert s1[0:i] to s2[0:j]

If chars match: dp[i][j] = dp[i-1][j-1]
Else: 1 + min(insert, delete, replace)

Time: O(m × n)
Space: O(m × n)
"""

def minDistance(word1, word2):
    """Minimum edit distance"""
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # delete
                    dp[i][j-1],    # insert
                    dp[i-1][j-1]   # replace
                )
    
    return dp[m][n]


# Test
if __name__ == "__main__":
    tests = [
        ("horse", "ros", 3),
        ("intention", "execution", 5),
    ]
    
    for w1, w2, exp in tests:
        result = minDistance(w1, w2)
        print(f'"{w1}" -> "{w2}": {result} ops (expected {exp})')

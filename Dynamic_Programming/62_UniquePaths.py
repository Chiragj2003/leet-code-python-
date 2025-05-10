"""
LeetCode #62 - Unique Paths
Topic: Dynamic Programming
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Robot at top-left of m×n grid.
Can only move right or down.
How many unique paths to bottom-right?

Example (3×7 grid): 28 paths

Think of it like:
Walking on city blocks - only east or south allowed!

WHY THIS WORKS (Simple Explanation):
Each cell: paths = paths from left + paths from top

dp[i][j] = dp[i-1][j] + dp[i][j-1]

Build from top-left to bottom-right!

Time: O(m×n)
Space: O(m×n), can optimize to O(n)
"""

def uniquePaths(m, n):
    """Count unique paths"""
    # DP table
    dp = [[1] * n for _ in range(m)]
    
    # Fill table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]


def uniquePaths_optimized(m, n):
    """Space optimized - use single row"""
    dp = [1] * n
    
    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]
    
    return dp[n-1]


# Test
if __name__ == "__main__":
    tests = [(3,7,28), (3,2,3), (7,3,28)]
    
    for m, n, exp in tests:
        result = uniquePaths(m, n)
        print(f"Grid {m}×{n}: {result} paths (expected {exp})")

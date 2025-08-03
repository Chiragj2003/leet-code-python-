"""
LeetCode #96 - Unique Binary Search Trees
Topic: Dynamic Programming / Tree
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Count structurally unique BSTs with n nodes (1 to n).

Example:
n=3 -> 5 unique BSTs

Think of it like:
How many different BST shapes possible?

WHY THIS WORKS (Catalan Number):
For each root i:
- Left subtree: i-1 nodes
- Right subtree: n-i nodes
dp[n] = sum of dp[i-1] × dp[n-i] for i=1 to n

Time: O(n²)
Space: O(n)
"""

def numTrees(n):
    """Count unique BSTs"""
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    
    for nodes in range(2, n + 1):
        for root in range(1, nodes + 1):
            left = root - 1
            right = nodes - root
            dp[nodes] += dp[left] * dp[right]
    
    return dp[n]


# Test
if __name__ == "__main__":
    for n in range(1, 5):
        result = numTrees(n)
        print(f"n={n}: {result} unique BSTs")

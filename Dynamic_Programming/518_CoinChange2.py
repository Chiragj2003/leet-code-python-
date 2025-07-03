"""
LeetCode #152 already exists - this is #518 - Coin Change 2
Topic: Dynamic Programming
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Count ways to make amount using coins.
(Combinations, not permutations)

Example:
amount = 5, coins = [1,2,5]
-> 4 ways ([5], [2,2,1], [2,1,1,1], [1,1,1,1,1])

Think of it like:
How many ways to make change?

WHY THIS WORKS:
DP: dp[i] = ways to make amount i
For each coin, update all reachable amounts.

Time: O(n × amount)
Space: O(amount)
"""

def change(amount, coins):
    """Count ways to make change"""
    dp = [0] * (amount + 1)
    dp[0] = 1  # One way to make 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    return dp[amount]


# Test
if __name__ == "__main__":
    result = change(5, [1,2,5])
    print(f"Ways to make change: {result}")

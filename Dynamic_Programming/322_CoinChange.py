"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #322 - Coin Change                                ║
║                    Topic: Dynamic Programming                                ║
║                    Difficulty: Medium                                         ║
║                    Company: Amazon, Meta, Uber                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Given coins of different denominations and total amount,
find MINIMUM number of coins needed to make that amount.
Return -1 if impossible.

EXAMPLES:
─────────
✓ Input: coins = [1,2,5], amount = 11 → Output: 3
  Explanation: 11 = 5 + 5 + 1 (3 coins)

✓ Input: coins = [2], amount = 3 → Output: -1
  Explanation: Cannot make 3 with only 2's

✓ Input: coins = [1], amount = 0 → Output: 0

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
💰 Making change: You have coins [1¢, 5¢, 10¢, 25¢].
   Need to make 37¢ with fewest coins.
   Best: 25¢ + 10¢ + 1¢ + 1¢ = 4 coins

🎯 Minimum moves: Each coin type is a "jump size".
   Reach target with minimum jumps!

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   Amazon payment: optimize transaction with minimum
   denomination breakdown for lower processing fees.

📌 TASK:
   Find minimum coins to make amount.
   Time O(amount × coins), Space O(amount).

📌 ACTION:
   Bottom-up DP:
   - dp[i] = min coins to make amount i
   - For each amount, try all coins

📌 RESULT:
   ✓ Time: O(S × n) where S=amount, n=coins
   ✓ Space: O(S) for DP array
   ✓ Minimum coins found

"""

# ═══════════════════════════════════════════════════════════════════════════
# 💡 BRUTE FORCE - Recursion (Exponential!)
# ═══════════════════════════════════════════════════════════════════════════
def coinChange_bruteforce(coins, amount):
    """
    Try all combinations recursively
    
    Time: O(S^n) - exponential!
    Space: O(n) recursion
    """
    def minCoins(remaining):
        if remaining == 0:
            return 0
        if remaining < 0:
            return float('inf')
        
        min_count = float('inf')
        for coin in coins:
            result = minCoins(remaining - coin)
            if result != float('inf'):
                min_count = min(min_count, result + 1)
        
        return min_count
    
    result = minCoins(amount)
    return result if result != float('inf') else -1


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Bottom-Up DP
# ═══════════════════════════════════════════════════════════════════════════
def coinChange(coins, amount):
    """
    Bottom-up DP
    
    dp[i] = minimum coins to make amount i
    
    Example: coins = [1,2,5], amount = 11
    ────────
    dp[0] = 0 (base case: 0 coins for amount 0)
    
    For amount 1:
      Try coin 1: dp[1-1] + 1 = 0 + 1 = 1
      dp[1] = 1
    
    For amount 2:
      Try coin 1: dp[2-1] + 1 = 1 + 1 = 2
      Try coin 2: dp[2-2] + 1 = 0 + 1 = 1
      dp[2] = min(2, 1) = 1
    
    For amount 5:
      Try coin 1: dp[4] + 1 = 2 + 1 = 3
      Try coin 2: dp[3] + 1 = 2 + 1 = 3
      Try coin 5: dp[0] + 1 = 0 + 1 = 1
      dp[5] = min(3, 3, 1) = 1
    
    ...continue until dp[11] = 3
    """
    # Initialize dp array with infinity
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case
    
    # Build up solutions for each amount
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE - Top-Down Memoization
# ═══════════════════════════════════════════════════════════════════════════
def coinChange_memo(coins, amount):
    """
    Top-down with memoization
    
    Time: O(S × n)
    Space: O(S)
    """
    memo = {}
    
    def minCoins(remaining):
        if remaining == 0:
            return 0
        if remaining < 0:
            return float('inf')
        if remaining in memo:
            return memo[remaining]
        
        min_count = float('inf')
        for coin in coins:
            result = minCoins(remaining - coin)
            if result != float('inf'):
                min_count = min(min_count, result + 1)
        
        memo[remaining] = min_count
        return min_count
    
    result = minCoins(amount)
    return result if result != float('inf') else -1


# ═══════════════════════════════════════════════════════════════════════════
# 📊 COMPLEXITY COMPARISON
# ═══════════════════════════════════════════════════════════════════════════
"""
╔════════════════╦════════════╦═══════════╦═════════════════════════╗
║   Approach     ║    Time    ║   Space   ║       Notes             ║
╠════════════════╬════════════╬═══════════╬═════════════════════════╣
║ Brute Force    ║  O(S^n)    ║   O(n)    ║ Too slow!               ║
║ Memoization    ║  O(S×n)    ║   O(S)    ║ Top-down DP             ║
║ Bottom-Up DP   ║  O(S×n)    ║   O(S)    ║ Optimal, iterative      ║
╚════════════════╩════════════╩═══════════╩═════════════════════════╝

S = amount, n = number of coins
"""


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
        ([1, 2, 5], 100, 20),
    ]
    
    print("=" * 70)
    print("🧪 TESTING COIN CHANGE")
    print("=" * 70)
    
    for coins, amount, expected in test_cases:
        brute = coinChange_bruteforce(coins, amount) if amount < 20 else "Skipped"
        memo = coinChange_memo(coins, amount)
        optimal = coinChange(coins, amount)
        
        print(f"\nInput: coins = {coins}, amount = {amount}")
        print(f"Expected: {expected}")
        print(f"Brute: {brute}")
        print(f"Memo: {memo} {'✓' if memo == expected else '✗'}")
        print(f"Optimal: {optimal} {'✓' if optimal == expected else '✗'}")

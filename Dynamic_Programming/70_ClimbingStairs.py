"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #70 - Climbing Stairs                             ║
║                    Topic: Dynamic Programming                                ║
║                    Difficulty: Easy                                           ║
║                    Company: Amazon, Google, Adobe                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Climbing n stairs. Can take 1 or 2 steps at a time.
How many DISTINCT ways to reach the top?

EXAMPLES:
─────────
✓ Input: n = 2 → Output: 2
  Ways: (1+1) or (2)

✓ Input: n = 3 → Output: 3
  Ways: (1+1+1), (1+2), (2+1)

✓ Input: n = 4 → Output: 5
  Ways: (1+1+1+1), (1+1+2), (1+2+1), (2+1+1), (2+2)

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🪜 Staircase: You're at bottom. Each step, hop 1 or 2 stairs.
   How many different hopping patterns to reach top?

🎮 Video game: Jump 1 or 2 platforms. Count all paths!

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   Amazon delivery: driver can skip 1 or 2 houses.
   Calculate total route variations.

📌 TASK:
   Count ways to reach step n.
   Time O(n), Space O(1).

📌 ACTION:
   Dynamic programming - Fibonacci pattern:
   - ways[n] = ways[n-1] + ways[n-2]
   - To reach step n, come from n-1 or n-2

📌 RESULT:
   ✓ Time: O(n) single pass
   ✓ Space: O(1) with optimization
   ✓ Efficient path counting

"""

# ═══════════════════════════════════════════════════════════════════════════
# 💡 BRUTE FORCE - Recursion (Exponential!)
# ═══════════════════════════════════════════════════════════════════════════
def climbStairs_bruteforce(n):
    """
    Recursive: try all paths
    
    Time: O(2^n) - exponential!
    Space: O(n) - recursion depth
    """
    if n <= 2:
        return n
    
    return climbStairs_bruteforce(n - 1) + climbStairs_bruteforce(n - 2)


# ═══════════════════════════════════════════════════════════════════════════
# 📚 BETTER - Memoization (Top-Down DP)
# ═══════════════════════════════════════════════════════════════════════════
def climbStairs_memo(n):
    """
    Recursion with memoization
    
    Time: O(n)
    Space: O(n) - memo + recursion
    """
    memo = {}
    
    def climb(n):
        if n <= 2:
            return n
        if n in memo:
            return memo[n]
        
        memo[n] = climb(n - 1) + climb(n - 2)
        return memo[n]
    
    return climb(n)


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Bottom-Up DP
# ═══════════════════════════════════════════════════════════════════════════
def climbStairs(n):
    """
    Bottom-up dynamic programming (Fibonacci)
    
    Pattern: This is literally Fibonacci!
    F(1) = 1, F(2) = 2
    F(n) = F(n-1) + F(n-2)
    
    Example: n = 5
    ────────
    Step 1: ways = 1 (only 1 way: take 1 step)
    Step 2: ways = 2 (two ways: 1+1 or 2)
    Step 3: ways = 2+1 = 3
    Step 4: ways = 3+2 = 5
    Step 5: ways = 5+3 = 8
    
    Answer: 8 ways
    """
    if n <= 2:
        return n
    
    prev2 = 1  # ways to reach step 1
    prev1 = 2  # ways to reach step 2
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1


# ═══════════════════════════════════════════════════════════════════════════
# 🎯 ALTERNATIVE - DP Array
# ═══════════════════════════════════════════════════════════════════════════
def climbStairs_array(n):
    """
    DP with array (easier to understand)
    
    Time: O(n)
    Space: O(n)
    """
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


# ═══════════════════════════════════════════════════════════════════════════
# 📊 COMPLEXITY COMPARISON
# ═══════════════════════════════════════════════════════════════════════════
"""
╔════════════════╦════════════╦═══════════╦═════════════════════════╗
║   Approach     ║    Time    ║   Space   ║       Notes             ║
╠════════════════╬════════════╬═══════════╬═════════════════════════╣
║ Brute Force    ║   O(2^n)   ║   O(n)    ║ Too slow! TLE           ║
║ Memoization    ║   O(n)     ║   O(n)    ║ Top-down DP             ║
║ DP Array       ║   O(n)     ║   O(n)    ║ Bottom-up, clear        ║
║ Space Optimized║   O(n)     ║   O(1)    ║ Best solution           ║
╚════════════════╩════════════╩═══════════╩═════════════════════════╝

For n=45:
- Brute: 2^45 = 35 trillion operations (minutes!)
- DP: 45 operations (instant!)
"""


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [2, 3, 4, 5, 10]
    
    print("=" * 70)
    print("🧪 TESTING CLIMBING STAIRS")
    print("=" * 70)
    
    for n in test_cases:
        # Skip brute force for large n (too slow)
        brute = climbStairs_bruteforce(n) if n < 20 else "Skipped (too slow)"
        memo = climbStairs_memo(n)
        optimal = climbStairs(n)
        array = climbStairs_array(n)
        
        print(f"\nInput: n = {n}")
        print(f"Brute: {brute}")
        print(f"Memo: {memo}")
        print(f"Optimal: {optimal}")
        print(f"Array: {array}")

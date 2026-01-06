"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #198 - House Robber                               ║
║                    Topic: Dynamic Programming                                ║
║                    Difficulty: Medium                                         ║
║                    Company: Amazon, Meta, Google                             ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Rob houses along street. Each house has money.
CANNOT rob two adjacent houses (alarm triggers).
Maximize money stolen.

EXAMPLES:
─────────
✓ Input: [1,2,3,1] → Output: 4
  Rob house 0 (1) and house 2 (3) = 1+3 = 4

✓ Input: [2,7,9,3,1] → Output: 12
  Rob house 0 (2), house 2 (9), house 4 (1) = 2+9+1 = 12

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🏠 Houses: [🏠₁ 🏠₇ 🏠₉ 🏠₃ 🏠₁]
   Can't rob neighbors! Pick houses far apart.
   Best: 🏠₁ + 🏠₉ + 🏠₁ = 11 (wait, let's check 7+3+1=11 too!)
   Actually: 🏠₇ + 🏠₉ = 16 or 🏠₇ + 🏠₃ + 🏠₁ = 11
   Wait: 🏠₂ + 🏠₉ + 🏠₁ = 12! ✓

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   Amazon warehouses: select facilities to upgrade with budget.
   Adjacent facilities share systems, can't upgrade both.

📌 TASK:
   Maximize profit without selecting adjacent.
   Time O(n), Space O(1).

📌 ACTION:
   DP: At each house, choose max of:
   - Rob current + skip previous
   - Skip current, keep previous max

📌 RESULT:
   ✓ Time: O(n) single pass
   ✓ Space: O(1) optimized
   ✓ Maximum profit found

"""

# ═══════════════════════════════════════════════════════════════════════════
# 💡 BRUTE FORCE - Try All Combinations
# ═══════════════════════════════════════════════════════════════════════════
def rob_bruteforce(nums):
    """
    Recursion: for each house, rob or skip
    
    Time: O(2^n) - exponential
    Space: O(n) - recursion depth
    """
    def robFrom(index):
        if index >= len(nums):
            return 0
        
        # Rob current + skip next, or skip current
        return max(
            nums[index] + robFrom(index + 2),
            robFrom(index + 1)
        )
    
    return robFrom(0)


# ═══════════════════════════════════════════════════════════════════════════
# 📚 BETTER - Memoization
# ═══════════════════════════════════════════════════════════════════════════
def rob_memo(nums):
    """
    Top-down DP with memoization
    
    Time: O(n)
    Space: O(n)
    """
    memo = {}
    
    def robFrom(index):
        if index >= len(nums):
            return 0
        if index in memo:
            return memo[index]
        
        memo[index] = max(
            nums[index] + robFrom(index + 2),
            robFrom(index + 1)
        )
        return memo[index]
    
    return robFrom(0)


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Bottom-Up DP
# ═══════════════════════════════════════════════════════════════════════════
def rob(nums):
    """
    Bottom-up DP with O(1) space
    
    dp[i] = max(nums[i] + dp[i-2], dp[i-1])
    
    Meaning: At house i, choose:
    - Rob it + best from i-2
    - Skip it, keep best from i-1
    
    Example: [2,7,9,3,1]
    ────────
    House 0: rob = 2, skip = 0 → max = 2
    House 1: rob = 7, skip = 2 → max = 7
    House 2: rob = 9+2=11, skip = 7 → max = 11
    House 3: rob = 3+7=10, skip = 11 → max = 11
    House 4: rob = 1+11=12, skip = 11 → max = 12
    
    Answer: 12
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev2 = 0  # max money 2 houses ago
    prev1 = 0  # max money 1 house ago
    
    for num in nums:
        # Rob current + prev2, or skip current
        current = max(num + prev2, prev1)
        prev2 = prev1
        prev1 = current
    
    return prev1


# ═══════════════════════════════════════════════════════════════════════════
# 🎯 ALTERNATIVE - DP Array (Clearer)
# ═══════════════════════════════════════════════════════════════════════════
def rob_array(nums):
    """
    DP with array for clarity
    
    Time: O(n)
    Space: O(n)
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
    
    return dp[-1]


# ═══════════════════════════════════════════════════════════════════════════
# 📊 COMPLEXITY COMPARISON
# ═══════════════════════════════════════════════════════════════════════════
"""
╔════════════════╦════════════╦═══════════╦═════════════════════════╗
║   Approach     ║    Time    ║   Space   ║       Notes             ║
╠════════════════╬════════════╬═══════════╬═════════════════════════╣
║ Brute Force    ║   O(2^n)   ║   O(n)    ║ Too slow for n>20       ║
║ Memoization    ║   O(n)     ║   O(n)    ║ Top-down DP             ║
║ DP Array       ║   O(n)     ║   O(n)    ║ Easy to understand      ║
║ Space Optimized║   O(n)     ║   O(1)    ║ Best solution           ║
╚════════════════╩════════════╩═══════════╩═════════════════════════╝
"""


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([2, 1, 1, 2], 4),
        ([5], 5),
    ]
    
    print("=" * 70)
    print("🧪 TESTING HOUSE ROBBER")
    print("=" * 70)
    
    for nums, expected in test_cases:
        brute = rob_bruteforce(nums) if len(nums) < 15 else "Skipped"
        memo = rob_memo(nums)
        optimal = rob(nums)
        array = rob_array(nums)
        
        print(f"\nInput: {nums}")
        print(f"Expected: {expected}")
        print(f"Brute: {brute}")
        print(f"Memo: {memo} {'✓' if memo == expected else '✗'}")
        print(f"Optimal: {optimal} {'✓' if optimal == expected else '✗'}")
        print(f"Array: {array} {'✓' if array == expected else '✗'}")

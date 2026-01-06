"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #300 - Longest Increasing Subsequence             ║
║                    Topic: Dynamic Programming                                ║
║                    Difficulty: Medium                                         ║
║                    Company: Amazon, Microsoft, Meta                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Find length of longest strictly increasing subsequence.
Subsequence: maintain relative order, don't need consecutive.

EXAMPLES:
─────────
✓ Input: [10,9,2,5,3,7,101,18] → Output: 4
  Subsequence: [2,3,7,101] or [2,5,7,101]

✓ Input: [0,1,0,3,2,3] → Output: 4
  Subsequence: [0,1,2,3]

✓ Input: [7,7,7,7] → Output: 1

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
📈 Stock prices: [10,9,2,5,3,7,101,18]
   Find longest period of increasing prices.
   Days 3→5→8 (prices 2→5→7→101) = 4 days!

🎯 High scores: Select games where score keeps increasing.
   [2,5,7,101] increases continuously!

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   Amazon metrics: find longest streak of improving
   performance metrics over time.

📌 TASK:
   Find length of longest increasing subsequence.
   Time O(n²) DP or O(n log n) binary search.

📌 ACTION:
   DP approach:
   - dp[i] = length of LIS ending at i
   - Check all previous elements

📌 RESULT:
   ✓ Time: O(n²) DP or O(n log n) optimized
   ✓ Space: O(n)
   ✓ Longest sequence found

"""

# ═══════════════════════════════════════════════════════════════════════════
# 💡 BRUTE FORCE - Try All Subsequences
# ═══════════════════════════════════════════════════════════════════════════
def lengthOfLIS_bruteforce(nums):
    """
    Generate all subsequences, check which are increasing
    
    Time: O(2^n) - exponential!
    Space: O(n)
    """
    def lis(index, prev):
        if index == len(nums):
            return 0
        
        # Skip current
        skip = lis(index + 1, prev)
        
        # Take current if valid
        take = 0
        if prev == -1 or nums[index] > nums[prev]:
            take = 1 + lis(index + 1, index)
        
        return max(skip, take)
    
    return lis(0, -1)


# ═══════════════════════════════════════════════════════════════════════════
# 📚 BETTER - Dynamic Programming O(n²)
# ═══════════════════════════════════════════════════════════════════════════
def lengthOfLIS(nums):
    """
    Bottom-up DP
    
    dp[i] = length of LIS ending at index i
    
    Example: [10,9,2,5,3,7,101,18]
    ────────
    dp[0] = 1 (just 10)
    dp[1] = 1 (just 9, can't extend from 10)
    dp[2] = 1 (just 2)
    dp[3] = 2 (2→5)
    dp[4] = 2 (2→3)
    dp[5] = 3 (2→3→7 or 2→5→7)
    dp[6] = 4 (2→3→7→101 or 2→5→7→101)
    dp[7] = 4 (2→3→7→18)
    
    Max = 4
    """
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n  # Each element is LIS of length 1
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Binary Search O(n log n)
# ═══════════════════════════════════════════════════════════════════════════
def lengthOfLIS_optimal(nums):
    """
    Binary search approach
    
    Maintain array of smallest tail values for each length
    
    Time: O(n log n)
    Space: O(n)
    """
    import bisect
    
    tails = []
    
    for num in nums:
        # Find position to insert/replace
        pos = bisect.bisect_left(tails, num)
        
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    
    return len(tails)


# ═══════════════════════════════════════════════════════════════════════════
# 📊 COMPLEXITY COMPARISON
# ═══════════════════════════════════════════════════════════════════════════
"""
╔════════════════╦════════════╦═══════════╦═════════════════════════╗
║   Approach     ║    Time    ║   Space   ║       Notes             ║
╠════════════════╬════════════╬═══════════╬═════════════════════════╣
║ Brute Force    ║   O(2^n)   ║   O(n)    ║ Try all subsequences    ║
║ DP             ║   O(n²)    ║   O(n)    ║ Standard solution       ║
║ Binary Search  ║ O(n log n) ║   O(n)    ║ Optimal                 ║
╚════════════════╩════════════╩═══════════╩═════════════════════════╝
"""


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
    ]
    
    print("=" * 70)
    print("🧪 TESTING LONGEST INCREASING SUBSEQUENCE")
    print("=" * 70)
    
    for nums, expected in test_cases:
        brute = lengthOfLIS_bruteforce(nums) if len(nums) < 15 else "Skipped"
        dp = lengthOfLIS(nums)
        optimal = lengthOfLIS_optimal(nums)
        
        print(f"\nInput: {nums}")
        print(f"Expected: {expected}")
        print(f"Brute: {brute}")
        print(f"DP O(n²): {dp} {'✓' if dp == expected else '✗'}")
        print(f"Binary O(n log n): {optimal} {'✓' if optimal == expected else '✗'}")

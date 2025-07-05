"""
LeetCode #322 already exists - this is #377 - Combination Sum IV
Topic: Dynamic Programming
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Count number of combinations that add up to target.
Order matters! (permutations)

Example:
nums = [1,2,3], target = 4
-> 7 ways ([1,1,1,1],[1,1,2],[1,2,1],[1,3],[2,1,1],[2,2],[3,1])

Think of it like:
Climbing stairs with variable steps!

WHY THIS WORKS:
DP: dp[i] = sum of dp[i-num] for all nums

Time: O(target × n)
Space: O(target)
"""

def combinationSum4(nums, target):
    """Count combinations (order matters)"""
    dp = [0] * (target + 1)
    dp[0] = 1  # One way to make 0
    
    for i in range(1, target + 1):
        for num in nums:
            if i >= num:
                dp[i] += dp[i - num]
    
    return dp[target]


# Test
if __name__ == "__main__":
    result = combinationSum4([1,2,3], 4)
    print(f"Combinations: {result}")

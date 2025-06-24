"""
LeetCode #416 - Partition Equal Subset Sum
Topic: Dynamic Programming
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Can you partition array into two subsets with equal sum?

Example:
[1,5,11,5] -> True ([1,5,5] and [11])
[1,2,3,5] -> False

Think of it like:
Splitting items into two groups with same total weight!

WHY THIS WORKS (Simple Explanation):
If total sum is odd, impossible!
If even, find subset with sum = total/2

This becomes 0/1 Knapsack problem!

Time: O(n × sum)
Space: O(sum)
"""

def canPartition(nums):
    """Check if can partition into equal sum subsets"""
    total = sum(nums)
    
    # If odd, can't split equally
    if total % 2 != 0:
        return False
    
    target = total // 2
    
    # DP: can we make sum = target?
    dp = [False] * (target + 1)
    dp[0] = True  # Can make sum 0
    
    for num in nums:
        # Traverse backwards to avoid using same number twice
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]


# Test
if __name__ == "__main__":
    tests = [
        ([1,5,11,5], True),
        ([1,2,3,5], False),
    ]
    
    for nums, exp in tests:
        result = canPartition(nums)
        print(f"{nums} -> {result} (expected {exp})")

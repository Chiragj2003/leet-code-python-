"""
LeetCode #198 - House Robber
Topic: Dynamic Programming
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
You're a robber planning to rob houses along a street.
Each house has money, but you CAN'T rob two adjacent houses
(security system connects adjacent houses).

Find maximum money you can rob without alerting police.

Example:
[1,2,3,1] -> Rob house 1 and 3: 1+3 = 4
[2,7,9,3,1] -> Rob 0,2,4: 2+9+1 = 12

Think of it like:
Picking numbers from a line where you can't pick adjacent ones.
What's the maximum sum?

WHY THIS WORKS (Simple Explanation):
At each house, you have two choices:
1. Rob this house + money from (i-2)th house
2. Don't rob, keep money from (i-1)th house

Choose the maximum!

Formula: dp[i] = max(nums[i] + dp[i-2], dp[i-1])

Time Complexity: O(n)
Space Complexity: O(1) with optimization
"""

def rob(nums):
    """
    Find maximum money to rob using dynamic programming
    
    Visual example: [2, 7, 9, 3, 1]
    
    House 0 (2): Rob it! Total = 2
    House 1 (7): Rob it! (7 > 2) Total = 7
    House 2 (9): Rob 2+9=11 or skip 7? -> 11 is better
    House 3 (3): Rob 7+3=10 or skip 11? -> 11 is better
    House 4 (1): Rob 11+1=12 or skip 11? -> 12 is better
    
    Result: 12 (rob houses 0, 2, 4)
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    # Track last two values only (space optimized)
    prev2 = nums[0]  # Max money up to house i-2
    prev1 = max(nums[0], nums[1])  # Max money up to house i-1
    
    for i in range(2, len(nums)):
        # Either rob current + prev2, or skip current
        current = max(nums[i] + prev2, prev1)
        prev2 = prev1
        prev1 = current
    
    return prev1


def rob_dp_array(nums):
    """
    Solution using DP array (easier to understand)
    
    dp[i] = maximum money robbing up to house i
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    n = len(nums)
    dp = [0] * n
    
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        # Rob current house + dp[i-2] OR skip it and take dp[i-1]
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])
    
    return dp[n-1]


def rob_verbose(nums):
    """
    Detailed version showing decision at each house
    """
    if not nums:
        return 0
    if len(nums) == 1:
        print(f"Houses: {nums}")
        print(f"Only one house, rob it: {nums[0]}")
        return nums[0]
    
    print(f"Houses with money: {nums}")
    print("\nDeciding at each house:\n")
    
    n = len(nums)
    dp = [0] * n
    
    dp[0] = nums[0]
    print(f"House 0 (${nums[0]}): Rob it! Total = ${dp[0]}")
    
    dp[1] = max(nums[0], nums[1])
    if dp[1] == nums[1]:
        print(f"House 1 (${nums[1]}): Rob it (better than ${nums[0]})! Total = ${dp[1]}")
    else:
        print(f"House 1 (${nums[1]}): Skip it (${nums[0]} is better)! Total = ${dp[1]}")
    
    for i in range(2, n):
        rob_current = nums[i] + dp[i-2]
        skip_current = dp[i-1]
        
        dp[i] = max(rob_current, skip_current)
        
        print(f"\nHouse {i} (${nums[i]}):")
        print(f"  Option 1: Rob it -> ${nums[i]} + ${dp[i-2]} = ${rob_current}")
        print(f"  Option 2: Skip it -> Keep ${skip_current}")
        
        if dp[i] == rob_current:
            print(f"  Decision: ROB IT! Total = ${dp[i]} ✓")
        else:
            print(f"  Decision: SKIP IT! Total = ${dp[i]} ✓")
    
    print(f"\nMaximum money: ${dp[n-1]}")
    return dp[n-1]


def rob_recursive(nums, i=0, memo=None):
    """
    Recursive solution with memoization
    Shows the recursive thinking
    """
    if memo is None:
        memo = {}
    
    if i >= len(nums):
        return 0
    
    if i in memo:
        return memo[i]
    
    # Either rob current house or skip it
    rob_current = nums[i] + rob_recursive(nums, i + 2, memo)
    skip_current = rob_recursive(nums, i + 1, memo)
    
    memo[i] = max(rob_current, skip_current)
    return memo[i]


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([2, 1, 1, 2], 4),
        ([5, 3, 4, 11, 2], 16),
        ([1], 1),
        ([2, 1], 2),
    ]
    
    print("=== Testing Optimized Solution ===")
    for nums, expected in test_cases:
        result = rob(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} Houses: {nums}")
        print(f"   Max money: ${result} (Expected: ${expected})")
        print()
    
    print("=== Testing DP Array Solution ===")
    for nums, expected in test_cases:
        result = rob_dp_array(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} {nums} -> ${result}")
    
    print("\n=== Verbose Example ===")
    rob_verbose([2, 7, 9, 3, 1])

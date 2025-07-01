"""
LeetCode #300 - Longest Increasing Subsequence
Topic: Dynamic Programming
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Find length of longest strictly increasing subsequence.

Example:
[10,9,2,5,3,7,101,18] -> 4 ([2,3,7,101])

Subsequence: not necessarily contiguous!

Think of it like:
Finding longest rising trend in stock prices!

WHY THIS WORKS (Simple Explanation):
For each element, find longest subsequence ending at it.

dp[i] = 1 + max(dp[j]) for all j < i where nums[j] < nums[i]

Time: O(n²), can optimize to O(n log n) with binary search
Space: O(n)
"""

def lengthOfLIS(nums):
    """Find length of LIS"""
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n  # Each element is subsequence of length 1
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)


# Test
if __name__ == "__main__":
    tests = [
        ([10,9,2,5,3,7,101,18], 4),
        ([0,1,0,3,2,3], 4),
        ([7,7,7,7,7,7,7], 1),
    ]
    
    for nums, exp in tests:
        result = lengthOfLIS(nums)
        print(f"{nums} -> {result} (expected {exp})")

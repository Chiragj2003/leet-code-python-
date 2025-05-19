"""
LeetCode #198 already exists, creating #213 - House Robber II
Topic: Dynamic Programming
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Same as House Robber but houses arranged in CIRCLE!
First and last houses are neighbors.

Example:
[2,3,2] -> 3 (can't rob both 2s)
[1,2,3,1] -> 4 (rob houses 1 and 3)

Think of it like:
Robbing houses on circular street!

WHY THIS WORKS (Simple Explanation):
Can't rob both first and last house.
Run House Robber twice:
1. Without first house
2. Without last house
Take maximum!

Time: O(n)
Space: O(1)
"""

def rob(nums):
    """Rob houses in circle"""
    if len(nums) == 1:
        return nums[0]
    
    def rob_linear(houses):
        prev1 = prev2 = 0
        for num in houses:
            temp = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = temp
        return prev1
    
    # Case 1: Skip last house
    # Case 2: Skip first house
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


# Test
if __name__ == "__main__":
    tests = [
        ([2,3,2], 3),
        ([1,2,3,1], 4),
        ([1,2,3], 3),
    ]
    
    for nums, exp in tests:
        result = rob(nums)
        print(f"{nums} -> ${result} (expected ${exp})")

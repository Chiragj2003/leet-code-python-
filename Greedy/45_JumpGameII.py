"""
LeetCode #45 - Jump Game II
Topic: Greedy / Array
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Find minimum jumps to reach last index.

Example:
[2,3,1,1,4] -> 2 jumps (index 0->1->4)

Think of it like:
Least hops to reach the end!

WHY THIS WORKS (Simple Explanation):
Greedy BFS-like approach:
- Track current jump range
- Find furthest reach in range
- Jump to next range

Time: O(n)
Space: O(1)
"""

def jump(nums):
    """Minimum jumps to reach end"""
    jumps = 0
    current_end = 0
    farthest = 0
    
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        
        if i == current_end:
            jumps += 1
            current_end = farthest
    
    return jumps


# Test
if __name__ == "__main__":
    tests = [
        ([2,3,1,1,4], 2),
        ([2,3,0,1,4], 2),
    ]
    
    for nums, exp in tests:
        result = jump(nums)
        print(f"{nums} -> {result} jumps (expected {exp})")

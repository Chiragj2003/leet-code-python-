"""
LeetCode #55 - Jump Game
Topic: Greedy / Array
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Can you reach last index?
Each element = max jump length from that position.

Example:
[2,3,1,1,4] -> True (jump 1 to index 1, then 3 to last)
[3,2,1,0,4] -> False (stuck at index 3)

Think of it like:
Can you hop to the end of stepping stones?

WHY THIS WORKS (Simple Explanation):
Track furthest reachable position:
- At each step, update max reach
- If current position > max reach, stuck!

Time: O(n)
Space: O(1)
"""

def canJump(nums):
    """Check if can reach last index"""
    max_reach = 0
    
    for i in range(len(nums)):
        if i > max_reach:
            return False
        
        max_reach = max(max_reach, i + nums[i])
        
        if max_reach >= len(nums) - 1:
            return True
    
    return True


# Test
if __name__ == "__main__":
    tests = [
        ([2,3,1,1,4], True),
        ([3,2,1,0,4], False),
    ]
    
    for nums, exp in tests:
        result = canJump(nums)
        print(f"{nums} -> {result} (expected {exp})")

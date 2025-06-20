"""
LeetCode #169 - Majority Element
Topic: Array / Boyer-Moore Voting
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Find element that appears more than n/2 times.

Example:
[3,2,3] -> 3
[2,2,1,1,1,2,2] -> 2

Think of it like:
Finding the most popular vote!

WHY THIS WORKS (Boyer-Moore Voting):
Maintain candidate and count.
If count=0, pick new candidate.
Majority element always wins!

Time: O(n)
Space: O(1)
"""

def majorityElement(nums):
    """Find majority element"""
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
        
        count += 1 if num == candidate else -1
    
    return candidate


# Test
if __name__ == "__main__":
    tests = [
        ([3,2,3], 3),
        ([2,2,1,1,1,2,2], 2),
    ]
    
    for nums, exp in tests:
        result = majorityElement(nums)
        print(f"{nums} -> {result} (expected {exp})")

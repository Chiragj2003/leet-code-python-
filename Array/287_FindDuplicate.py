"""
LeetCode #287 - Find the Duplicate Number
Topic: Array / Two Pointers
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Array of n+1 integers where each integer is between 1 and n (inclusive).
There's exactly one duplicate number. Find it!

Example:
[1,3,4,2,2] -> 2 appears twice
[3,1,3,4,2] -> 3 appears twice

Constraints: Don't modify array, use only O(1) space

Think of it like:
Finding the repeated ID card in a pile!

WHY THIS WORKS (Simple Explanation):
Floyd's Cycle Detection (like Linked List Cycle!)

Treat array as linked list:
- Index i points to nums[i]
- Since there's a duplicate, there's a cycle!

Use fast & slow pointers to find cycle entry point.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def findDuplicate(nums):
    """
    Find duplicate using Floyd's Cycle Detection
    
    Visual: [1,3,4,2,2]
    Index:   0 1 2 3 4
    
    Treat as linked list:
    0 -> 1 -> 3 -> 2 -> 4 -> 2 (cycle!)
    
    Cycle exists because duplicate creates loop!
    """
    # Phase 1: Find intersection in cycle
    slow = fast = nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Phase 2: Find entrance to cycle (duplicate)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow


# Test
if __name__ == "__main__":
    test_cases = [
        ([1,3,4,2,2], 2),
        ([3,1,3,4,2], 3),
    ]
    
    for nums, expected in test_cases:
        result = findDuplicate(nums)
        print(f"{nums} -> {result} (expected {expected})")

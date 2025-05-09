"""
LeetCode #128 - Longest Consecutive Sequence
Topic: Array / Hashset
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Find length of longest consecutive sequence.
Must run in O(n) time!

Example:
[100,4,200,1,3,2] -> 4 (sequence: 1,2,3,4)

Think of it like:
Finding longest chain of sequential numbers!

WHY THIS WORKS (Simple Explanation):
Use set for O(1) lookup:
- For each number, check if it's start of sequence
- Count consecutive numbers from there

Time: O(n)
Space: O(n)
"""

def longestConsecutive(nums):
    """Find longest consecutive sequence"""
    if not nums:
        return 0
    
    num_set = set(nums)
    max_len = 0
    
    for num in num_set:
        # Only start counting if this is start of sequence
        if num - 1 not in num_set:
            current = num
            length = 1
            
            while current + 1 in num_set:
                current += 1
                length += 1
            
            max_len = max(max_len, length)
    
    return max_len


# Test
if __name__ == "__main__":
    tests = [
        ([100,4,200,1,3,2], 4),
        ([0,3,7,2,5,8,4,6,0,1], 9),
    ]
    
    for nums, exp in tests:
        result = longestConsecutive(nums)
        print(f"{nums} -> {result} (expected {exp})")

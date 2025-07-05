"""
LeetCode #80 - Remove Duplicates from Sorted Array II
Topic: Two Pointers
Difficulty: Medium

PROBLEM EXPLANATION:
Given a sorted array, remove duplicates in-place such that duplicates appear at most twice.
Return the new length of the array.

Example:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]

APPROACH (Two Pointers):
1. Use a slow pointer to track position where next valid element should go
2. Use a fast pointer to scan through array
3. An element is valid if it appears at most twice
4. Check if current element is different from element 2 positions back
5. If different (or count ≤ 2), it's valid - copy it to slow pointer position

Time Complexity: O(n)
Space Complexity: O(1)
"""

def removeDuplicates(nums):
    """
    Returns the new length after removing duplicates (keeping at most 2)
    """
    if len(nums) <= 2:
        return len(nums)
    
    # slow pointer: position for next valid element
    slow = 2
    
    # Start from index 2 since first two elements are always valid
    for fast in range(2, len(nums)):
        # If current element is different from element 2 positions back
        # it means we can include it (at most 2 duplicates allowed)
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1
    
    return slow


# Test cases
if __name__ == "__main__":
    test1 = [1, 1, 1, 2, 2, 3]
    length1 = removeDuplicates(test1)
    print(f"Test 1: Length={length1}, Array={test1[:length1]}")
    # Expected: Length=5, Array=[1,1,2,2,3]
    
    test2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    length2 = removeDuplicates(test2)
    print(f"Test 2: Length={length2}, Array={test2[:length2]}")
    # Expected: Length=7, Array=[0,0,1,1,2,3,3]
    
    test3 = [1, 1, 1, 1]
    length3 = removeDuplicates(test3)
    print(f"Test 3: Length={length3}, Array={test3[:length3]}")
    # Expected: Length=2, Array=[1,1]

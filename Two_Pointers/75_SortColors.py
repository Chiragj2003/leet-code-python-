"""
LeetCode #75 - Sort Colors
Topic: Two Pointers
Difficulty: Medium

PROBLEM EXPLANATION:
Given an array with n objects colored red, white, or blue, sort them in-place
so that objects of the same color are adjacent, with colors in order red, white, and blue.
We use integers 0, 1, and 2 to represent red, white, and blue respectively.

Example:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

APPROACH (Dutch National Flag Algorithm):
1. Use three pointers: low, mid, and high
2. low tracks position for next 0, high tracks position for next 2
3. mid scans through the array
4. When we see 0, swap with low pointer
5. When we see 2, swap with high pointer
6. When we see 1, just move mid forward

Time Complexity: O(n) - single pass through array
Space Complexity: O(1) - in-place sorting
"""

def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    low = 0      # pointer for next 0
    mid = 0      # current element being examined
    high = len(nums) - 1  # pointer for next 2
    
    while mid <= high:
        if nums[mid] == 0:
            # Swap with low pointer and move both forward
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            # Just move mid forward
            mid += 1
        else:  # nums[mid] == 2
            # Swap with high pointer and move high backward
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# Test cases
if __name__ == "__main__":
    test1 = [2, 0, 2, 1, 1, 0]
    sortColors(test1)
    print(f"Test 1: {test1}")  # Expected: [0, 0, 1, 1, 2, 2]
    
    test2 = [2, 0, 1]
    sortColors(test2)
    print(f"Test 2: {test2}")  # Expected: [0, 1, 2]
    
    test3 = [0]
    sortColors(test3)
    print(f"Test 3: {test3}")  # Expected: [0]

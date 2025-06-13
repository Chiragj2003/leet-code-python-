"""
LeetCode #33 - Search in Rotated Sorted Array
Topic: Binary Search
Difficulty: Medium

PROBLEM EXPLANATION:
A sorted array has been rotated at some pivot unknown to you.
Search for a target value and return its index, or -1 if not found.

Example:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

APPROACH (Modified Binary Search):
1. Use binary search, but identify which half is sorted
2. Check if target lies in the sorted half
3. If yes, search that half; otherwise search the other half
4. One half is always sorted in a rotated array

Key Insight: After rotation, one side of mid is always sorted!

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def search(nums, target):
    """
    Returns index of target, or -1 if not found
    """
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Found target
        if nums[mid] == target:
            return mid
        
        # Determine which side is sorted
        if nums[left] <= nums[mid]:
            # Left side is sorted
            if nums[left] <= target < nums[mid]:
                # Target is in sorted left side
                right = mid - 1
            else:
                # Target is in right side
                left = mid + 1
        else:
            # Right side is sorted
            if nums[mid] < target <= nums[right]:
                # Target is in sorted right side
                left = mid + 1
            else:
                # Target is in left side
                right = mid - 1
    
    return -1


# Test cases
if __name__ == "__main__":
    test1 = [4, 5, 6, 7, 0, 1, 2]
    print(f"Test 1: {search(test1, 0)}")  # Expected: 4
    
    test2 = [4, 5, 6, 7, 0, 1, 2]
    print(f"Test 2: {search(test2, 3)}")  # Expected: -1
    
    test3 = [1]
    print(f"Test 3: {search(test3, 0)}")  # Expected: -1
    
    test4 = [1, 3]
    print(f"Test 4: {search(test4, 3)}")  # Expected: 1

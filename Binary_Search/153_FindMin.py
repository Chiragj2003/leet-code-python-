"""
LeetCode #153 - Find Minimum in Rotated Sorted Array
Topic: Binary Search
Difficulty: Medium

PROBLEM EXPLANATION:
Suppose an array of unique elements sorted in ascending order is rotated
at some pivot. Find the minimum element.

Example:
Input: nums = [3,4,5,1,2]
Output: 1

Input: nums = [4,5,6,7,0,1,2]
Output: 0

APPROACH (Binary Search):
1. Use binary search to find the rotation point (minimum)
2. If nums[mid] > nums[right], minimum is in right half
3. Otherwise, minimum is in left half (including mid)
4. The rotation point is where the order breaks

Key Insight: Compare mid with right to determine which half has minimum

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def findMin(nums):
    """
    Returns the minimum element in rotated sorted array
    """
    left = 0
    right = len(nums) - 1
    
    # If array is not rotated or has single element
    if nums[left] <= nums[right]:
        return nums[left]
    
    while left < right:
        mid = (left + right) // 2
        
        # Check if mid+1 is the minimum
        if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        
        # Check if mid is the minimum
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return nums[mid]
        
        # Decide which half to search
        if nums[mid] > nums[right]:
            # Minimum is in right half
            left = mid + 1
        else:
            # Minimum is in left half
            right = mid


# Simpler approach
def findMin_v2(nums):
    """
    Cleaner implementation
    """
    left = 0
    right = len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            # Minimum is in right half
            left = mid + 1
        else:
            # Minimum is in left half (including mid)
            right = mid
    
    return nums[left]


# Test cases
if __name__ == "__main__":
    test1 = [3, 4, 5, 1, 2]
    print(f"Test 1: {findMin_v2(test1)}")  # Expected: 1
    
    test2 = [4, 5, 6, 7, 0, 1, 2]
    print(f"Test 2: {findMin_v2(test2)}")  # Expected: 0
    
    test3 = [11, 13, 15, 17]
    print(f"Test 3: {findMin_v2(test3)}")  # Expected: 11
    
    test4 = [2, 1]
    print(f"Test 4: {findMin_v2(test4)}")  # Expected: 1

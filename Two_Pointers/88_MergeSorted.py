"""
LeetCode #88 - Merge Sorted Array
Topic: Two Pointers
Difficulty: Easy

PROBLEM EXPLANATION:
You're given two sorted integer arrays nums1 and nums2.
Merge nums2 into nums1 as one sorted array.
nums1 has enough space (size m + n) to hold both arrays.

Example:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

APPROACH (Three Pointers - Fill from End):
1. Start from the end of both arrays
2. Compare elements and place the larger one at the end of nums1
3. Move backwards through both arrays
4. This avoids overwriting elements in nums1

Why fill from end? Because nums1 has empty space at the end!

Time Complexity: O(m + n)
Space Complexity: O(1)
"""

def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # Three pointers: p1 for nums1, p2 for nums2, p for merge position
    p1 = m - 1      # Last element in nums1's actual data
    p2 = n - 1      # Last element in nums2
    p = m + n - 1   # Last position in nums1
    
    # Merge from back to front
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    # If there are remaining elements in nums2, copy them
    # (no need to copy remaining nums1 elements, they're already there)
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1


# Test cases
if __name__ == "__main__":
    test1 = [1, 2, 3, 0, 0, 0]
    merge(test1, 3, [2, 5, 6], 3)
    print(f"Test 1: {test1}")  # Expected: [1, 2, 2, 3, 5, 6]
    
    test2 = [1]
    merge(test2, 1, [], 0)
    print(f"Test 2: {test2}")  # Expected: [1]
    
    test3 = [0]
    merge(test3, 0, [1], 1)
    print(f"Test 3: {test3}")  # Expected: [1]

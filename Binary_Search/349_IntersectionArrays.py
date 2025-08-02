"""
LeetCode #349 - Intersection of Two Arrays
Topic: Binary Search / Hash Set
Difficulty: Easy

PROBLEM EXPLANATION:
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return in any order.

Example:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4] or [4,9]

APPROACH 1 (Hash Set - Optimal):
1. Convert nums1 to a set for O(1) lookup
2. Iterate through nums2 and check if element exists in set
3. Add to result set to avoid duplicates

Time Complexity: O(n + m)
Space Complexity: O(n)

APPROACH 2 (Binary Search):
1. Sort one array
2. For each element in other array, use binary search
3. Useful when one array is already sorted

Time Complexity: O(n log n + m log n)
Space Complexity: O(1) excluding output
"""

def intersection(nums1, nums2):
    """
    Returns intersection using hash set (optimal approach)
    """
    set1 = set(nums1)
    result = set()
    
    for num in nums2:
        if num in set1:
            result.add(num)
    
    return list(result)


def intersection_binary_search(nums1, nums2):
    """
    Returns intersection using binary search
    """
    nums1.sort()
    result = set()
    
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
    for num in nums2:
        if binary_search(nums1, num):
            result.add(num)
    
    return list(result)


# Test cases
if __name__ == "__main__":
    test1_nums1 = [1, 2, 2, 1]
    test1_nums2 = [2, 2]
    print(f"Test 1: {intersection(test1_nums1, test1_nums2)}")
    # Expected: [2]
    
    test2_nums1 = [4, 9, 5]
    test2_nums2 = [9, 4, 9, 8, 4]
    print(f"Test 2: {intersection(test2_nums1, test2_nums2)}")
    # Expected: [9, 4] or [4, 9]
    
    test3_nums1 = [1, 2, 3]
    test3_nums2 = [4, 5, 6]
    print(f"Test 3: {intersection(test3_nums1, test3_nums2)}")
    # Expected: []

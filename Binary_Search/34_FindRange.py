"""
LeetCode #34 - Find First and Last Position of Element in Sorted Array
Topic: Binary Search
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
In a sorted array, find where a target number first appears and where it last appears.
Like finding the first and last page where a word appears in a dictionary!

Example:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Explanation: 8 appears at index 3 and 4

WHY THIS WORKS (Simple Explanation):
Use binary search twice:
1. First search: find leftmost occurrence (first position)
2. Second search: find rightmost occurrence (last position)

For leftmost: when we find target, keep searching left
For rightmost: when we find target, keep searching right

Time Complexity: O(log n) - two binary searches
Space Complexity: O(1) - only a few variables
"""

def searchRange(nums, target):
    """
    Find first and last position of target in sorted array
    
    Think of it like:
    - Use binary search to find ANY occurrence
    - Then use binary search again to find the boundaries
    - Or better: search for leftmost and rightmost separately
    """
    
    def find_leftmost(nums, target):
        """Find first occurrence of target"""
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                result = mid  # Found it, but keep searching left
                right = mid - 1  # Search left side
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    def find_rightmost(nums, target):
        """Find last occurrence of target"""
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                result = mid  # Found it, but keep searching right
                left = mid + 1  # Search right side
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    # Find both boundaries
    left_pos = find_leftmost(nums, target)
    if left_pos == -1:
        return [-1, -1]  # Target not found
    
    right_pos = find_rightmost(nums, target)
    return [left_pos, right_pos]


# Test cases with explanations
if __name__ == "__main__":
    test1 = [5, 7, 7, 8, 8, 10]
    print(f"Test 1: {searchRange(test1, 8)}")
    # Expected: [3, 4] - 8 appears at indices 3 and 4
    
    test2 = [5, 7, 7, 8, 8, 10]
    print(f"Test 2: {searchRange(test2, 6)}")
    # Expected: [-1, -1] - 6 not in array
    
    test3 = []
    print(f"Test 3: {searchRange(test3, 0)}")
    # Expected: [-1, -1] - empty array
    
    test4 = [1]
    print(f"Test 4: {searchRange(test4, 1)}")
    # Expected: [0, 0] - single element

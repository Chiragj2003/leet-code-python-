"""
LeetCode #713 - Subarray Product Less Than K
Topic: Two Pointers (Sliding Window)
Difficulty: Medium

PROBLEM EXPLANATION:
Given an array of positive integers and a positive integer k,
count the number of contiguous subarrays where the product of all elements
is strictly less than k.

Example:
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]

APPROACH (Sliding Window):
1. Use two pointers: left and right
2. Expand window by moving right, multiply product
3. If product >= k, shrink window from left by dividing
4. For each position of right, all subarrays ending at right are valid
5. Number of new subarrays = (right - left + 1)

Time Complexity: O(n)
Space Complexity: O(1)
"""

def numSubarrayProductLessThanK(nums, k):
    """
    Returns count of subarrays with product < k
    """
    if k <= 1:
        return 0
    
    count = 0
    product = 1
    left = 0
    
    for right in range(len(nums)):
        # Expand window: include nums[right]
        product *= nums[right]
        
        # Shrink window while product >= k
        while product >= k:
            product //= nums[left]
            left += 1
        
        # Add count of all subarrays ending at right
        # [left...right], [left+1...right], ..., [right]
        count += right - left + 1
    
    return count


# Test cases
if __name__ == "__main__":
    test1 = [10, 5, 2, 6]
    print(f"Test 1: {numSubarrayProductLessThanK(test1, 100)}")
    # Expected: 8
    
    test2 = [1, 2, 3]
    print(f"Test 2: {numSubarrayProductLessThanK(test2, 0)}")
    # Expected: 0
    
    test3 = [1, 1, 1]
    print(f"Test 3: {numSubarrayProductLessThanK(test3, 2)}")
    # Expected: 6 (all subarrays have product = 1 < 2)
    
    test4 = [10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3]
    print(f"Test 4: {numSubarrayProductLessThanK(test4, 19)}")
    # Expected: 18

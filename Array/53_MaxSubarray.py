"""
LeetCode #53 - Maximum Subarray
Topic: Array (Dynamic Programming / Kadane's Algorithm)
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Find the contiguous subarray with the largest sum.

Example:
[-2,1,-3,4,-1,2,1,-5,4] -> [4,-1,2,1] has sum = 6

Think of it like:
You're collecting coins along a path. Sometimes you find negative coins (debts).
If your collection becomes too negative, better to start fresh from next position!

WHY THIS WORKS (Simple Explanation):
Kadane's Algorithm - track running sum:
1. Keep adding numbers to current sum
2. If current sum becomes negative, reset to 0 (start fresh)
3. Track the maximum sum seen

Like building a snowball - if it melts too much, start a new one!

Time Complexity: O(n) - single pass through array
Space Complexity: O(1) - only storing few variables
"""

def maxSubArray(nums):
    """
    Kadane's Algorithm for maximum subarray sum
    
    Visual example: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    
    i=0: num=-2, current=-2, max=-2
    i=1: num=1, current=-2+1=-1, but reset to 1, max=1
    i=2: num=-3, current=1-3=-2, max=1
    i=3: num=4, current=-2+4=2, but reset to 4, max=4
    i=4: num=-1, current=4-1=3, max=4
    i=5: num=2, current=3+2=5, max=5
    i=6: num=1, current=5+1=6, max=6
    i=7: num=-5, current=6-5=1, max=6
    i=8: num=4, current=1+4=5, max=6
    
    Result: 6 (subarray [4,-1,2,1])
    """
    # Initialize with first element
    max_sum = current_sum = nums[0]
    
    # Process rest of array
    for num in nums[1:]:
        # Either extend current subarray or start new one
        # Start new if current_sum is dragging us down
        current_sum = max(num, current_sum + num)
        
        # Track maximum
        max_sum = max(max_sum, current_sum)
    
    return max_sum


def maxSubArray_detailed(nums):
    """
    Same algorithm with detailed tracking
    Shows which subarray gives maximum sum
    """
    max_sum = float('-inf')
    current_sum = 0
    start = 0
    end = 0
    temp_start = 0
    
    for i, num in enumerate(nums):
        current_sum += num
        
        # Update maximum
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
        
        # Reset if current sum goes negative
        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1
    
    print(f"Maximum subarray: {nums[start:end+1]}")
    return max_sum


def maxSubArray_divide_conquer(nums):
    """
    Alternative: Divide and Conquer approach
    
    Maximum subarray is either:
    1. Entirely in left half
    2. Entirely in right half
    3. Crosses the middle
    
    Time: O(n log n), Space: O(log n) for recursion
    """
    def helper(left, right):
        # Base case: single element
        if left == right:
            return nums[left]
        
        mid = (left + right) // 2
        
        # Maximum in left half
        left_max = helper(left, mid)
        
        # Maximum in right half
        right_max = helper(mid + 1, right)
        
        # Maximum crossing middle
        # Find max sum from mid going left
        left_sum = float('-inf')
        current = 0
        for i in range(mid, left - 1, -1):
            current += nums[i]
            left_sum = max(left_sum, current)
        
        # Find max sum from mid+1 going right
        right_sum = float('-inf')
        current = 0
        for i in range(mid + 1, right + 1):
            current += nums[i]
            right_sum = max(right_sum, current)
        
        # Maximum is best of three
        cross_max = left_sum + right_sum
        
        return max(left_max, right_max, cross_max)
    
    return helper(0, len(nums) - 1)


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),  # [4,-1,2,1]
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),  # [5,4,-1,7,8]
        ([-1], -1),
        ([-2, -1], -1),
        ([1, 2, -1, -2, 2, 1, -2, 1], 3),  # [2,1]
    ]
    
    print("=== Testing Kadane's Algorithm ===")
    for nums, expected in test_cases:
        result = maxSubArray(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {nums}")
        print(f"   Max Sum: {result} (Expected: {expected})")
        print()
    
    print("=== Detailed Solution (showing subarray) ===")
    for nums, expected in test_cases[:3]:
        print(f"Input: {nums}")
        result = maxSubArray_detailed(nums)
        print(f"Sum: {result}\n")

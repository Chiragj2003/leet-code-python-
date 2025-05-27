"""
LeetCode #15 - 3Sum
Topic: Two Pointers
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Find all unique triplets (3 numbers) in an array that add up to zero.
Like finding three friends whose combined ages equal 0 (positive and negative ages)!

Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: -1 + -1 + 2 = 0 and -1 + 0 + 1 = 0

WHY THIS WORKS (Simple Explanation):
1. Sort the array first (makes it easier to avoid duplicates)
2. Fix one number and use two pointers for the other two
3. If sum is too small, move left pointer right (to get bigger numbers)
4. If sum is too large, move right pointer left (to get smaller numbers)
5. Skip duplicates to avoid repeated triplets

Time Complexity: O(n²) - for each number, we use two pointers
Space Complexity: O(1) - excluding output array
"""

def threeSum(nums):
    """
    Find all unique triplets that sum to zero
    
    Simple approach:
    1. Sort array: [-4, -1, -1, 0, 1, 2]
    2. For each number, try to find two others that make sum = 0
    3. Use two pointers (like in 2Sum for sorted array)
    """
    nums.sort()
    result = []
    
    # Fix first number
    for i in range(len(nums) - 2):
        # Skip duplicate first numbers
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        # Now find two numbers that sum to -nums[i]
        target = -nums[i]
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                # Found a triplet!
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            
            elif current_sum < target:
                # Sum too small, need bigger numbers
                left += 1
            else:
                # Sum too large, need smaller numbers
                right -= 1
    
    return result


# Test cases with explanations
if __name__ == "__main__":
    test1 = [-1, 0, 1, 2, -1, -4]
    print(f"Test 1: {threeSum(test1)}")
    # Expected: [[-1, -1, 2], [-1, 0, 1]]
    
    test2 = [0, 1, 1]
    print(f"Test 2: {threeSum(test2)}")
    # Expected: [] (no triplet sums to 0)
    
    test3 = [0, 0, 0]
    print(f"Test 3: {threeSum(test3)}")
    # Expected: [[0, 0, 0]]

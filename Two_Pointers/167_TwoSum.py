"""
LeetCode #167 - Two Sum II - Input Array Is Sorted
Topic: Two Pointers
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Given a sorted array, find two numbers that add up to a target.
Return their positions (1-indexed, not 0-indexed).

Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: 2 + 7 = 9, positions are 1 and 2

WHY THIS WORKS (Simple Explanation):
Since array is sorted, we can use two pointers:
- Start from both ends
- If sum is too small, move left pointer right (get bigger number)
- If sum is too large, move right pointer left (get smaller number)
- If sum matches, we found it!

Time Complexity: O(n) - single pass with two pointers
Space Complexity: O(1) - only two pointers used
"""

def twoSum(numbers, target):
    """
    Find two numbers that sum to target in sorted array
    
    Easy to understand:
    - Left pointer at start, right pointer at end
    - Add numbers at both pointers
    - Too small? Move left forward (bigger numbers ahead)
    - Too big? Move right backward (smaller numbers behind)
    - Just right? Return positions!
    """
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            # Found it! Return 1-indexed positions
            return [left + 1, right + 1]
        
        elif current_sum < target:
            # Need bigger sum, move left pointer right
            left += 1
        
        else:
            # Need smaller sum, move right pointer left
            right -= 1
    
    # Problem guarantees exactly one solution, so we'll never reach here
    return []


# Test cases with explanations
if __name__ == "__main__":
    test1 = [2, 7, 11, 15]
    print(f"Test 1: {twoSum(test1, 9)}")
    # Expected: [1, 2] because 2 + 7 = 9
    
    test2 = [2, 3, 4]
    print(f"Test 2: {twoSum(test2, 6)}")
    # Expected: [1, 3] because 2 + 4 = 6
    
    test3 = [-1, 0]
    print(f"Test 3: {twoSum(test3, -1)}")
    # Expected: [1, 2] because -1 + 0 = -1

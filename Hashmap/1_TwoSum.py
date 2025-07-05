"""
LeetCode #1 - Two Sum
Topic: Hashmap
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Given an array of numbers and a target, find two numbers that add up to target.
Return their positions (indices).

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9

WHY THIS WORKS (Simple Explanation):
Use a hashmap (dictionary) to remember numbers we've seen:
- For each number, check if (target - current_number) exists in hashmap
- If yes, we found the pair!
- If no, store current number in hashmap and continue

Why hashmap? Because looking up in hashmap is super fast - O(1)!

Time Complexity: O(n) - visit each number once
Space Complexity: O(n) - store numbers in hashmap
"""

def twoSum(nums, target):
    """
    Find two numbers that sum to target
    
    Simple approach:
    1. Create empty hashmap
    2. For each number:
       - Calculate what number we need: needed = target - current
       - Check if we've seen this needed number before
       - If yes, return both indices
       - If no, remember current number
    """
    # Dictionary to store: number -> its index
    seen = {}
    
    for i, num in enumerate(nums):
        # What number do we need to reach target?
        needed = target - num
        
        # Have we seen this needed number before?
        if needed in seen:
            # Yes! Return both indices
            return [seen[needed], i]
        
        # No, remember current number for future
        seen[num] = i
    
    # Problem guarantees exactly one solution, so we won't reach here
    return []


# Test cases with explanations
if __name__ == "__main__":
    test1 = [2, 7, 11, 15]
    print(f"Test 1: {twoSum(test1, 9)}")
    # Expected: [0, 1]
    # Walk through: needed for 2 is 7, not seen yet, store 2
    #               needed for 7 is 2, we've seen 2! Return [0, 1]
    
    test2 = [3, 2, 4]
    print(f"Test 2: {twoSum(test2, 6)}")
    # Expected: [1, 2]
    # 3+2=5, 3+4=7, but 2+4=6 ✓
    
    test3 = [3, 3]
    print(f"Test 3: {twoSum(test3, 6)}")
    # Expected: [0, 1]
    # Same number twice: 3+3=6

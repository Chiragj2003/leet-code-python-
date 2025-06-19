"""
LeetCode #283 - Move Zeroes
Topic: Array / Two Pointers
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Move all zeros to the end while maintaining order of non-zero elements.

Example:
[0,1,0,3,12] -> [1,3,12,0,0]

Think of it like:
Cleaning a shelf - push all empty spaces to the right,
keep all items in their relative order on the left!

WHY THIS WORKS (Simple Explanation):
Use two pointers:
1. One pointer finds non-zero elements
2. Another pointer tracks where to place them
3. After placing all non-zeros, fill rest with zeros

Like sorting laundry - put clean clothes on left, empty space on right!

Alternative: Swap non-zeros with zeros as we find them

Time Complexity: O(n) - single pass
Space Complexity: O(1) - in-place modification
"""

def moveZeroes(nums):
    """
    Move zeros to end (in-place)
    
    Visual example: [0, 1, 0, 3, 12]
    
    Two pointers:
    - left: where to place next non-zero
    - right: scanning for non-zeros
    
    right=0: nums[0]=0 (skip)
    right=1: nums[1]=1 (non-zero!) -> nums[left]=1, left++ -> [1,1,0,3,12], left=1
    right=2: nums[2]=0 (skip)
    right=3: nums[3]=3 (non-zero!) -> nums[left]=3, left++ -> [1,3,0,3,12], left=2
    right=4: nums[4]=12 (non-zero!) -> nums[left]=12, left++ -> [1,3,12,3,12], left=3
    
    Fill rest with zeros: [1,3,12,0,0]
    """
    # Pointer for where to place next non-zero
    left = 0
    
    # Find all non-zero elements and move them to front
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left] = nums[right]
            left += 1
    
    # Fill rest with zeros
    for i in range(left, len(nums)):
        nums[i] = 0


def moveZeroes_swap(nums):
    """
    Alternative: Swap method
    
    When we find a non-zero, swap it with leftmost zero position
    
    Example: [0, 1, 0, 3, 12]
    
    left=0 (tracks leftmost zero position)
    
    i=0: nums[0]=0, left stays 0
    i=1: nums[1]=1 (non-zero!), swap with nums[0] -> [1,0,0,3,12], left=1
    i=2: nums[2]=0, left stays 1
    i=3: nums[3]=3 (non-zero!), swap with nums[1] -> [1,3,0,0,12], left=2
    i=4: nums[4]=12 (non-zero!), swap with nums[2] -> [1,3,12,0,0], left=3
    """
    left = 0  # Points to leftmost zero
    
    for right in range(len(nums)):
        if nums[right] != 0:
            # Swap non-zero with leftmost zero
            nums[left], nums[right] = nums[right], nums[left]
            left += 1


def moveZeroes_verbose(nums):
    """
    Detailed version showing each step
    """
    print(f"Initial array: {nums}\n")
    
    left = 0
    
    print("=== Finding and moving non-zeros ===")
    for right in range(len(nums)):
        if nums[right] != 0:
            print(f"Step {right}: Found non-zero {nums[right]} at position {right}")
            print(f"  Place it at position {left}")
            nums[left] = nums[right]
            left += 1
            print(f"  Array now: {nums}")
            print()
    
    print(f"=== Filling remaining positions with zeros ===")
    for i in range(left, len(nums)):
        print(f"Position {i}: Set to 0")
        nums[i] = 0
    
    print(f"\nFinal array: {nums}")


# Test cases
if __name__ == "__main__":
    test_cases = [
        [0, 1, 0, 3, 12],
        [0],
        [1, 2, 3],
        [0, 0, 1],
        [2, 1],
    ]
    
    print("=== Testing Two-Pointer Solution ===")
    for nums in test_cases:
        original = nums.copy()
        moveZeroes(nums)
        print(f"Input:  {original}")
        print(f"Output: {nums}")
        print()
    
    print("=== Testing Swap Solution ===")
    test_cases = [
        [0, 1, 0, 3, 12],
        [0],
        [1, 2, 3],
        [0, 0, 1],
        [2, 1],
    ]
    for nums in test_cases:
        original = nums.copy()
        moveZeroes_swap(nums)
        print(f"Input:  {original}")
        print(f"Output: {nums}")
        print()
    
    print("=== Verbose Example ===")
    nums = [0, 1, 0, 3, 12]
    moveZeroes_verbose(nums)

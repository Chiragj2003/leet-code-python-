"""
LeetCode #75 - Sort Colors
Topic: Array / Two Pointers
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Sort array with 0s, 1s, 2s in-place.
(Dutch National Flag problem)

Example:
[2,0,2,1,1,0] -> [0,0,1,1,2,2]

Think of it like:
Sorting red, white, blue flags!

WHY THIS WORKS:
Three pointers: left (0s), curr (scanning), right (2s)
- If 0: swap with left
- If 2: swap with right
- If 1: just move forward

Time: O(n)
Space: O(1)
"""

def sortColors(nums):
    """Sort colors in-place"""
    left, curr, right = 0, 0, len(nums) - 1
    
    while curr <= right:
        if nums[curr] == 0:
            nums[left], nums[curr] = nums[curr], nums[left]
            left += 1
            curr += 1
        elif nums[curr] == 2:
            nums[curr], nums[right] = nums[right], nums[curr]
            right -= 1
        else:
            curr += 1


# Test
if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    print(f"Before: {nums}")
    sortColors(nums)
    print(f"After: {nums}")

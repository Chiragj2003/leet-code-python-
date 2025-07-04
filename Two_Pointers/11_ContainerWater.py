"""
LeetCode #11 - Container With Most Water
Topic: Two Pointers
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Imagine you have vertical lines at different positions on a number line.
You want to find two lines that can hold the most water between them.
Think of it like finding the best container!

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: Lines at position 1 (height=8) and position 8 (height=7)
form a container. Width = 7, min height = 7, area = 7*7 = 49

WHY THIS WORKS (Simple Explanation):
- Start with the widest possible container (leftmost and rightmost lines)
- The water level is limited by the shorter line
- Move the shorter line inward - maybe we'll find a taller line
- Keep track of the maximum area we've seen
- Continue until pointers meet

Time Complexity: O(n) - we look at each line once
Space Complexity: O(1) - we only use two pointers
"""

def maxArea(height):
    """
    Find maximum water container area
    
    Think of it like this:
    - Two pointers start at both ends (widest container)
    - Calculate area = width * min(left_height, right_height)
    - Move the pointer with smaller height (try to find taller line)
    - Keep doing this until pointers meet
    """
    left = 0
    right = len(height) - 1
    max_water = 0
    
    while left < right:
        # Calculate current container area
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        
        # Update maximum
        max_water = max(max_water, current_area)
        
        # Move the pointer with smaller height
        # Why? Because the shorter side limits water, so we try to find a taller one
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water


# Test cases with explanations
if __name__ == "__main__":
    test1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Test 1: {maxArea(test1)}")  # Expected: 49
    # Best container: between height 8 at index 1 and height 7 at index 8
    
    test2 = [1, 1]
    print(f"Test 2: {maxArea(test2)}")  # Expected: 1
    # Only two lines, width=1, height=1
    
    test3 = [4, 3, 2, 1, 4]
    print(f"Test 3: {maxArea(test3)}")  # Expected: 16
    # Container between first and last line: width=4, height=4

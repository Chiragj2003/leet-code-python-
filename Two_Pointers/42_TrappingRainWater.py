"""
LeetCode #42 - Trapping Rain Water
Topic: Two Pointers / Stack
Difficulty: Hard

PROBLEM EXPLANATION (Easy Terms):
Calculate how much water can be trapped after rain.

Example:
[0,1,0,2,1,0,1,3,2,1,2,1]
Water trapped: 6 units

Think of it like:
Pools formed between walls!

WHY THIS WORKS (Two Pointers):
Track max heights from left and right.
Water at position = min(left_max, right_max) - height

Time: O(n)
Space: O(1)
"""

def trap(height):
    """Calculate trapped rainwater"""
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    
    return water


# Test
if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    result = trap(height)
    print(f"Water trapped: {result} units")

"""
LeetCode #84 - Largest Rectangle in Histogram
Topic: Stack / Monotonic Stack
Difficulty: Hard

PROBLEM EXPLANATION (Easy Terms):
Find largest rectangle in histogram.

Example:
heights = [2,1,5,6,2,3]
-> 10 (rectangle of width 2, height 5)

Think of it like:
Finding biggest box that fits under bars!

WHY THIS WORKS:
Use monotonic stack to track heights.
When see smaller height, calculate rectangles.

Time: O(n)
Space: O(n)
"""

def largestRectangleArea(heights):
    """Find largest rectangle area"""
    stack = []
    max_area = 0
    heights.append(0)  # Sentinel
    
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area


# Test
if __name__ == "__main__":
    tests = [
        ([2,1,5,6,2,3], 10),
        ([2,4], 4),
    ]
    
    for heights, exp in tests:
        result = largestRectangleArea(heights[:])
        print(f"{heights} -> {result} (expected {exp})")

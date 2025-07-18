"""
LeetCode #85 - Maximal Rectangle
Topic: Stack / Dynamic Programming
Difficulty: Hard

PROBLEM EXPLANATION (Easy Terms):
Find largest rectangle of 1s in binary matrix.

Example:
[["1","0","1","0","0"],
 ["1","0","1","1","1"],
 ["1","1","1","1","1"],
 ["1","0","0","1","0"]]
-> 6

Think of it like:
Finding biggest rectangular area of 1s!

WHY THIS WORKS:
Convert to histogram problem for each row!
For each row, calculate heights and use histogram solution.

Time: O(m × n)
Space: O(n)
"""

def maximalRectangle(matrix):
    """Find maximal rectangle"""
    if not matrix:
        return 0
    
    n = len(matrix[0])
    heights = [0] * n
    max_area = 0
    
    for row in matrix:
        for i in range(n):
            heights[i] = heights[i] + 1 if row[i] == '1' else 0
        
        max_area = max(max_area, largestHistogram(heights))
    
    return max_area


def largestHistogram(heights):
    """Helper: largest rectangle in histogram"""
    stack = []
    max_area = 0
    heights = heights + [0]
    
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area


# Test
if __name__ == "__main__":
    matrix = [["1","0","1","0","0"],
              ["1","0","1","1","1"],
              ["1","1","1","1","1"],
              ["1","0","0","1","0"]]
    result = maximalRectangle(matrix)
    print(f"Maximal rectangle: {result}")

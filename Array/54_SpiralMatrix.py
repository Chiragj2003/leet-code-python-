"""
LeetCode #54 - Spiral Matrix
Topic: Array / Matrix
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Return elements of matrix in spiral order.

Example:
[[1,2,3],
 [4,5,6],
 [7,8,9]]
-> [1,2,3,6,9,8,7,4,5]

Think of it like:
Walking around matrix edges inward!

WHY THIS WORKS (Simple Explanation):
Track four boundaries:
- top, bottom, left, right
Move right, down, left, up, shrinking boundaries!

Time: O(m × n)
Space: O(1) excluding result
"""

def spiralOrder(matrix):
    """Return matrix in spiral order"""
    if not matrix:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Right
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1
        
        # Down
        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1
        
        # Left (if still valid)
        if top <= bottom:
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1
        
        # Up (if still valid)
        if left <= right:
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1
    
    return result


# Test
if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    result = spiralOrder(matrix)
    print(f"Spiral: {result}")

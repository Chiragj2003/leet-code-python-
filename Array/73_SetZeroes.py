"""
LeetCode #73 - Set Matrix Zeroes
Topic: Array / Matrix
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
If element is 0, set entire row and column to 0!
Do it IN-PLACE.

Example:
[[1,1,1],      [[1,0,1],
 [1,0,1],  ->   [0,0,0],
 [1,1,1]]       [1,0,1]]

Think of it like:
Spreading zeros across rows and columns!

WHY THIS WORKS (Simple Explanation):
Use first row/column as markers:
1. Mark which rows/cols need zeroing
2. Use markers to set zeros
3. Handle first row/col separately

Time: O(m × n)
Space: O(1)
"""

def setZeroes(matrix):
    """Set matrix zeroes in-place"""
    m, n = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][c] == 0 for c in range(n))
    first_col_zero = any(matrix[r][0] == 0 for r in range(m))
    
    # Use first row/col as markers
    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0
    
    # Set zeros based on markers
    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0
    
    # Handle first row
    if first_row_zero:
        for c in range(n):
            matrix[0][c] = 0
    
    # Handle first column
    if first_col_zero:
        for r in range(m):
            matrix[r][0] = 0


# Test
if __name__ == "__main__":
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print("Before:", matrix)
    setZeroes(matrix)
    print("After:", matrix)

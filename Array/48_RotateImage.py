"""
LeetCode #48 - Rotate Image
Topic: Array / Matrix
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Rotate a 2D matrix 90 degrees clockwise IN-PLACE.

Example:
[1,2,3]      [7,4,1]
[4,5,6]  ->  [8,5,2]
[7,8,9]      [9,6,3]

Think of it like:
Rotating a photo 90 degrees clockwise!

WHY THIS WORKS (Simple Explanation):
Two steps:
1. Transpose matrix (swap rows and columns)
2. Reverse each row

Example:
[1,2,3]    Transpose    [1,4,7]    Reverse rows    [7,4,1]
[4,5,6]   ---------->   [2,5,8]   ------------->  [8,5,2]
[7,8,9]                 [3,6,9]                    [9,6,3]

Time Complexity: O(n²) where n is matrix dimension
Space Complexity: O(1) - in-place
"""

def rotate(matrix):
    """Rotate matrix 90 degrees clockwise"""
    n = len(matrix)
    
    # Step 1: Transpose (swap matrix[i][j] with matrix[j][i])
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()


def rotate_verbose(matrix):
    """Detailed version"""
    import copy
    original = copy.deepcopy(matrix)
    n = len(matrix)
    
    print(f"Original matrix:")
    for row in original:
        print(f"  {row}")
    print()
    
    # Transpose
    print("Step 1: Transpose")
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for row in matrix:
        print(f"  {row}")
    print()
    
    # Reverse rows
    print("Step 2: Reverse each row")
    for i in range(n):
        matrix[i].reverse()
    
    for row in matrix:
        print(f"  {row}")
    print()


# Test
if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    rotate_verbose(matrix)

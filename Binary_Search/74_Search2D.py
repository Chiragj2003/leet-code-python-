"""
LeetCode #74 - Search a 2D Matrix
Topic: Binary Search
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
You have a 2D matrix where:
- Each row is sorted left to right
- First element of each row is greater than last element of previous row
Basically, if you flatten it, it's one big sorted array!

Search for a target value efficiently.

Example:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

WHY THIS WORKS (Simple Explanation):
Treat the 2D matrix as a 1D sorted array!
- Use binary search on this "virtual" 1D array
- Convert 1D index to 2D coordinates: row = index / cols, col = index % cols
- This way we get O(log(m*n)) time instead of checking each element

Time Complexity: O(log(m*n)) - binary search on all elements
Space Complexity: O(1) - only a few variables
"""

def searchMatrix(matrix, target):
    """
    Search in 2D matrix using binary search
    
    Simple trick:
    - Imagine 2D matrix as 1D array
    - Use binary search on this 1D array
    - Convert index back to 2D when needed
    
    Example: [[1,3,5],[7,9,11]]
    Think of it as: [1,3,5,7,9,11]
    """
    if not matrix or not matrix[0]:
        return False
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Binary search on "virtual" 1D array
    left = 0
    right = rows * cols - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Convert 1D index to 2D coordinates
        row = mid // cols
        col = mid % cols
        mid_value = matrix[row][col]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    
    return False


# Test cases with explanations
if __name__ == "__main__":
    test1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(f"Test 1: {searchMatrix(test1, 3)}")
    # Expected: True - 3 is in the matrix
    
    print(f"Test 2: {searchMatrix(test1, 13)}")
    # Expected: False - 13 is not in the matrix
    
    test3 = [[1]]
    print(f"Test 3: {searchMatrix(test3, 1)}")
    # Expected: True - single element match
    
    test4 = [[1, 3, 5]]
    print(f"Test 4: {searchMatrix(test4, 3)}")
    # Expected: True - single row matrix

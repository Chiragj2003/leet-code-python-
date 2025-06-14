"""
LeetCode #463 - Island Perimeter
Topic: Hashmap / Array
Difficulty: Easy

PROBLEM EXPLANATION:
Given a 2D grid where 1 represents land and 0 represents water,
calculate the perimeter of the island. There is exactly one island,
and it doesn't have lakes (water inside that isn't connected to water around the island).

Example:
Input: grid = [[0,1,0,0],
               [1,1,1,0],
               [0,1,0,0],
               [1,1,0,0]]
Output: 16

APPROACH:
1. For each land cell (1), it contributes 4 to perimeter
2. For each adjacent land cell, subtract 2 (shared edge)
3. Alternatively: count edges that border water or grid boundary

Time Complexity: O(m * n)
Space Complexity: O(1)
"""

def islandPerimeter(grid):
    """
    Returns the perimeter of the island
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides
                perimeter += 4
                
                # Check top neighbor
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2  # Shared edge
                
                # Check left neighbor
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2  # Shared edge
    
    return perimeter


# Alternative: Count exposed edges
def islandPerimeter_v2(grid):
    """
    Count edges bordering water or boundary
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all 4 directions
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    # If out of bounds or water, add to perimeter
                    if ni < 0 or ni >= rows or nj < 0 or nj >= cols or grid[ni][nj] == 0:
                        perimeter += 1
    
    return perimeter


# Test cases
if __name__ == "__main__":
    test1 = [[0,1,0,0],
             [1,1,1,0],
             [0,1,0,0],
             [1,1,0,0]]
    print(f"Test 1: {islandPerimeter(test1)}")  # Expected: 16
    
    test2 = [[1]]
    print(f"Test 2: {islandPerimeter(test2)}")  # Expected: 4
    
    test3 = [[1,0]]
    print(f"Test 3: {islandPerimeter(test3)}")  # Expected: 4

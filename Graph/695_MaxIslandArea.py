"""
LeetCode #200 already exists - this is #695 - Max Area of Island
Topic: Graph / DFS
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Find largest island area in grid.

Example:
[[0,0,1,0,0],
 [0,1,1,0,0],
 [1,1,0,0,0]] -> 6

Think of it like:
Finding biggest connected land mass!

WHY THIS WORKS:
DFS to explore each island, count cells.

Time: O(m × n)
Space: O(m × n)
"""

def maxAreaOfIsland(grid):
    """Find max island area"""
    m, n = len(grid), len(grid[0])
    max_area = 0
    
    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
            return 0
        
        grid[r][c] = 0  # Mark visited
        
        area = 1
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            area += dfs(r + dr, c + dc)
        
        return area
    
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                max_area = max(max_area, dfs(r, c))
    
    return max_area


# Test
if __name__ == "__main__":
    grid = [[0,0,1,0,0],[0,1,1,0,0],[1,1,0,0,0]]
    result = maxAreaOfIsland(grid)
    print(f"Max island area: {result}")

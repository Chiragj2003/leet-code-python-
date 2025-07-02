"""
LeetCode #200 - Number of Islands
Topic: Graph / DFS / BFS
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Given a 2D grid of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and formed by connecting adjacent lands
horizontally or vertically.

Example:
[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Answer: 3 islands

Think of it like:
Looking at a map from above. Count separate land masses.

WHY THIS WORKS (Simple Explanation):
1. Scan through grid cell by cell
2. When you find land ('1'), it's part of an island
3. Use DFS/BFS to "sink" the entire island (mark as visited)
4. Count how many times you start a new DFS/BFS

Like flooding each island with water after finding it!

Time Complexity: O(rows * cols) - visit each cell
Space Complexity: O(rows * cols) for recursion in worst case
"""

def numIslands(grid):
    """
    Count islands using DFS
    
    Visual example:
    1 1 0 0
    1 1 0 0
    0 0 1 0
    0 0 0 1
    
    Start at (0,0): Find '1', start DFS to mark entire island 1
    Continue scanning: All '1's in top-left are now '0's
    Find (2,2): Find '1', start DFS for island 2
    Find (3,3): Find '1', start DFS for island 3
    
    Total: 3 islands
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    def dfs(r, c):
        """Sink the island starting at (r, c)"""
        # Boundary check and water check
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            grid[r][c] == '0'):
            return
        
        # Mark as visited (sink it)
        grid[r][c] = '0'
        
        # Explore all 4 directions
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left
    
    # Scan entire grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                # Found new island!
                islands += 1
                # Sink entire island
                dfs(r, c)
    
    return islands


def numIslands_bfs(grid):
    """
    Count islands using BFS (iterative)
    
    Same idea but using queue instead of recursion
    """
    if not grid or not grid[0]:
        return 0
    
    from collections import deque
    
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    def bfs(r, c):
        """Sink island using BFS"""
        queue = deque([(r, c)])
        grid[r][c] = '0'  # Mark as visited
        
        while queue:
            row, col = queue.popleft()
            
            # Check all 4 directions
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = row + dr, col + dc
                
                if (0 <= nr < rows and 0 <= nc < cols and 
                    grid[nr][nc] == '1'):
                    grid[nr][nc] = '0'
                    queue.append((nr, nc))
    
    # Scan grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                bfs(r, c)
    
    return islands


def numIslands_verbose(grid):
    """
    Detailed version showing the process
    """
    if not grid or not grid[0]:
        return 0
    
    # Make a copy to preserve original
    import copy
    grid = copy.deepcopy(grid)
    
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    print("Original grid:")
    for row in grid:
        print("  " + " ".join(row))
    print()
    
    def dfs(r, c, island_num):
        """Sink island and mark with island number"""
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            grid[r][c] != '1'):
            return
        
        grid[r][c] = str(island_num)  # Mark with island number
        
        dfs(r + 1, c, island_num)
        dfs(r - 1, c, island_num)
        dfs(r, c + 1, island_num)
        dfs(r, c - 1, island_num)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                print(f"Found island #{islands} at position ({r},{c})")
                dfs(r, c, islands)
                
                print(f"After marking island #{islands}:")
                for row in grid:
                    print("  " + " ".join(row))
                print()
    
    print(f"Total islands: {islands}")
    return islands


# Test cases
if __name__ == "__main__":
    test_cases = [
        (
            [
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ],
            1
        ),
        (
            [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ],
            3
        ),
        (
            [
                ["1","0","1","0","1"],
                ["0","1","0","1","0"],
                ["1","0","1","0","1"]
            ],
            13
        ),
    ]
    
    print("=== Testing DFS Solution ===")
    for grid, expected in test_cases:
        # Make copy since function modifies grid
        import copy
        grid_copy = copy.deepcopy(grid)
        
        result = numIslands(grid_copy)
        status = "✓" if result == expected else "✗"
        print(f"{status} Grid size: {len(grid)}x{len(grid[0])}")
        print(f"   Islands: {result} (Expected: {expected})")
        print()
    
    print("=== Testing BFS Solution ===")
    for grid, expected in test_cases:
        import copy
        grid_copy = copy.deepcopy(grid)
        
        result = numIslands_bfs(grid_copy)
        status = "✓" if result == expected else "✗"
        print(f"{status} Islands: {result}")
    
    print("\n" + "="*50)
    print("=== Verbose Example ===")
    grid = [
        ["1","1","0","0"],
        ["1","1","0","0"],
        ["0","0","1","0"],
        ["0","0","0","1"]
    ]
    numIslands_verbose(grid)

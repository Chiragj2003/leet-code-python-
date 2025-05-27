"""
LeetCode #994 - Rotting Oranges
Topic: Graph / BFS
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Grid with fresh (1) and rotten (2) oranges.
Every minute, rotten oranges rot adjacent fresh ones.
How many minutes until all oranges rotten?

Example:
[[2,1,1],
 [1,1,0],
 [0,1,1]]
-> 4 minutes

Think of it like:
Infection spreading through grid!

WHY THIS WORKS (Simple Explanation):
Multi-source BFS:
- Start from all rotten oranges
- Spread rot level by level
- Count levels = minutes

Time: O(m × n)
Space: O(m × n)
"""

from collections import deque

def orangesRotting(grid):
    """Find minutes to rot all oranges"""
    m, n = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    
    # Find all rotten oranges and count fresh
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1
    
    minutes = 0
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    
    # BFS
    while queue:
        r, c, time = queue.popleft()
        minutes = max(minutes, time)
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < m and 0 <= nc < n and 
                grid[nr][nc] == 1):
                grid[nr][nc] = 2
                fresh -= 1
                queue.append((nr, nc, time + 1))
    
    return minutes if fresh == 0 else -1


# Test
if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    result = orangesRotting(grid)
    print(f"Minutes to rot all: {result}")

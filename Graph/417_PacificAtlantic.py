"""
LeetCode #417 - Pacific Atlantic Water Flow
Topic: Graph / DFS
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Island where water flows to edges.
Find cells where water can reach BOTH oceans.

Pacific on top & left edges.
Atlantic on bottom & right edges.

Think of it like:
Finding high points that drain to both sides!

WHY THIS WORKS (Simple Explanation):
Work backwards from oceans!
- DFS from Pacific edge
- DFS from Atlantic edge
- Return intersection (cells reaching both)

Time: O(m × n)
Space: O(m × n)
"""

def pacificAtlantic(heights):
    """Find cells reaching both oceans"""
    if not heights:
        return []
    
    m, n = len(heights), len(heights[0])
    
    pacific = set()
    atlantic = set()
    
    def dfs(r, c, visited):
        visited.add((r, c))
        
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < m and 0 <= nc < n and 
                (nr, nc) not in visited and
                heights[nr][nc] >= heights[r][c]):
                dfs(nr, nc, visited)
    
    # DFS from Pacific edges
    for c in range(n):
        dfs(0, c, pacific)
    for r in range(m):
        dfs(r, 0, pacific)
    
    # DFS from Atlantic edges
    for c in range(n):
        dfs(m-1, c, atlantic)
    for r in range(m):
        dfs(r, n-1, atlantic)
    
    return list(pacific & atlantic)


# Test
if __name__ == "__main__":
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    result = pacificAtlantic(heights)
    print(f"Cells reaching both oceans: {result}")

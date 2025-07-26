"""
LeetCode #329 - Longest Increasing Path in Matrix
Topic: Graph / DFS + Memoization
Difficulty: Hard

PROBLEM EXPLANATION (Easy Terms):
Find longest increasing path in matrix.
Can move up/down/left/right.

Example:
[[9,9,4],
 [6,6,8],
 [2,1,1]]
-> 4 (path: 1→2→6→9)

Think of it like:
Finding longest uphill path!

WHY THIS WORKS:
DFS + memoization.
Cache longest path from each cell.

Time: O(m × n)
Space: O(m × n)
"""

def longestIncreasingPath(matrix):
    """Find longest increasing path"""
    if not matrix:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    memo = {}
    
    def dfs(r, c):
        if (r, c) in memo:
            return memo[(r, c)]
        
        length = 1
        
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < m and 0 <= nc < n and 
                matrix[nr][nc] > matrix[r][c]):
                length = max(length, 1 + dfs(nr, nc))
        
        memo[(r, c)] = length
        return length
    
    max_path = 0
    for r in range(m):
        for c in range(n):
            max_path = max(max_path, dfs(r, c))
    
    return max_path


# Test
if __name__ == "__main__":
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    result = longestIncreasingPath(matrix)
    print(f"Longest path: {result}")

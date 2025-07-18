"""
LeetCode #79 - Word Search
Topic: Backtracking / Matrix
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Find if word exists in 2D board.
Can move up/down/left/right.

Example:
board = [['A','B','C','E'],
         ['S','F','C','S'],
         ['A','D','E','E']]
word = "ABCCED" -> True

Think of it like:
Word search puzzle!

WHY THIS WORKS (Simple Explanation):
DFS + Backtracking:
- Try each cell as starting point
- Explore all 4 directions
- Mark visited, backtrack when done

Time: O(m × n × 4^L) where L is word length
Space: O(L) for recursion
"""

def exist(board, word):
    """Check if word exists in board"""
    m, n = len(board), len(board[0])
    
    def dfs(r, c, index):
        if index == len(word):
            return True
        
        if (r < 0 or r >= m or c < 0 or c >= n or 
            board[r][c] != word[index]):
            return False
        
        # Mark visited
        temp = board[r][c]
        board[r][c] = '#'
        
        # Explore 4 directions
        found = (dfs(r+1, c, index+1) or
                dfs(r-1, c, index+1) or
                dfs(r, c+1, index+1) or
                dfs(r, c-1, index+1))
        
        # Backtrack
        board[r][c] = temp
        return found
    
    # Try each cell as start
    for r in range(m):
        for c in range(n):
            if dfs(r, c, 0):
                return True
    
    return False


# Test
if __name__ == "__main__":
    board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    print(f"ABCCED exists: {exist(board, 'ABCCED')}")
    print(f"SEE exists: {exist(board, 'SEE')}")
    print(f"ABCB exists: {exist(board, 'ABCB')}")

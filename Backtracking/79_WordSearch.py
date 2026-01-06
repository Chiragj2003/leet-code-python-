"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #79 - Word Search                                 ║
║                    Topic: Backtracking                                       ║
║                    Difficulty: Medium                                         ║
║                    Company: Amazon, Meta, Microsoft                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Given m×n grid and word, return TRUE if word exists in grid.
Word can be constructed from sequential adjacent cells (horizontal/vertical).
Same cell can't be used twice.

EXAMPLES:
─────────
✓ board = [["A","B","C","E"],
           ["S","F","C","S"],
           ["A","D","E","E"]]
  
  word = "ABCCED" → TRUE
  word = "SEE"    → TRUE
  word = "ABCB"   → FALSE (can't reuse 'B')

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🎮 Maze game: Start at any letter, move up/down/left/right
   to spell your word. Can't step on same square twice!

📝 Word puzzle: Connect adjacent letters (not diagonal)
   to form the word.

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   Amazon search: validate if product name exists in
   2D warehouse layout grid.

📌 TASK:
   Search for word in grid using backtracking.
   Time O(m×n×4^L), Space O(L).

📌 ACTION:
   DFS + Backtracking:
   1. Try each cell as start
   2. Explore 4 directions
   3. Mark visited, backtrack if fail

📌 RESULT:
   ✓ Time: O(m×n×4^L) - try each cell, 4^L paths
   ✓ Space: O(L) recursion depth
   ✓ Word found efficiently

"""

# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Backtracking + DFS
# ═══════════════════════════════════════════════════════════════════════════
def exist(board, word):
    """
    Backtracking DFS to find word in grid
    
    Approach:
    1. Try each cell as starting point
    2. DFS in 4 directions
    3. Mark visited with '#', restore on backtrack
    """
    if not board or not word:
        return False
    
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c, index):
        # Success: found all letters
        if index == len(word):
            return True
        
        # Out of bounds or wrong letter
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            board[r][c] != word[index]):
            return False
        
        # Mark as visited
        temp = board[r][c]
        board[r][c] = '#'
        
        # Explore 4 directions
        found = (dfs(r + 1, c, index + 1) or  # Down
                 dfs(r - 1, c, index + 1) or  # Up
                 dfs(r, c + 1, index + 1) or  # Right
                 dfs(r, c - 1, index + 1))    # Left
        
        # Backtrack: restore cell
        board[r][c] = temp
        
        return found
    
    # Try each cell as starting point
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    
    return False


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE - With Visited Set
# ═══════════════════════════════════════════════════════════════════════════
def exist_with_set(board, word):
    """
    Use separate visited set instead of modifying board
    """
    if not board or not word:
        return False
    
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c, index, visited):
        if index == len(word):
            return True
        
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            (r, c) in visited or board[r][c] != word[index]):
            return False
        
        visited.add((r, c))
        
        found = (dfs(r + 1, c, index + 1, visited) or
                 dfs(r - 1, c, index + 1, visited) or
                 dfs(r, c + 1, index + 1, visited) or
                 dfs(r, c - 1, index + 1, visited))
        
        visited.remove((r, c))
        
        return found
    
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0, set()):
                return True
    
    return False


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    
    test_cases = [
        "ABCCED",  # True
        "SEE",     # True
        "ABCB",    # False
    ]
    
    print("=" * 70)
    print("🧪 TESTING WORD SEARCH")
    print("=" * 70)
    
    for word in test_cases:
        # Need fresh copies
        board1 = [row[:] for row in board]
        board2 = [row[:] for row in board]
        
        result1 = exist(board1, word)
        result2 = exist_with_set(board2, word)
        
        print(f"\nWord: '{word}'")
        print(f"Method 1: {result1}")
        print(f"Method 2: {result2}")

"""
LeetCode #212 - Word Search II
Topic: Trie / Backtracking
Difficulty: Hard

PROBLEM EXPLANATION (Easy Terms):
Find all words from dictionary in board.

Example:
board = [['o','a','a','n'],
         ['e','t','a','e'],
         ['i','h','k','r'],
         ['i','f','l','v']]
words = ["oath","pea","eat","rain"]
-> ["eat","oath"]

Think of it like:
Multi-word search puzzle!

WHY THIS WORKS:
Build trie from words, then DFS on board.
Prune using trie!

Time: O(m × n × 4^L)
Space: O(k) where k is total characters in words
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


def findWords(board, words):
    """Find all words in board"""
    # Build trie
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word
    
    m, n = len(board), len(board[0])
    result = []
    
    def dfs(r, c, node):
        char = board[r][c]
        if char not in node.children:
            return
        
        next_node = node.children[char]
        if next_node.word:
            result.append(next_node.word)
            next_node.word = None  # Avoid duplicates
        
        board[r][c] = '#'  # Mark visited
        
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != '#':
                dfs(nr, nc, next_node)
        
        board[r][c] = char  # Backtrack
    
    # Try each cell as start
    for r in range(m):
        for c in range(n):
            dfs(r, c, root)
    
    return result


# Test
if __name__ == "__main__":
    board = [['o','a','a','n'],
             ['e','t','a','e'],
             ['i','h','k','r'],
             ['i','f','l','v']]
    words = ["oath","pea","eat","rain"]
    result = findWords(board, words)
    print(f"Found words: {result}")

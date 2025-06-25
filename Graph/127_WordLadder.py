"""
LeetCode #127 - Word Ladder
Topic: Graph / BFS
Difficulty: Hard

PROBLEM EXPLANATION (Easy Terms):
Transform beginWord to endWord, changing one letter at a time.
Each intermediate word must be in wordList.

Example:
beginWord = "hit", endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Shortest: 5 ("hit" -> "hot" -> "dot" -> "dog" -> "cog")

Think of it like:
Shortest path through word transformations!

WHY THIS WORKS (Simple Explanation):
BFS to find shortest path:
- Try changing each character
- Check if new word in wordList
- Find shortest sequence

Time: O(m² × n) where m is word length, n is wordList size
Space: O(m × n)
"""

from collections import deque

def ladderLength(beginWord, endWord, wordList):
    """Find shortest transformation sequence"""
    if endWord not in wordList:
        return 0
    
    wordSet = set(wordList)
    queue = deque([(beginWord, 1)])
    visited = {beginWord}
    
    while queue:
        word, steps = queue.popleft()
        
        if word == endWord:
            return steps
        
        # Try changing each character
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                
                if new_word in wordSet and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, steps + 1))
    
    return 0


# Test
if __name__ == "__main__":
    result = ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
    print(f"Shortest path: {result} steps")

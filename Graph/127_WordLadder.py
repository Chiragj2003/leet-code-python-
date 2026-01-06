"""
LeetCode #127 - Word Ladder | ENHANCED COMPLETE SOLUTION
Topic: Graph / BFS | Difficulty: Hard

PROBLEM STATEMENT:
Given two words, beginWord and endWord, and a dictionary wordList, return the 
number of words in the SHORTEST TRANSFORMATION SEQUENCE from beginWord to endWord, 
or 0 if no such sequence exists. You can only change ONE letter at a time, and each 
intermediate word must exist in wordList.

KEY EXAMPLES:
  "hit" → "cog" via ["hot","dot","dog","lot","log","cog"] = 5 (hit→hot→dot→dog→cog)
  "hit" → "cog" via ["hot","dot","dog","lot","log"] = 0 (cog not in list)
  "a" → "c" via ["a","b","c"] = 2 (a→c)

DETAILED EXPLANATION:
This is a SHORTEST PATH problem in an implicit graph where each WORD is a NODE and 
two words are CONNECTED if they differ by exactly ONE LETTER.

Why BFS?
- Explores level by level (distance by distance)
- First time we reach endWord = SHORTEST path found!
- Optimal for unweighted graphs

Core Algorithm:
1. Return 0 if endWord not in wordList
2. Create SET from wordList for O(1) lookups
3. BFS: initialize queue with (beginWord, 1)
4. For each word: try changing each character to a-z
5. Add valid unvisited neighbors to queue
6. Return steps when we reach endWord

COMPLEXITY:
Time:  O(N × L² × 26) where N = wordList size, L = word length
Space: O(N × L) for visited set and queue

KEY INSIGHTS:
- Set lookup is O(1) vs O(n) for list - CRUCIAL!
- Mark visited immediately to prevent cycles
- BFS guarantees shortest path in unweighted graph
- Bidirectional BFS is 2-3× faster for large inputs

EDGE CASES:
- beginWord == endWord → return 1
- endWord not in wordList → return 0
- beginWord not in wordList but reachable → still works!
- No valid path → return 0
"""

from collections import deque

# ★ STANDARD SOLUTION - BFS (Interview Ready)
def ladderLength(beginWord, endWord, wordList):
    """
    Classic BFS solution. Clean, easy to explain, optimal.
    
    Time: O(N × L² × 26)  | Space: O(N × L)
    """
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
                if c == word[i]:
                    continue
                new_word = word[:i] + c + word[i+1:]
                
                if new_word in wordSet and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, steps + 1))
    
    return 0


# ★ BIDIRECTIONAL BFS - 2-3× Faster!
def ladderLength_bidirectional(beginWord, endWord, wordList):
    """
    Search from BOTH ends simultaneously.
    
    Key: Always expand smaller frontier for best performance.
    Explores ~2×b^(d/2) nodes instead of b^d nodes.
    
    Time: O(N × L² × 26) with better constants | Space: O(N × L)
    """
    if endWord not in wordList:
        return 0
    
    wordSet = set(wordList)
    begin_set, end_set = {beginWord}, {endWord}
    visited = {beginWord, endWord}
    steps = 1
    
    def get_neighbors(word):
        neighbors = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c != word[i]:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in wordSet:
                        neighbors.append(new_word)
        return neighbors
    
    while begin_set and end_set:
        if len(begin_set) > len(end_set):
            begin_set, end_set = end_set, begin_set
        
        steps += 1
        next_set = set()
        
        for word in begin_set:
            for neighbor in get_neighbors(word):
                if neighbor in end_set:
                    return steps
                if neighbor not in visited:
                    visited.add(neighbor)
                    next_set.add(neighbor)
        
        begin_set = next_set
    
    return 0


# ★ WITH PATH TRACKING - For Debugging
def ladderLength_with_path(beginWord, endWord, wordList):
    """
    Returns (steps, path) - useful for debugging and verification.
    """
    if endWord not in wordList:
        return 0, []
    
    wordSet = set(wordList)
    queue = deque([(beginWord, 1, [beginWord])])
    visited = {beginWord}
    
    while queue:
        word, steps, path = queue.popleft()
        
        if word == endWord:
            return steps, path
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c == word[i]:
                    continue
                new_word = word[:i] + c + word[i+1:]
                
                if new_word in wordSet and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, steps + 1, path + [new_word]))
    
    return 0, []


# COMPREHENSIVE TEST CASES
if __name__ == "__main__":
    tests = [
        ("hit", "cog", ["hot","dot","dog","lot","log","cog"], 5),
        ("hit", "cog", ["hot","dot","dog","lot","log"], 0),
        ("a", "c", ["a","b","c"], 2),
        ("red", "tax", ["red","ted","tex","tax"], 4),
    ]
    
    print("="*70)
    print("LeetCode #127 - Word Ladder Solutions")
    print("="*70)
    
    print("\n✓ Standard BFS:")
    for b, e, w, exp in tests:
        r = ladderLength(b, e, w)
        print(f"  {r} (expected {exp}) {'✓' if r==exp else '✗'}")
    
    print("\n✓ Bidirectional BFS:")
    for b, e, w, exp in tests:
        r = ladderLength_bidirectional(b, e, w)
        print(f"  {r} (expected {exp}) {'✓' if r==exp else '✗'}")
    
    print("\n✓ With Path:")
    r, p = ladderLength_with_path("hit", "cog", ["hot","dot","dog","lot","log","cog"])
    print(f"  Path: {' → '.join(p)} ({r} steps)")

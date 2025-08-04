"""
LeetCode #211 - Design Add and Search Words Data Structure
Topic: Trie / Backtracking
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Trie with wildcard search!
'.' matches any character.

Example:
add("bad"), add("dad"), add("mad")
search(".ad") -> true
search("b..") -> true

Think of it like:
Dictionary with pattern matching!

WHY THIS WORKS:
Use trie + DFS for wildcards.

Time: O(m) for add, O(n) for search worst case
Space: O(n × m)
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        """Add word to trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        """Search with wildcards"""
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            
            char = word[i]
            
            if char == '.':
                # Try all children
                return any(dfs(child, i + 1) 
                          for child in node.children.values())
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)
        
        return dfs(self.root, 0)


# Test
if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    print(f"Search '.ad': {wd.search('.ad')}")
    print(f"Search 'b..': {wd.search('b..')}")

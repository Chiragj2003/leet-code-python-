"""
LeetCode #208 - Implement Trie (Prefix Tree)
Topic: Trie / Design
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Build prefix tree (Trie) for efficient word storage/search.

Operations:
- insert(word)
- search(word)
- startsWith(prefix)

Think of it like:
Dictionary with fast prefix lookups!

WHY THIS WORKS:
Tree where each node = letter.
Path from root = word/prefix.

Time: O(m) where m is word length
Space: O(n × m)
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Insert word into trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        """Search for exact word"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def startsWith(self, prefix):
        """Check if prefix exists"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Test
if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(f"Search 'apple': {trie.search('apple')}")
    print(f"Search 'app': {trie.search('app')}")
    print(f"Starts with 'app': {trie.startsWith('app')}")

"""
LeetCode #387 - First Unique Character in a String
Topic: Hashmap
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Find the first character in a string that appears only once.
Return its index, or -1 if no such character exists.

Example:
Input: s = "leetcode"
Output: 0
Explanation: 'l' appears only once and is the first such character

WHY THIS WORKS (Simple Explanation):
Two passes approach:
1. First pass: Count how many times each character appears (use hashmap)
2. Second pass: Find first character with count = 1

Why two passes? Because we need to know all frequencies before deciding!

Time Complexity: O(n) - two passes through string
Space Complexity: O(1) - at most 26 lowercase letters
"""

from collections import Counter

def firstUniqChar(s):
    """
    Find index of first unique (non-repeating) character
    
    Easy approach:
    1. Count all characters: {'l':1, 'e':3, 't':1, 'c':1, 'o':1, 'd':1}
    2. Go through string again, find first character with count 1
    """
    # Count frequency of each character
    char_count = Counter(s)
    
    # Find first character with count = 1
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    
    # No unique character found
    return -1


# Manual approach without Counter
def firstUniqChar_manual(s):
    """
    Same logic but without using Counter library
    """
    # Count frequencies manually
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find first unique character
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    
    return -1


# Test cases with explanations
if __name__ == "__main__":
    test1 = "leetcode"
    print(f"Test 1: {firstUniqChar(test1)}")
    # Expected: 0
    # Counts: l=1, e=3, t=1, c=1, o=1, d=1
    # First unique: 'l' at index 0
    
    test2 = "loveleetcode"
    print(f"Test 2: {firstUniqChar(test2)}")
    # Expected: 2
    # Counts: l=2, o=2, v=1, e=4, t=1, c=1, d=1
    # First unique: 'v' at index 2
    
    test3 = "aabb"
    print(f"Test 3: {firstUniqChar(test3)}")
    # Expected: -1
    # All characters repeat

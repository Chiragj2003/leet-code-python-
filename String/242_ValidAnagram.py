"""
LeetCode #242 - Valid Anagram
Topic: String / Hashmap
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Check if two strings are anagrams.

Example:
"anagram" and "nagaram" -> True
"rat" and "car" -> False

Think of it like:
Same letters, different order!

WHY THIS WORKS:
Count characters - must be identical!

Time: O(n)
Space: O(1) - at most 26 letters
"""

from collections import Counter

def isAnagram(s, t):
    """Check if strings are anagrams"""
    return Counter(s) == Counter(t)


# Test
if __name__ == "__main__":
    tests = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
    ]
    
    for s, t, exp in tests:
        result = isAnagram(s, t)
        print(f'"{s}" & "{t}" -> {result} (expected {exp})')

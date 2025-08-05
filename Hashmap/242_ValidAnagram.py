"""
LeetCode #242 - Valid Anagram
Topic: Hashmap
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Two strings are anagrams if they use the same letters with same frequencies.
Like "listen" and "silent" - same letters, just rearranged!

Example:
Input: s = "anagram", t = "nagaram"
Output: true

WHY THIS WORKS (Simple Explanation):
Count the frequency of each character in both strings.
If the frequency maps are identical, they're anagrams!

Alternative: Sort both strings and compare - if same, they're anagrams.

Time Complexity: O(n) - count characters once
Space Complexity: O(1) - at most 26 letters
"""

from collections import Counter

def isAnagram(s, t):
    """
    Check if two strings are anagrams
    
    Easiest approach:
    1. Count characters in s: {'a':3, 'n':1, 'g':1, 'r':1, 'm':1}
    2. Count characters in t: {'n':1, 'a':3, 'g':1, 'r':1, 'm':1}
    3. Compare the counts - if same, it's an anagram!
    """
    # Different lengths = can't be anagrams
    if len(s) != len(t):
        return False
    
    # Count and compare
    return Counter(s) == Counter(t)


# Alternative: Using sorting
def isAnagram_sort(s, t):
    """
    Sort both strings and compare
    If sorted strings are same, they're anagrams
    
    Example: "anagram" -> "aaagmnr"
             "nagaram" -> "aaagmnr"
    Same! So they're anagrams.
    """
    return sorted(s) == sorted(t)


# Alternative: Manual counting without Counter
def isAnagram_manual(s, t):
    """
    Count manually using dictionary
    """
    if len(s) != len(t):
        return False
    
    # Count characters in s
    count_s = {}
    for char in s:
        count_s[char] = count_s.get(char, 0) + 1
    
    # Count characters in t
    count_t = {}
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1
    
    # Compare
    return count_s == count_t


# Test cases with explanations
if __name__ == "__main__":
    test1_s = "anagram"
    test1_t = "nagaram"
    print(f"Test 1: {isAnagram(test1_s, test1_t)}")
    # Expected: True
    # Both have: a=3, n=1, g=1, r=1, m=1
    
    test2_s = "rat"
    test2_t = "car"
    print(f"Test 2: {isAnagram(test2_s, test2_t)}")
    # Expected: False
    # "rat" has 'r', "car" has 'c' - different letters
    
    test3_s = "listen"
    test3_t = "silent"
    print(f"Test 3: {isAnagram(test3_s, test3_t)}")
    # Expected: True
    # Classic anagram example!

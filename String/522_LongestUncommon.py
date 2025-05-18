"""
LeetCode #522 - Longest Uncommon Subsequence II
Topic: String
Difficulty: Medium

PROBLEM EXPLANATION:
Given an array of strings, find the length of the longest uncommon subsequence.
An uncommon subsequence is a string that is a subsequence of one string but not
a subsequence of any other string in the array.

Example:
Input: strs = ["aba","cdc","eae"]
Output: 3 (each string is not subsequence of others)

APPROACH:
1. Sort strings by length (longest first)
2. For each string, check if it's a subsequence of any other string
3. If not, it's uncommon - return its length
4. Special case: if string appears multiple times, skip it

Time Complexity: O(n² * m) where m is avg string length
Space Complexity: O(n)
"""

def findLUSlength(strs):
    def is_subsequence(s, t):
        """Check if s is subsequence of t"""
        i = 0
        for char in t:
            if i < len(s) and s[i] == char:
                i += 1
        return i == len(s)
    
    # Sort by length (descending)
    strs.sort(key=len, reverse=True)
    
    for i, s in enumerate(strs):
        # Check if s appears multiple times
        if strs.count(s) > 1:
            continue
        
        # Check if s is subsequence of any other string
        is_uncommon = True
        for j, t in enumerate(strs):
            if i != j and is_subsequence(s, t):
                is_uncommon = False
                break
        
        if is_uncommon:
            return len(s)
    
    return -1


# Test cases
if __name__ == "__main__":
    test1 = ["aba", "cdc", "eae"]
    print(f"Test 1: {findLUSlength(test1)}")  # Expected: 3
    
    test2 = ["aaa", "aaa", "aa"]
    print(f"Test 2: {findLUSlength(test2)}")  # Expected: -1

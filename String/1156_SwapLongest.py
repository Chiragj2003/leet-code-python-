"""
LeetCode #1156 - Swap For Longest Repeated Character Substring
Topic: String / Sliding Window
Difficulty: Medium

PROBLEM EXPLANATION:
Given a string, you can swap two characters at most once.
Return the length of the longest substring with repeating characters.

Example:
Input: text = "ababa"
Output: 3
Explanation: Swap first 'b' with last 'a': "aaaab" -> "aaa" = 3

Input: text = "aaabbaaa"
Output: 4
Explanation: Swap middle 'b' with 'a': 4 consecutive 'a's

APPROACH:
1. For each character, find all blocks of that character
2. Check if we can extend a block by swapping
3. Can extend if: adjacent blocks with 1 different char between, or extra char available

Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import Counter

def maxRepOpt1(text):
    """
    Returns length of longest repeating substring after one swap
    """
    # Count total occurrences of each character
    count = Counter(text)
    
    # Group consecutive characters
    groups = []
    i = 0
    while i < len(text):
        j = i
        while j < len(text) and text[j] == text[i]:
            j += 1
        groups.append((text[i], j - i))
        i = j
    
    max_len = max(count.values())  # At least we can get this
    
    # Check each group
    for i in range(len(groups)):
        char, length = groups[i]
        
        # Case 1: Extend current group by 1 if extra char available
        if count[char] > length:
            max_len = max(max_len, length + 1)
        
        # Case 2: Merge two groups separated by single different char
        if i + 2 < len(groups) and groups[i+2][0] == char and groups[i+1][1] == 1:
            total = groups[i][1] + groups[i+2][1]
            # Can merge + 1 if extra char available
            if count[char] > total:
                max_len = max(max_len, total + 1)
            else:
                max_len = max(max_len, total)
    
    return max_len


# Test cases
if __name__ == "__main__":
    print(f"Test 1: {maxRepOpt1('ababa')}")  # Expected: 3
    print(f"Test 2: {maxRepOpt1('aaabbaaa')}")  # Expected: 4
    print(f"Test 3: {maxRepOpt1('aaaa')}")  # Expected: 4
    print(f"Test 4: {maxRepOpt1('abcdef')}")  # Expected: 1

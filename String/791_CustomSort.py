"""
LeetCode #791 - Custom Sort String
Topic: String
Difficulty: Medium

PROBLEM EXPLANATION:
You are given two strings order and s. All characters in order are unique
and sorted in some custom order. Permute the characters of s so that they
match the order that order was sorted. Return any permutation of s that satisfies this.

Example:
Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: "c", "b", "a" appear in order, so they're first. "d" doesn't appear, so it's last.

APPROACH:
1. Count frequency of each character in s
2. Build result by iterating through order
3. For each char in order, add all occurrences from s
4. Add remaining characters not in order

Time Complexity: O(n + m)
Space Complexity: O(n)
"""

from collections import Counter

def customSortString(order, s):
    """
    Returns s sorted according to order
    """
    # Count frequency of characters in s
    count = Counter(s)
    result = []
    
    # Add characters in the order specified
    for char in order:
        if char in count:
            result.append(char * count[char])
            del count[char]
    
    # Add remaining characters
    for char, freq in count.items():
        result.append(char * freq)
    
    return ''.join(result)


# Test cases
if __name__ == "__main__":
    test1 = customSortString("cba", "abcd")
    print(f"Test 1: {test1}")  # Expected: "cbad"
    
    test2 = customSortString("bcafg", "abcd")
    print(f"Test 2: {test2}")  # Expected: "bcad"
    
    test3 = customSortString("kqep", "pekeq")
    print(f"Test 3: {test3}")  # Expected: "kqeep"

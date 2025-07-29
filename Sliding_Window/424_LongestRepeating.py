"""
LeetCode #424 - Longest Repeating Character Replacement
Topic: Sliding Window
Difficulty: Medium

PROBLEM EXPLANATION:
Given a string s and an integer k, you can replace at most k characters
with any other character. Return the length of the longest substring
containing the same letter you can get.

Example:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace two 'B's with 'A's -> "AAAA"

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace one 'B' with 'A' -> "AABA" or "ABAA" (length 4)

APPROACH (Sliding Window):
1. Use sliding window with character frequency counter
2. Expand window by adding character
3. If (window_size - most_frequent_char_count) > k, shrink window
4. Track maximum window size

Key insight: In a valid window, we can replace (window_size - max_frequency) characters

Time Complexity: O(n)
Space Complexity: O(1) - only 26 letters
"""

from collections import Counter

def characterReplacement(s, k):
    """
    Returns length of longest repeating character substring after k replacements
    """
    count = Counter()
    max_length = 0
    max_freq = 0  # Frequency of most common character in window
    left = 0
    
    for right in range(len(s)):
        # Add character to window
        count[s[right]] += 1
        max_freq = max(max_freq, count[s[right]])
        
        # Check if window is valid
        window_size = right - left + 1
        
        # If we need to replace more than k characters, shrink window
        if window_size - max_freq > k:
            count[s[left]] -= 1
            left += 1
        
        # Update max length
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Test cases
if __name__ == "__main__":
    print(f"Test 1: {characterReplacement('ABAB', 2)}")  # Expected: 4
    print(f"Test 2: {characterReplacement('AABABBA', 1)}")  # Expected: 4
    print(f"Test 3: {characterReplacement('ABAA', 0)}")  # Expected: 2
    print(f"Test 4: {characterReplacement('AAAA', 2)}")  # Expected: 4

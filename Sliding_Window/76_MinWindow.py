"""
LeetCode #76 - Minimum Window Substring
Topic: Sliding Window / String
Difficulty: Hard

PROBLEM EXPLANATION (Easy Terms):
Find minimum window in s that contains all characters of t.

Example:
s = "ADOBECODEBANC", t = "ABC"
-> "BANC"

Think of it like:
Finding smallest substring with all required letters!

WHY THIS WORKS:
Sliding window with character counts.

Time: O(m + n)
Space: O(m + n)
"""

from collections import Counter

def minWindow(s, t):
    """Find minimum window substring"""
    if not s or not t:
        return ""
    
    need = Counter(t)
    have = {}
    required = len(need)
    formed = 0
    
    l, r = 0, 0
    min_len = float('inf')
    min_window = (0, 0)
    
    while r < len(s):
        char = s[r]
        have[char] = have.get(char, 0) + 1
        
        if char in need and have[char] == need[char]:
            formed += 1
        
        while l <= r and formed == required:
            if r - l + 1 < min_len:
                min_len = r - l + 1
                min_window = (l, r)
            
            char = s[l]
            have[char] -= 1
            if char in need and have[char] < need[char]:
                formed -= 1
            l += 1
        
        r += 1
    
    l, r = min_window
    return s[l:r+1] if min_len != float('inf') else ""


# Test
if __name__ == "__main__":
    result = minWindow("ADOBECODEBANC", "ABC")
    print(f'Minimum window: "{result}"')

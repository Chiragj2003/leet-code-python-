"""
LeetCode #3 - Longest Substring Without Repeating Characters
Topic: Sliding Window
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Find the length of the longest substring that has NO repeating characters.

Example:
"abcabcbb" -> "abc" (length 3)
"bbbbb" -> "b" (length 1)
"pwwkew" -> "wke" (length 3)

Think of it like:
You're collecting unique items. When you find a duplicate, you must
throw away items from the start until the duplicate is gone.

WHY THIS WORKS (Simple Explanation):
Use a "sliding window" (a flexible substring):
1. Expand window by adding characters
2. If duplicate found, shrink window from left
3. Track the maximum window size seen

Use a set to quickly check for duplicates!

Time Complexity: O(n) - each character visited at most twice
Space Complexity: O(min(n, 26)) - set stores unique characters
"""

def lengthOfLongestSubstring(s):
    """
    Find length of longest substring without repeating characters
    
    Visual example for "abcabcbb":
    
    a: window="a", chars={'a'}, max_len=1
    b: window="ab", chars={'a','b'}, max_len=2
    c: window="abc", chars={'a','b','c'}, max_len=3
    a: duplicate! remove from left until 'a' gone
       window="bca", chars={'b','c','a'}, max_len=3
    b: duplicate! shrink...
       window="cab", chars={'c','a','b'}, max_len=3
    c: duplicate! shrink...
       window="abc", chars={'a','b','c'}, max_len=3
    """
    # Track characters in current window
    char_set = set()
    left = 0  # Left pointer of window
    max_length = 0
    
    # Expand window with right pointer
    for right in range(len(s)):
        # If duplicate found, shrink window from left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character to window
        char_set.add(s[right])
        
        # Update maximum length
        max_length = max(max_length, right - left + 1)
    
    return max_length


def lengthOfLongestSubstring_hashmap(s):
    """
    Alternative solution using hashmap to store last seen index
    This allows jumping left pointer directly!
    
    Example "abcabcbb":
    last_seen = {}
    
    'a' at 0: last_seen={'a':0}, window=1, max=1
    'b' at 1: last_seen={'a':0,'b':1}, window=2, max=2
    'c' at 2: last_seen={'a':0,'b':1,'c':2}, window=3, max=3
    'a' at 3: 'a' seen at 0! Jump left to 1
              last_seen={'a':3,'b':1,'c':2}, window=3, max=3
    """
    last_seen = {}  # char -> last seen index
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # If character seen and within current window
        if s[right] in last_seen and last_seen[s[right]] >= left:
            # Jump left pointer to after the duplicate
            left = last_seen[s[right]] + 1
        
        # Update last seen position
        last_seen[s[right]] = right
        
        # Update max length
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Test cases with detailed output
if __name__ == "__main__":
    test_cases = [
        ("abcabcbb", 3),  # "abc"
        ("bbbbb", 1),     # "b"
        ("pwwkew", 3),    # "wke"
        ("", 0),          # empty string
        ("dvdf", 3),      # "vdf"
        ("abba", 2),      # "ab" or "ba"
    ]
    
    print("=== Testing Sliding Window Solution ===")
    for s, expected in test_cases:
        result = lengthOfLongestSubstring(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: '{s}' -> Output: {result} (Expected: {expected})")
    
    print("\n=== Testing Hashmap Solution ===")
    for s, expected in test_cases:
        result = lengthOfLongestSubstring_hashmap(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: '{s}' -> Output: {result} (Expected: {expected})")

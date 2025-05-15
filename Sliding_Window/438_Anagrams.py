"""
LeetCode #438 - Find All Anagrams in a String
Topic: Sliding Window
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Find all starting positions of p's anagrams in string s.

Example:
s = "cbaebabacd", p = "abc"
Output: [0, 6]
Explanation:
- Substring at index 0 is "cba" (anagram of "abc")
- Substring at index 6 is "bac" (anagram of "abc")

Think of it like:
Slide a window of size len(p) across s.
At each position, check if the window contains same letters as p.

WHY THIS WORKS (Simple Explanation):
Anagram = same letters with different arrangement
So we need same CHARACTER FREQUENCIES!

Use sliding window:
1. Count frequencies in p
2. Slide window of size len(p) through s
3. When window frequencies match p -> found anagram!

Time Complexity: O(n) where n = len(s)
Space Complexity: O(1) - only 26 letters
"""

from collections import Counter

def findAnagrams(s, p):
    """
    Find all start indices of p's anagrams in s
    
    Visual example:
    s = "cbaebabacd", p = "abc"
    p_count = {'a':1, 'b':1, 'c':1}
    
    Window [0:3] "cba": {'c':1,'b':1,'a':1} ✓ Match! -> add 0
    Window [1:4] "bae": {'b':1,'a':1,'e':1} ✗
    Window [2:5] "aeb": {'a':1,'e':1,'b':1} ✗
    Window [3:6] "eba": {'e':1,'b':1,'a':1} ✗
    Window [4:7] "bab": {'b':2,'a':1} ✗
    Window [5:8] "aba": {'a':2,'b':1} ✗
    Window [6:9] "bac": {'b':1,'a':1,'c':1} ✓ Match! -> add 6
    """
    result = []
    
    if len(p) > len(s):
        return result
    
    # Count character frequencies in p
    p_count = Counter(p)
    window_count = Counter()
    
    # Initialize first window
    window_size = len(p)
    for i in range(window_size):
        window_count[s[i]] += 1
    
    # Check first window
    if window_count == p_count:
        result.append(0)
    
    # Slide the window
    for i in range(window_size, len(s)):
        # Add new character on right
        window_count[s[i]] += 1
        
        # Remove leftmost character
        left_char = s[i - window_size]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]
        
        # Check if current window is anagram
        if window_count == p_count:
            result.append(i - window_size + 1)
    
    return result


def findAnagrams_array(s, p):
    """
    Alternative: Use arrays instead of Counter
    Slightly faster for small alphabets
    """
    result = []
    
    if len(p) > len(s):
        return result
    
    # Frequency arrays
    p_count = [0] * 26
    s_count = [0] * 26
    
    # Count frequencies in p and first window
    for i in range(len(p)):
        p_count[ord(p[i]) - ord('a')] += 1
        s_count[ord(s[i]) - ord('a')] += 1
    
    # Check first window
    if p_count == s_count:
        result.append(0)
    
    # Slide window
    for i in range(len(p), len(s)):
        # Add right character
        s_count[ord(s[i]) - ord('a')] += 1
        
        # Remove left character
        s_count[ord(s[i - len(p)]) - ord('a')] -= 1
        
        # Check if match
        if p_count == s_count:
            result.append(i - len(p) + 1)
    
    return result


# Test cases with detailed walkthrough
if __name__ == "__main__":
    test_cases = [
        ("cbaebabacd", "abc", [0, 6]),
        ("abab", "ab", [0, 1, 2]),
        ("baa", "aa", [1]),
        ("", "a", []),
        ("a", "a", [0]),
    ]
    
    print("=== Testing Counter Solution ===")
    for s, p, expected in test_cases:
        result = findAnagrams(s, p)
        status = "✓" if result == expected else "✗"
        print(f"{status} s='{s}', p='{p}'")
        print(f"   Output: {result}")
        print(f"   Expected: {expected}")
        print()
    
    print("=== Testing Array Solution ===")
    for s, p, expected in test_cases:
        result = findAnagrams_array(s, p)
        status = "✓" if result == expected else "✗"
        print(f"{status} s='{s}', p='{p}'")
        print(f"   Output: {result}")
        print(f"   Expected: {expected}")
        print()

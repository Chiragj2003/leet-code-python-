"""
LeetCode #567 - Permutation in String
Topic: Sliding Window
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Check if s2 contains any permutation of s1.

Example:
s1 = "ab", s2 = "eidbaooo" -> True (contains "ba" which is permutation of "ab")
s1 = "ab", s2 = "eidboaoo" -> False

Think of it like:
You're looking for any arrangement of letters from s1 inside s2.
"ab" can be arranged as "ab" or "ba" - find either in s2!

WHY THIS WORKS (Simple Explanation):
Use a sliding window of size len(s1):
1. Count frequency of characters in s1
2. Slide window through s2
3. If window has same character frequencies -> found permutation!

Optimization: Track "matches" count instead of comparing entire frequency maps

Time Complexity: O(n) where n is length of s2
Space Complexity: O(1) - only 26 letters in alphabet
"""

from collections import Counter

def checkInclusion(s1, s2):
    """
    Check if s2 contains permutation of s1
    
    Visual example:
    s1 = "ab", s2 = "eidbaooo"
    
    s1_count = {'a':1, 'b':1}
    
    Window "ei": {'e':1, 'i':1} ✗
    Window "id": {'i':1, 'd':1} ✗
    Window "db": {'d':1, 'b':1} ✗
    Window "ba": {'b':1, 'a':1} ✓ Match!
    """
    if len(s1) > len(s2):
        return False
    
    # Count characters in s1
    s1_count = Counter(s1)
    window_count = Counter()
    
    # Initialize first window
    window_size = len(s1)
    for i in range(window_size):
        window_count[s2[i]] += 1
    
    # Check if first window matches
    if window_count == s1_count:
        return True
    
    # Slide the window
    for i in range(window_size, len(s2)):
        # Add new character
        window_count[s2[i]] += 1
        
        # Remove leftmost character
        left_char = s2[i - window_size]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]
        
        # Check if current window matches
        if window_count == s1_count:
            return True
    
    return False


def checkInclusion_optimized(s1, s2):
    """
    Optimized: Track number of matching character frequencies
    
    Instead of comparing entire dictionaries, track how many
    characters have matching frequencies.
    When matches == 26, we found a permutation!
    """
    if len(s1) > len(s2):
        return False
    
    # Frequency arrays for 26 letters
    s1_count = [0] * 26
    s2_count = [0] * 26
    
    # Count frequencies in first window
    for i in range(len(s1)):
        s1_count[ord(s1[i]) - ord('a')] += 1
        s2_count[ord(s2[i]) - ord('a')] += 1
    
    # Count how many characters have matching frequencies
    matches = 0
    for i in range(26):
        if s1_count[i] == s2_count[i]:
            matches += 1
    
    # Slide the window
    left = 0
    for right in range(len(s1), len(s2)):
        if matches == 26:
            return True
        
        # Add right character
        index = ord(s2[right]) - ord('a')
        s2_count[index] += 1
        if s2_count[index] == s1_count[index]:
            matches += 1
        elif s2_count[index] == s1_count[index] + 1:
            matches -= 1
        
        # Remove left character
        index = ord(s2[left]) - ord('a')
        s2_count[index] -= 1
        if s2_count[index] == s1_count[index]:
            matches += 1
        elif s2_count[index] == s1_count[index] - 1:
            matches -= 1
        
        left += 1
    
    return matches == 26


# Test cases with explanations
if __name__ == "__main__":
    test_cases = [
        ("ab", "eidbaooo", True),   # "ba" is permutation of "ab"
        ("ab", "eidboaoo", False),  # no permutation found
        ("a", "ab", True),          # "a" found
        ("abc", "bbbca", True),     # "bca" is permutation
        ("hello", "ooolleoooleh", False),  # no valid window
    ]
    
    print("=== Testing Basic Solution ===")
    for s1, s2, expected in test_cases:
        result = checkInclusion(s1, s2)
        status = "✓" if result == expected else "✗"
        print(f"{status} s1='{s1}', s2='{s2}' -> {result} (Expected: {expected})")
    
    print("\n=== Testing Optimized Solution ===")
    for s1, s2, expected in test_cases:
        result = checkInclusion_optimized(s1, s2)
        status = "✓" if result == expected else "✗"
        print(f"{status} s1='{s1}', s2='{s2}' -> {result} (Expected: {expected})")

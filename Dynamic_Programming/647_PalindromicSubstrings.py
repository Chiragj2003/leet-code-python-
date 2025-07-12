"""
LeetCode #647 - Palindromic Substrings
Topic: Dynamic Programming / String
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Count all palindromic substrings.

Example:
"abc" -> 3 ("a", "b", "c")
"aaa" -> 6 ("a", "a", "a", "aa", "aa", "aaa")

Think of it like:
Finding all mirror-image substrings!

WHY THIS WORKS (Simple Explanation):
Expand around center:
- Each char is center (odd length)
- Between chars is center (even length)

Time: O(n²)
Space: O(1)
"""

def countSubstrings(s):
    """Count palindromic substrings"""
    count = 0
    
    def expand(left, right):
        nonlocal count
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
    
    for i in range(len(s)):
        expand(i, i)      # Odd length
        expand(i, i + 1)  # Even length
    
    return count


# Test
if __name__ == "__main__":
    tests = [
        ("abc", 3),
        ("aaa", 6),
    ]
    
    for s, exp in tests:
        result = countSubstrings(s)
        print(f'"{s}" -> {result} palindromes (expected {exp})')

"""

                 LeetCode #242 - Valid Anagram                                
                 Topic: String/HashMap | Difficulty: Easy                     
                 Company: Amazon, Meta, Microsoft                             


PROBLEM: Check if two strings are anagrams (same chars, different order).

Examples:
  "anagram", "nagaram"  True
  "rat", "car"  False
"""

from collections import Counter

#  SOLUTION 1: Sort and Compare (OPTIMAL for simplicity)
def isAnagram(s, t):
    """
    Sort both strings and compare
    Time: O(n log n), Space: O(1)
    
    Anagrams have identical sorted forms.
    """
    return sorted(s) == sorted(t)


#  SOLUTION 2: Character Count (OPTIMAL time)
def isAnagram_count(s, t):
    """
    Count characters in both strings
    Time: O(n), Space: O(1) - max 26 chars
    
    Anagrams have same character frequencies.
    """
    if len(s) != len(t):
        return False
    
    return Counter(s) == Counter(t)


#  SOLUTION 3: Array Counter (No extra imports)
def isAnagram_array(s, t):
    """
    Use array to count chars
    Time: O(n), Space: O(1)
    
    Manual counting - good for interviews without imports.
    """
    if len(s) != len(t):
        return False
    
    count = [0] * 26
    
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    
    return all(c == 0 for c in count)


if __name__ == "__main__":
    print("Testing Valid Anagram:\n")
    
    tests = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "ab", False)
    ]
    
    for s, t, expected in tests:
        r1 = isAnagram(s, t)
        r2 = isAnagram_count(s, t)
        r3 = isAnagram_array(s, t)
        
        print(f'"{s}", "{t}": Sort={r1} Counter={r2} Array={r3} (exp={expected}) {"" if r1 == expected else ""}')

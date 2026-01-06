"""

              LeetCode #1156 - Swap For Longest Repeated Character            
              Topic: String/Sliding Window | Difficulty: Medium               
              Company: Amazon                                                 


PROBLEM: Find max length of substring with same char after at most 1 swap.

Example:
  "ababa"  3 (swap to get "aaaba" or "abaaa")
  "aaabaaa"  6 (swap middle 'b' with external 'a')
"""

from collections import Counter

#  SOLUTION 1: Sliding Window with Counter (OPTIMAL)
def maxRepOpt1(text):
    """
    Sliding window for each character
    Time: O(26*n) = O(n), Space: O(1)
    
    For each char: find max window with at most 1 different char.
    """
    count = Counter(text)
    max_len = 0
    
    for char in count:
        # Try to form longest substring of 'char'
        i = 0
        while i < len(text):
            if text[i] != char:
                i += 1
                continue
            
            # Found start of char sequence
            j = i
            diff_count = 0
            diff_pos = -1
            
            while j < len(text):
                if text[j] == char:
                    j += 1
                elif diff_count == 0:
                    diff_count = 1
                    diff_pos = j
                    j += 1
                else:
                    break
            
            # Length of sequence
            seq_len = j - i
            char_count = seq_len - diff_count
            
            # Can we swap from outside?
            if count[char] > char_count:
                max_len = max(max_len, seq_len)
            else:
                max_len = max(max_len, seq_len - diff_count)
            
            i = diff_pos if diff_pos != -1 else j
    
    return max_len


#  SOLUTION 2: Group Consecutive (Simpler)
def maxRepOpt1_group(text):
    """
    Group consecutive same chars, check merge potential
    Time: O(n), Space: O(n)
    
    If two groups of same char separated by 1 different char, can merge.
    """
    # Group consecutive chars
    groups = []
    i = 0
    while i < len(text):
        j = i
        while j < len(text) and text[j] == text[i]:
            j += 1
        groups.append((text[i], j - i))
        i = j
    
    count = Counter(text)
    max_len = max(min(length + 1, count[char]) for char, length in groups)
    
    # Check if can merge two groups
    for i in range(len(groups) - 2):
        if groups[i][0] == groups[i+2][0] and groups[i+1][1] == 1:
            # Can merge groups[i] and groups[i+2]
            merged = groups[i][1] + groups[i+2][1]
            max_len = max(max_len, min(merged + 1, count[groups[i][0]]))
    
    return max_len


if __name__ == "__main__":
    print("Testing Swap For Longest:\n")
    
    tests = [
        ("ababa", 3),
        ("aaabaaa", 6),
        ("aaaa", 4),
        ("aaaaa", 5),
        ("abcdef", 1)
    ]
    
    for text, expected in tests:
        r1 = maxRepOpt1(text)
        r2 = maxRepOpt1_group(text)
        
        print(f'"{text}": Window={r1} Group={r2} (exp={expected}) {"" if r1 == expected else ""}')

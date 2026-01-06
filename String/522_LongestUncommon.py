"""

              LeetCode #522 - Longest Uncommon Subsequence II                 
              Topic: String | Difficulty: Medium                              
              Company: Google                                                 


PROBLEM: Find longest uncommon subsequence (not subsequence of any other string).

Example:
  ["aba","cdc","eae"]  3 (all length 3, none are subsequences of each other)
"""

#  SOLUTION 1: Brute Force Check (OPTIMAL for correctness)
def findLUSlength(strs):
    """
    Check each string if it's subsequence of any other
    Time: O(n * m), Space: O(1)
    where n=len(strs), m=avg string length
    
    Sort by length descending - check longest first.
    """
    def is_subsequence(s, t):
        # Check if s is subsequence of t
        i = 0
        for char in t:
            if i < len(s) and char == s[i]:
                i += 1
        return i == len(s)
    
    strs.sort(key=len, reverse=True)
    
    for i, s in enumerate(strs):
        # Check if s is uncommon
        is_uncommon = True
        for j, t in enumerate(strs):
            if i != j and is_subsequence(s, t):
                is_uncommon = False
                break
        
        if is_uncommon:
            return len(s)
    
    return -1


#  SOLUTION 2: Frequency Check
def findLUSlength_freq(strs):
    """
    Use frequency map
    Time: O(n * m), Space: O(n)
    
    If string appears once and not subsequence of others, it's uncommon.
    """
    from collections import Counter
    
    def is_subsequence(s, t):
        i = 0
        for char in t:
            if i < len(s) and char == s[i]:
                i += 1
        return i == len(s)
    
    freq = Counter(strs)
    strs_unique = sorted(set(strs), key=len, reverse=True)
    
    for s in strs_unique:
        if freq[s] == 1:
            # Check if not subsequence of any other
            is_uncommon = True
            for t in strs:
                if s != t and is_subsequence(s, t):
                    is_uncommon = False
                    break
            
            if is_uncommon:
                return len(s)
    
    return -1


if __name__ == "__main__":
    print("Testing Longest Uncommon Subsequence:\n")
    
    tests = [
        (["aba","cdc","eae"], 3),
        (["aaa","aaa","aa"], -1),
        (["aabbcc", "aabbcc","cb"], 2)
    ]
    
    for strs, expected in tests:
        r1 = findLUSlength(strs[:])  # Copy to avoid mutation
        r2 = findLUSlength_freq(strs[:])
        
        print(f'{strs}: Brute={r1} Freq={r2} (exp={expected}) {"" if r1 == expected else ""}')

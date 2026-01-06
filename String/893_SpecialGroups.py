"""

              LeetCode #893 - Groups of Special-Equivalent Strings            
              Topic: String/HashMap | Difficulty: Medium                      
              Company: Google                                                 


PROBLEM: Count groups where strings are special-equivalent.
Special-equivalent: can swap chars at even indices with each other,
and chars at odd indices with each other.

Example:
  ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
   3 groups
"""

#  SOLUTION 1: Sort Even/Odd as Signature (OPTIMAL)
def numSpecialEquivGroups(words):
    """
    Use sorted even/odd chars as signature
    Time: O(n * k log k), Space: O(n*k)
    where n=len(words), k=max word length
    
    Two strings are equivalent if they have same sorted even/odd chars.
    """
    def signature(word):
        even = ''.join(sorted(word[0::2]))
        odd = ''.join(sorted(word[1::2]))
        return (even, odd)
    
    groups = set()
    for word in words:
        groups.add(signature(word))
    
    return len(groups)


#  SOLUTION 2: Count Even/Odd Characters
def numSpecialEquivGroups_count(words):
    """
    Count frequency of chars at even/odd positions
    Time: O(n * k), Space: O(n*k)
    
    Use tuple of counts as signature.
    """
    def signature(word):
        even_count = [0] * 26
        odd_count = [0] * 26
        
        for i, char in enumerate(word):
            if i % 2 == 0:
                even_count[ord(char) - ord('a')] += 1
            else:
                odd_count[ord(char) - ord('a')] += 1
        
        return (tuple(even_count), tuple(odd_count))
    
    groups = set()
    for word in words:
        groups.add(signature(word))
    
    return len(groups)


if __name__ == "__main__":
    print("Testing Special Equivalent Groups:\n")
    
    tests = [
        (["abcd","cdab","cbad","xyzz","zzxy","zzyx"], 3),
        (["abc","acb","bac","bca","cab","cba"], 3),
        (["a","b","c","a","c","c"], 3)
    ]
    
    for words, expected in tests:
        r1 = numSpecialEquivGroups(words)
        r2 = numSpecialEquivGroups_count(words)
        
        print(f'{words}:')
        print(f'  Sort={r1} Count={r2} (exp={expected}) {"" if r1 == expected else ""}\n')

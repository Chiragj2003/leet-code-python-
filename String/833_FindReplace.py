"""

              LeetCode #833 - Find And Replace in String                      
              Topic: String | Difficulty: Medium                              
              Company: Amazon, Google                                         


PROBLEM: Replace substrings at specific indices with new strings.

Example:
  s = "abcd", indices = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]
   "eeebffff"
"""

#  SOLUTION 1: Sort and Replace Backwards (OPTIMAL)
def findReplaceString(s, indices, sources, targets):
    """
    Sort by index descending, replace from right to left
    Time: O(n log n + m), Space: O(m)
    where n=len(indices), m=len(s)
    
    Replace backwards to avoid index shifting.
    """
    # Create list of (index, source, target)
    replacements = sorted(zip(indices, sources, targets), reverse=True)
    
    s_list = list(s)
    
    for idx, source, target in replacements:
        # Check if source matches at idx
        if s[idx:idx+len(source)] == source:
            # Replace
            s_list[idx:idx+len(source)] = list(target)
    
    return ''.join(s_list)


#  SOLUTION 2: Mark and Build
def findReplaceString_mark(s, indices, sources, targets):
    """
    Mark valid replacements, then build result
    Time: O(n + m), Space: O(m)
    
    Two-pass approach.
    """
    # Mark replacements
    replace_map = {}
    for i, idx in enumerate(indices):
        if s[idx:idx+len(sources[i])] == sources[i]:
            replace_map[idx] = (len(sources[i]), targets[i])
    
    # Build result
    result = []
    i = 0
    while i < len(s):
        if i in replace_map:
            skip_len, target = replace_map[i]
            result.append(target)
            i += skip_len
        else:
            result.append(s[i])
            i += 1
    
    return ''.join(result)


if __name__ == "__main__":
    print("Testing Find And Replace:\n")
    
    tests = [
        ("abcd", [0,2], ["a","cd"], ["eee","ffff"], "eeebffff"),
        ("abcd", [0,2], ["ab","ec"], ["eee","ffff"], "eeecd")
    ]
    
    for s, indices, sources, targets, expected in tests:
        r1 = findReplaceString(s, indices, sources, targets)
        r2 = findReplaceString_mark(s, indices, sources, targets)
        
        print(f's="{s}": Sort={r1} Mark={r2}')
        print(f'  Expected={expected} {"" if r1 == expected else ""}\n')

"""
LeetCode #833 - Find and Replace in String
Topic: String
Difficulty: Medium

PROBLEM EXPLANATION:
Given a string s and arrays indices, sources, and targets, perform replacements:
- If sources[i] matches s starting at indices[i], replace with targets[i]
- Process all replacements that don't overlap

Example:
Input: s = "abcd", indices = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]
Output: "eeebffff"
Explanation: "a" at index 0 -> "eee", "cd" at index 2 -> "ffff"

APPROACH:
1. Create list of (index, source, target) and sort by index (descending)
2. Process from right to left to avoid index shifting
3. For each replacement, check if source matches at index
4. If yes, replace; otherwise skip

Time Complexity: O(n log n + m) where m is total length
Space Complexity: O(n)
"""

def findReplaceString(s, indices, sources, targets):
    """
    Returns string after replacements
    """
    # Combine and sort by index (descending to process right-to-left)
    replacements = sorted(zip(indices, sources, targets), reverse=True)
    
    # Convert string to list for easier manipulation
    result = list(s)
    
    for index, source, target in replacements:
        # Check if source matches at index
        if s[index:index+len(source)] == source:
            # Replace
            result[index:index+len(source)] = list(target)
    
    return ''.join(result)


# Test cases
if __name__ == "__main__":
    test1 = findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"])
    print(f"Test 1: {test1}")  # Expected: "eeebffff"
    
    test2 = findReplaceString("abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"])
    print(f"Test 2: {test2}")  # Expected: "eeecd"
    
    test3 = findReplaceString("vmokgggqzp", [3,5,1], ["kg","ggq","mo"], ["s","so","bfr"])
    print(f"Test 3: {test3}")  # Expected: "vbfrssozp"

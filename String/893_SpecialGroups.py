"""
LeetCode #893 - Groups of Special-Equivalent Strings
Topic: String
Difficulty: Medium

PROBLEM EXPLANATION:
Two strings are special-equivalent if after any number of swaps of characters
at even indices or odd indices separately, they become equal.
Return the number of groups of special-equivalent strings.

Example:
Input: words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
Output: 3
Explanation: Groups are ["abcd","cdab","cbad"], ["xyzz","zzxy","zzyx"], []

APPROACH:
1. For each string, separate into even and odd indexed characters
2. Sort both groups
3. Use sorted tuple as signature
4. Count unique signatures

Time Complexity: O(n * m log m)
Space Complexity: O(n * m)
"""

def numSpecialEquivGroups(words):
    """
    Returns number of special-equivalent groups
    """
    def get_signature(word):
        # Separate even and odd indexed characters
        even = ''.join(sorted(word[::2]))
        odd = ''.join(sorted(word[1::2]))
        return (even, odd)
    
    # Use set to count unique signatures
    signatures = set()
    
    for word in words:
        signatures.add(get_signature(word))
    
    return len(signatures)


# Test cases
if __name__ == "__main__":
    test1 = ["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"]
    print(f"Test 1: {numSpecialEquivGroups(test1)}")  # Expected: 3
    
    test2 = ["abc", "acb", "bac", "bca", "cab", "cba"]
    print(f"Test 2: {numSpecialEquivGroups(test2)}")  # Expected: 3
    
    test3 = ["a", "b", "c", "a", "c", "c"]
    print(f"Test 3: {numSpecialEquivGroups(test3)}")  # Expected: 3

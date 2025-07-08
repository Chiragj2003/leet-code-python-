"""
LeetCode #49 - Group Anagrams
Topic: Hashmap / String
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Group strings that are anagrams of each other.

Example:
Input: ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Think of it like:
Anagrams are words with same letters in different order.
"eat", "tea", "ate" all have letters 'e', 'a', 't'
So they belong to the same group!

WHY THIS WORKS (Simple Explanation):
Use a signature to identify anagrams:
1. Sort the letters: "eat" -> "aet", "tea" -> "aet" (same!)
2. Use sorted string as key in hashmap
3. All anagrams will have the same key!

Think of sorting as a "fingerprint" for anagrams.

Time Complexity: O(n * k log k) where n=number of strings, k=max length
Space Complexity: O(n * k) for storing all strings
"""

from collections import defaultdict

def groupAnagrams(strs):
    """
    Group anagrams using sorted string as key
    
    Visual example:
    ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    "eat" -> sorted: "aet" -> groups["aet"] = ["eat"]
    "tea" -> sorted: "aet" -> groups["aet"] = ["eat", "tea"]
    "tan" -> sorted: "ant" -> groups["ant"] = ["tan"]
    "ate" -> sorted: "aet" -> groups["aet"] = ["eat", "tea", "ate"]
    "nat" -> sorted: "ant" -> groups["ant"] = ["tan", "nat"]
    "bat" -> sorted: "abt" -> groups["abt"] = ["bat"]
    
    Result: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
    """
    # Dictionary: sorted_string -> list of original strings
    groups = defaultdict(list)
    
    for word in strs:
        # Sort characters to get signature
        # All anagrams will have same sorted form
        sorted_word = ''.join(sorted(word))
        
        # Add to group
        groups[sorted_word].append(word)
    
    # Return all groups as list
    return list(groups.values())


def groupAnagrams_count(strs):
    """
    Alternative: Use character count as key
    
    Instead of sorting, count frequency of each letter.
    "eat" -> (1,0,0,0,1,0,...,1,0,0) for 'a','e','t'
    
    This avoids sorting but creates tuple key.
    Time: O(n * k) where k is max string length
    """
    groups = defaultdict(list)
    
    for word in strs:
        # Count frequency of each letter (a-z)
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        
        # Use tuple as hashmap key
        # Tuples are immutable and hashable!
        key = tuple(count)
        groups[key].append(word)
    
    return list(groups.values())


# Test cases with explanations
if __name__ == "__main__":
    test_cases = [
        (
            ["eat","tea","tan","ate","nat","bat"],
            [["bat"],["nat","tan"],["ate","eat","tea"]]
        ),
        (
            [""],
            [[""]]
        ),
        (
            ["a"],
            [["a"]]
        ),
        (
            ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"],
            [["cab"],["tin"],["pew"],["duh"],["may"],["ill"],["buy"],["bar"],["max"],["doc"]]
        ),
    ]
    
    print("=== Testing Sorting Solution ===")
    for strs, expected in test_cases:
        result = groupAnagrams(strs)
        # Sort for comparison (order doesn't matter)
        result_sorted = [sorted(group) for group in sorted(result)]
        expected_sorted = [sorted(group) for group in sorted(expected)]
        
        status = "✓" if result_sorted == expected_sorted else "✗"
        print(f"{status} Input: {strs}")
        print(f"   Output: {result}")
        print()
    
    print("=== Testing Character Count Solution ===")
    for strs, expected in test_cases:
        result = groupAnagrams_count(strs)
        result_sorted = [sorted(group) for group in sorted(result)]
        expected_sorted = [sorted(group) for group in sorted(expected)]
        
        status = "✓" if result_sorted == expected_sorted else "✗"
        print(f"{status} Input: {strs}")
        print(f"   Output: {result}")
        print()

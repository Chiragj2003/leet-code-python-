"""
LeetCode #953 - Verifying an Alien Dictionary
Topic: Hashmap
Difficulty: Easy

PROBLEM EXPLANATION:
In an alien language, they use the English alphabet but in a different order.
Given a sequence of words in alien language and the order of the alphabet,
return true if the words are sorted lexicographically in this alien language.

Example:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: 'h' < 'l' in the alien language, so "hello" comes before "leetcode"

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: 'd' < 'l' in alien language, so "word" should come after "world"

APPROACH:
1. Create a mapping of character to its order position
2. Compare adjacent words to check if they're in order
3. For each pair, find first differing character
4. If word1[i] > word2[i] in alien order, return False
5. If word1 is prefix of word2 but longer, return False

Time Complexity: O(n * m) where n = number of words, m = avg word length
Space Complexity: O(1) - only 26 letters
"""

def isAlienSorted(words, order):
    """
    Returns True if words are sorted in alien dictionary order
    """
    # Create character to position mapping
    order_map = {char: i for i, char in enumerate(order)}
    
    # Compare adjacent words
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        
        # Check if word1 should come before word2
        if not is_sorted(word1, word2, order_map):
            return False
    
    return True


def is_sorted(word1, word2, order_map):
    """
    Check if word1 comes before word2 in alien dictionary
    """
    min_len = min(len(word1), len(word2))
    
    # Compare character by character
    for i in range(min_len):
        if word1[i] != word2[i]:
            # Found first differing character
            if order_map[word1[i]] > order_map[word2[i]]:
                return False
            else:
                return True
    
    # One word is prefix of another
    # word1 should not be longer than word2
    return len(word1) <= len(word2)


# Test cases
if __name__ == "__main__":
    test1_words = ["hello", "leetcode"]
    test1_order = "hlabcdefgijkmnopqrstuvwxyz"
    print(f"Test 1: {isAlienSorted(test1_words, test1_order)}")
    # Expected: True
    
    test2_words = ["word", "world", "row"]
    test2_order = "worldabcefghijkmnpqstuvxyz"
    print(f"Test 2: {isAlienSorted(test2_words, test2_order)}")
    # Expected: False
    
    test3_words = ["apple", "app"]
    test3_order = "abcdefghijklmnopqrstuvwxyz"
    print(f"Test 3: {isAlienSorted(test3_words, test3_order)}")
    # Expected: False (apple is longer than app)
    
    test4_words = ["kuvp", "q"]
    test4_order = "ngxlkthsjuoqcpavbfdermiywz"
    print(f"Test 4: {isAlienSorted(test4_words, test4_order)}")
    # Expected: True

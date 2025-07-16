"""
LeetCode #1160 - Find Words That Can Be Formed by Characters
Topic: Hashmap
Difficulty: Easy

PROBLEM EXPLANATION:
You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars
(each character can only be used once).
Return the sum of lengths of all good strings in words.

Example:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: "cat" and "hat" can be formed (6 letters total).
"bt" needs 'b' which is not in chars
"tree" needs two 'e's but chars has none

APPROACH:
1. Count frequency of characters in chars
2. For each word, check if it can be formed with available characters
3. Compare character frequencies: word_count vs chars_count
4. If word can be formed, add its length to result

Time Complexity: O(n * m) where n = number of words, m = avg word length
Space Complexity: O(1) - at most 26 letters
"""

from collections import Counter

def countCharacters(words, chars):
    """
    Returns sum of lengths of all good words
    """
    chars_count = Counter(chars)
    total_length = 0
    
    for word in words:
        word_count = Counter(word)
        
        # Check if word can be formed
        can_form = True
        for char, count in word_count.items():
            if chars_count[char] < count:
                can_form = False
                break
        
        if can_form:
            total_length += len(word)
    
    return total_length


# Alternative: More concise using all()
def countCharacters_v2(words, chars):
    """
    Cleaner implementation
    """
    chars_count = Counter(chars)
    total_length = 0
    
    for word in words:
        word_count = Counter(word)
        # Check if all characters in word can be satisfied by chars
        if all(word_count[c] <= chars_count[c] for c in word_count):
            total_length += len(word)
    
    return total_length


# Test cases
if __name__ == "__main__":
    test1_words = ["cat", "bt", "hat", "tree"]
    test1_chars = "atach"
    print(f"Test 1: {countCharacters(test1_words, test1_chars)}")
    # Expected: 6
    
    test2_words = ["hello", "world", "leetcode"]
    test2_chars = "welldonehoneyr"
    print(f"Test 2: {countCharacters(test2_words, test2_chars)}")
    # Expected: 10
    
    test3_words = ["cat", "dog", "cow"]
    test3_chars = "cowtoad"
    print(f"Test 3: {countCharacters(test3_words, test3_chars)}")
    # Expected: 6 (cat + cow)

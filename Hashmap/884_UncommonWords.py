"""
LeetCode #884 - Uncommon Words from Two Sentences
Topic: Hashmap
Difficulty: Easy

PROBLEM EXPLANATION:
A sentence is a string of single-space separated words.
A word is uncommon if it appears exactly once in one of the sentences,
and does not appear in the other sentence.
Return all uncommon words in any order.

Example:
Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]

Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]

APPROACH:
1. Count frequency of all words from both sentences
2. A word is uncommon if it appears exactly once in total
3. Return words with count = 1

Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""

from collections import Counter

def uncommonFromSentences(s1, s2):
    """
    Returns uncommon words from two sentences
    """
    # Split and count all words
    words1 = s1.split()
    words2 = s2.split()
    
    # Count frequency of all words
    word_count = Counter(words1 + words2)
    
    # Return words that appear exactly once
    return [word for word, count in word_count.items() if count == 1]


# Alternative: Without Counter
def uncommonFromSentences_v2(s1, s2):
    """
    Using dictionary instead of Counter
    """
    word_count = {}
    
    # Count words from s1
    for word in s1.split():
        word_count[word] = word_count.get(word, 0) + 1
    
    # Count words from s2
    for word in s2.split():
        word_count[word] = word_count.get(word, 0) + 1
    
    # Return words with count = 1
    return [word for word, count in word_count.items() if count == 1]


# Test cases
if __name__ == "__main__":
    test1_s1 = "this apple is sweet"
    test1_s2 = "this apple is sour"
    print(f"Test 1: {uncommonFromSentences(test1_s1, test1_s2)}")
    # Expected: ["sweet", "sour"]
    
    test2_s1 = "apple apple"
    test2_s2 = "banana"
    print(f"Test 2: {uncommonFromSentences(test2_s1, test2_s2)}")
    # Expected: ["banana"]
    
    test3_s1 = "s z z z s"
    test3_s2 = "s z ejt"
    print(f"Test 3: {uncommonFromSentences(test3_s1, test3_s2)}")
    # Expected: ["ejt"]

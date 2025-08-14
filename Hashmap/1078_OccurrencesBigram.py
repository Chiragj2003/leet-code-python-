"""
LeetCode #1078 - Occurrences After Bigram
Topic: Hashmap / String
Difficulty: Easy

PROBLEM EXPLANATION:
Given two strings first and second, and a text string, return an array of
all words in text that appear after a bigram (consecutive pair of words)
where the first word is first and the second word is second.

Example:
Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]
Explanation: "a good girl" and "a good student" - words after "a good" are "girl" and "student"

APPROACH:
1. Split text into words
2. Iterate through words looking for the bigram pattern
3. When found, add the next word (if exists) to result
4. Continue checking for more occurrences

Time Complexity: O(n) where n = number of words
Space Complexity: O(n) for storing words and result
"""

def findOcurrences(text, first, second):
    """
    Returns words that appear after the bigram (first, second)
    """
    words = text.split()
    result = []
    
    # Check each consecutive pair of words
    for i in range(len(words) - 2):
        if words[i] == first and words[i + 1] == second:
            # Found the bigram, add next word
            result.append(words[i + 2])
    
    return result


# Test cases
if __name__ == "__main__":
    test1_text = "alice is a good girl she is a good student"
    test1_first = "a"
    test1_second = "good"
    print(f"Test 1: {findOcurrences(test1_text, test1_first, test1_second)}")
    # Expected: ["girl", "student"]
    
    test2_text = "we will we will rock you"
    test2_first = "we"
    test2_second = "will"
    print(f"Test 2: {findOcurrences(test2_text, test2_first, test2_second)}")
    # Expected: ["we", "rock"]
    
    test3_text = "alice is aa good girl she is a good student"
    test3_first = "a"
    test3_second = "good"
    print(f"Test 3: {findOcurrences(test3_text, test3_first, test3_second)}")
    # Expected: ["student"]
    
    test4_text = "jkypmsxd jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa kcyxdfnoa jkypmsxd kcyxdfnoa"
    test4_first = "jkypmsxd"
    test4_second = "kcyxdfnoa"
    print(f"Test 4: {findOcurrences(test4_text, test4_first, test4_second)}")
    # Expected: ["jkypmsxd", "jkypmsxd", "kcyxdfnoa"]

"""
LeetCode #748 - Shortest Completing Word
Topic: Hashmap
Difficulty: Easy

PROBLEM EXPLANATION:
Given a string licensePlate and an array of strings words,
find the shortest completing word in words.

A completing word is a word that contains all the letters in licensePlate
(ignoring numbers and spaces). Letters are case insensitive.
If there are multiple words with same length, return the first one.

Example:
Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
Output: "steps"
Explanation: "step" contains letters {s, t, e, p} but licensePlate needs {s, s, p, t}
"steps" contains {s, t, e, p, s} which covers all letters

APPROACH:
1. Extract letters from licensePlate and count frequencies
2. For each word, check if it contains all required letters
3. Track the shortest completing word

Time Complexity: O(n * m) where n = number of words, m = avg word length
Space Complexity: O(1) - at most 26 letters
"""

from collections import Counter

def shortestCompletingWord(licensePlate, words):
    """
    Returns the shortest completing word
    """
    # Extract letters from license plate and count them
    letters = [c.lower() for c in licensePlate if c.isalpha()]
    license_count = Counter(letters)
    
    shortest = None
    
    for word in words:
        word_count = Counter(word.lower())
        
        # Check if word contains all required letters
        is_completing = True
        for letter, count in license_count.items():
            if word_count[letter] < count:
                is_completing = False
                break
        
        # Update shortest if this word is completing and shorter
        if is_completing:
            if shortest is None or len(word) < len(shortest):
                shortest = word
    
    return shortest


# Test cases
if __name__ == "__main__":
    test1_license = "1s3 PSt"
    test1_words = ["step", "steps", "stripe", "stepple"]
    print(f"Test 1: {shortestCompletingWord(test1_license, test1_words)}")
    # Expected: "steps"
    
    test2_license = "1s3 456"
    test2_words = ["looks", "pest", "stew", "show"]
    print(f"Test 2: {shortestCompletingWord(test2_license, test2_words)}")
    # Expected: "pest"
    
    test3_license = "Ah71752"
    test3_words = ["suggest", "letter", "of", "husband", "easy", "education", "drug", "prevent", "writer", "old"]
    print(f"Test 3: {shortestCompletingWord(test3_license, test3_words)}")
    # Expected: "husband"
    
    test4_license = "OgEu755"
    test4_words = ["enough", "these", "play", "wide", "wonder", "box", "arrive", "money", "tax", "thus"]
    print(f"Test 4: {shortestCompletingWord(test4_license, test4_words)}")
    # Expected: "enough"

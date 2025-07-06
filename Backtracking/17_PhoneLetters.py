"""
LeetCode #17 - Letter Combinations of a Phone Number
Topic: Backtracking / String
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Phone keypad mappings (like old phones):
2=abc, 3=def, 4=ghi, 5=jkl, 6=mno, 7=pqrs, 8=tuv, 9=wxyz

Find all letter combinations for digits.

Example:
"23" -> ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Think of it like:
Typing on old phone keyboard!

WHY THIS WORKS (Simple Explanation):
Backtracking: try each letter for each digit.

Time: O(4^n) worst case
Space: O(n)
"""

def letterCombinations(digits):
    """Generate letter combinations"""
    if not digits:
        return []
    
    phone = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    result = []
    
    def backtrack(index, path):
        if index == len(digits):
            result.append(path)
            return
        
        for letter in phone[digits[index]]:
            backtrack(index + 1, path + letter)
    
    backtrack(0, '')
    return result


# Test
if __name__ == "__main__":
    result = letterCombinations("23")
    print(f'"23" -> {result}')

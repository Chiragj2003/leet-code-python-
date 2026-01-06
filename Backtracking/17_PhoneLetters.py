"""
╔══════════════════════════════════════════════════════════════════════════════╗
║              LeetCode #17 - Letter Combinations of a Phone Number             ║
║                    Topic: Backtracking / String                              ║
║                    Difficulty: Medium                                         ║
║                    Company: Amazon, Google, Facebook                         ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Old phone keypads had letters on number buttons:
2=abc, 3=def, 4=ghi, 5=jkl, 6=mno, 7=pqrs, 8=tuv, 9=wxyz

Given digits, return ALL possible letter combinations.

EXAMPLES:
─────────
✓ Input: "23"    → Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
✓ Input: ""      → Output: []
✓ Input: "2"     → Output: ["a","b","c"]

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
📱 You're texting on an old flip phone!
   Press "2" → could be "a", "b", or "c"
   Press "3" → could be "d", "e", or "f"
   
   For "23", you can make:
   "a"+"d"="ad", "a"+"e"="ae", "a"+"f"="af",
   "b"+"d"="bd", "b"+"e"="be", "b"+"f"="bf",
   "c"+"d"="cd", "c"+"e"="ce", "c"+"f"="cf"
   
   List ALL possible texts you could spell!

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   At Amazon Alexa voice assistant, user says phone number digits.
   We need to generate all possible name spellings for contact lookup
   (like old T9 predictive text).

📌 TASK:
   Given digit string, return all letter combinations.
   Time O(4^n × n), Space O(n) for recursion.

📌 ACTION:
   Use backtracking (decision tree exploration):
   
   ✓ Algorithm:
     1. Map digits to letters
     2. For each digit, try all its letters
     3. Recursively build combinations
     4. When reach end, save combination

📌 RESULT:
   ✓ Time Complexity: O(4^n × n) - worst case (7,9 have 4 letters)
   ✓ Space Complexity: O(n) for recursion depth
   ✓ Generates all contact name possibilities instantly

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⏰ COMPLEXITY ANALYSIS                                    ║
╚══════════════════════════════════════════════════════════════════════════════╝

ITERATIVE (Build layer by layer):
    Time: O(4^n × n)
    Space: O(4^n) for all combinations

BACKTRACKING (OPTIMAL):
    Time: O(4^n × n) - same but cleaner
    Space: O(n) recursion depth

"""

# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Backtracking (AMAZON PREFERRED!)
# ═══════════════════════════════════════════════════════════════════════════
def letterCombinations(digits):
    """
    Backtracking - OPTIMAL for Amazon Interview!
    
    🔑 KEY INSIGHT:
    ───────────────
    Decision tree: For each digit, branch into all its letters.
    
    Example: "23"
    ───────
                    ""
            /       |       \\
           a        b        c    (digit "2")
         / | \\    / | \\    / | \\
        d  e  f   d  e  f   d  e  f  (digit "3")
    
    Paths: ad, ae, af, bd, be, bf, cd, ce, cf
    
    Visual trace for "23":
    ─────────────────────
    Start: path=""
    
    Digit 0 (="2"): Try "a"
      path="a"
      Digit 1 (="3"): Try "d"
        path="ad" → COMPLETE! Add to result
      Digit 1 (="3"): Try "e"
        path="ae" → COMPLETE! Add to result
      Digit 1 (="3"): Try "f"
        path="af" → COMPLETE! Add to result
    
    Digit 0 (="2"): Try "b"
      path="b"
      Digit 1 (="3"): Try "d"
        path="bd" → COMPLETE! Add to result
      ... and so on
    
    WHY THIS IS BEST FOR AMAZON:
    ─────────────────────────────
    ✓ Clean recursive structure
    ✓ O(n) space for recursion
    ✓ Explores all possibilities
    ✓ Easy to understand and modify
    """
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        result = ['']
        
        for digit in digits:
            temp = []
            for combination in result:
                for letter in phone[digit]:
                    temp.append(combination + letter)
            result = temp
        
        return result


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE 1 - Iterative Approach
# ═══════════════════════════════════════════════════════════════════════════
def letterCombinations_iterative(digits):
    """
    Iterative: Build combinations layer by layer
    
    Example: "23"
    ───────
    Start: [""]
    Add digit "2": ["a", "b", "c"]
    Add digit "3": ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    
    Time: O(4^n × n)
    Space: O(4^n)
    """
    if not digits:
        return []
    
    phone = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    result = ['']
    
    for digit in digits:
        temp = []
        for combination in result:
            for letter in phone[digit]:
                temp.append(combination + letter)
        result = temp
    
    return result


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [
        ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
        ("", []),
        ("2", ["a","b","c"]),
        ("7", ["p","q","r","s"]),
    ]
    
    print("=" * 70)
    print("🧪 TESTING LETTER COMBINATIONS")
    print("=" * 70)
    
    for digits, expected in test_cases:
        result_backtrack = letterCombinations(digits)
        result_iterative = letterCombinations_iterative(digits)
        
        status = "✓" if result_backtrack == expected else "✗"
        
        print(f"\n{status} Input: '{digits}'")
        print(f"  Expected:   {expected}")
        print(f"  Backtrack:  {result_backtrack}")
        print(f"  Iterative:  {result_iterative}")
    
    print("\n" + "=" * 70)
    print("📊 COMPLEXITY COMPARISON")
    print("=" * 70)
    print("| Method      | Time      | Space   | Amazon |")
    print("|-------------|-----------|---------|--------|")
    print("| Backtrack   | O(4^n×n)  | O(n)    | ✅     |")
    print("| Iterative   | O(4^n×n)  | O(4^n)  | ⚠️     |")

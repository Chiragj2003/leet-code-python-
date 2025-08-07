"""
LeetCode #22 - Generate Parentheses
Topic: Backtracking
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Generate all valid combinations of n pairs of parentheses.

Example:
n=3 -> ["((()))","(()())","(())()","()(())","()()()"]

Think of it like:
All ways to properly nest n pairs of brackets!

WHY THIS WORKS (Simple Explanation):
At each step:
- Can add '(' if we haven't used all n
- Can add ')' if it won't make invalid (more ')' than '(')

Backtrack to try all valid combinations!

Time: O(4^n / sqrt(n)) - Catalan number
Space: O(n) for recursion
"""

def generateParenthesis(n):
    """Generate all valid parentheses combinations"""
    result = []
    
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        
        # Can add '(' if haven't used all
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        
        # Can add ')' if won't make invalid
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    
    backtrack('', 0, 0)
    return result


# Test
if __name__ == "__main__":
    for n in [1, 2, 3]:
        result = generateParenthesis(n)
        print(f"n={n}: {result}")

"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #22 - Generate Parentheses                        ║
║                    Topic: Backtracking                                       ║
║                    Difficulty: Medium                                         ║
║                    Company: Amazon, Meta, Google                             ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Given n pairs of parentheses, generate ALL valid combinations.

EXAMPLES:
─────────
✓ Input: n = 3  → Output: ["((()))","(()())","(())()","()(())","()()()"]
✓ Input: n = 1  → Output: ["()"]

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🔓 Opening and closing doors:
   - You have 3 doors
   - Must open before you can close
   - Open all, then close all: ((()))
   - Mix it up: ()()()

🎨 Brackets: Think of them as hugs!
   ( = start hug, ) = end hug
   Can't end before you start!

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   Amazon JSON validation: generate all valid bracket patterns
   for testing parser edge cases.

📌 TASK:
   Generate all valid n-pair parentheses.
   Time O(4^n / √n), Space O(n).

📌 ACTION:
   Backtracking with rules:
   1. Add '(' if open < n
   2. Add ')' if close < open

📌 RESULT:
   ✓ Time: O(4^n / √n) - Catalan number
   ✓ Space: O(n) recursion
   ✓ All valid patterns generated

"""

# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Backtracking
# ═══════════════════════════════════════════════════════════════════════════
def generateParenthesis(n):
    """
    Backtracking with open/close counters
    
    Rules:
    1. Add '(' if open < n
    2. Add ')' if close < open
    
    Example: n = 2
    ───────
                    ""
                 /      
               "("       
             /    \\
          "(("    "()"
           |       |
        "(())"  "()()"
    """
    result = []
    
    def backtrack(path, open_count, close_count):
        # Base case: complete
        if len(path) == 2 * n:
            result.append(path)
            return
        
        # Add '(' if we can
        if open_count < n:
            backtrack(path + '(', open_count + 1, close_count)
        
        # Add ')' if valid
        if close_count < open_count:
            backtrack(path + ')', open_count, close_count + 1)
    
    backtrack('', 0, 0)
    return result


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE - Iterative DP
# ═══════════════════════════════════════════════════════════════════════════
def generateParenthesis_dp(n):
    """
    Dynamic programming approach
    
    dp[0] = [""]
    dp[1] = ["()"]
    dp[2] = ["(())", "()()"]
    """
    if n == 0:
        return [""]
    
    dp = [[] for _ in range(n + 1)]
    dp[0] = [""]
    
    for i in range(1, n + 1):
        for j in range(i):
            # ( left ) right
            for left in dp[j]:
                for right in dp[i - 1 - j]:
                    dp[i].append(f"({left}){right}")
    
    return dp[n]


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [1, 2, 3]
    
    print("=" * 70)
    print("🧪 TESTING GENERATE PARENTHESES")
    print("=" * 70)
    
    for n in test_cases:
        result1 = generateParenthesis(n)
        result2 = generateParenthesis_dp(n)
        
        print(f"\nInput: n = {n}")
        print(f"Count: {len(result1)} combinations")
        print(f"Backtrack: {result1}")
        print(f"DP: {result2}")

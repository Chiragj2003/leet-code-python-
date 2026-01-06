"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #39 - Combination Sum                             ║
║                    Topic: Backtracking                                       ║
║                    Difficulty: Medium                                         ║
║                    Company: Amazon, Airbnb, eBay                             ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Given array of DISTINCT integers and target, find ALL unique combinations
where numbers sum to target. Same number can be used UNLIMITED times.

EXAMPLES:
─────────
✓ Input: candidates = [2,3,6,7], target = 7
  Output: [[2,2,3],[7]]

✓ Input: candidates = [2,3,5], target = 8
  Output: [[2,2,2,2],[2,3,3],[3,5]]

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
💰 Making change: You have coins [2, 3, 5].
   How many ways to make $8?
   - Four 2's: 2+2+2+2
   - One 2, two 3's: 2+3+3
   - One 3, one 5: 3+5

🎯 Target game: throw darts worth 2, 3, 5 points.
   How to score exactly 8?

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   Amazon gift card: customer has multiple denominations,
   find all ways to reach exact amount.

📌 TASK:
   Find all combinations summing to target.
   Time O(2^target), Space O(target).

📌 ACTION:
   Backtracking with reusable elements:
   1. Try each candidate
   2. Allow reuse by staying at same index
   3. Prune when sum exceeds target

📌 RESULT:
   ✓ Time: O(2^target) worst case
   ✓ Space: O(target) recursion depth
   ✓ All valid combinations found

"""

# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Backtracking
# ═══════════════════════════════════════════════════════════════════════════
def combinationSum(candidates, target):
    """
    Backtracking with reusable elements
    
    Example: [2,3,6,7], target = 7
    ───────
                    []
            /    |    \\   \\
          [2]   [3]  [6]  [7] ✓
         / | \\   |
      [2,2][2,3][2,6][3,3]
        |    ✓
     [2,2,2]    
        |
    [2,2,2,2] (over)
    """
    result = []
    
    def backtrack(start, path, total):
        # Success: found combination
        if total == target:
            result.append(path[:])
            return
        
        # Prune: exceeded target
        if total > target:
            return
        
        # Try each candidate
        for i in range(start, len(candidates)):
            # Choose
            path.append(candidates[i])
            # Explore (allow reuse: stay at i)
            backtrack(i, path, total + candidates[i])
            # Unchoose
            path.pop()
    
    backtrack(0, [], 0)
    return result


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE - Early Pruning
# ═══════════════════════════════════════════════════════════════════════════
def combinationSum_pruned(candidates, target):
    """
    Backtracking with sorted candidates for early pruning
    """
    result = []
    candidates.sort()  # Sort for early termination
    
    def backtrack(start, path, total):
        if total == target:
            result.append(path[:])
            return
        
        for i in range(start, len(candidates)):
            # Early exit: if current too large, rest also too large
            if total + candidates[i] > target:
                break
            
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])
            path.pop()
    
    backtrack(0, [], 0)
    return result


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [
        ([2, 3, 6, 7], 7),
        ([2, 3, 5], 8),
        ([2], 1),
    ]
    
    print("=" * 70)
    print("🧪 TESTING COMBINATION SUM")
    print("=" * 70)
    
    for candidates, target in test_cases:
        result1 = combinationSum(candidates.copy(), target)
        result2 = combinationSum_pruned(candidates.copy(), target)
        
        print(f"\nInput: candidates = {candidates}, target = {target}")
        print(f"Result: {result1}")
        print(f"Pruned: {result2}")

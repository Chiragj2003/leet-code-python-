"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #78 - Subsets                                     ║
║                    Topic: Backtracking                                       ║
║                    Difficulty: Medium                                         ║
║                    Company: Amazon, Facebook, Google                         ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Given array of UNIQUE integers, return ALL possible subsets (power set).

EXAMPLES:
─────────
✓ Input: [1,2,3]  
  Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

✓ Input: [0]      → Output: [[],[0]]

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🍕 Pizza toppings: cheese, peppers, onions.
   What are ALL possible pizza combinations?
   - Plain (no toppings)
   - Just cheese
   - Just peppers
   - Cheese + peppers
   - etc.

📦 Packing: You have 3 items. What are all ways to pack?
   (including packing nothing!)

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   Amazon product bundles: given n items, generate all
   possible bundle combinations for customers.

📌 TASK:
   Return all subsets (2^n total).
   Time O(2^n × n), Space O(n).

📌 ACTION:
   Backtracking: for each element, include or exclude.

📌 RESULT:
   ✓ Time: O(2^n × n) - 2^n subsets, n to copy
   ✓ Space: O(n) recursion
   ✓ All bundle options generated

"""

# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Backtracking
# ═══════════════════════════════════════════════════════════════════════════
def subsets(nums):
    """
    Backtracking - generate all subsets
    
    Example: [1,2,3]
    ───────
                    []
            /               \\
          [1]                []
        /     \\            /    \\
     [1,2]    [1]        [2]     []
     /  \\    /  \\      /  \\    /  \\
  [1,2,3][1,2][1,3][1][2,3][2][3][]
    """
    result = []
    
    def backtrack(start, path):
        # Add current subset
        result.append(path[:])
        
        # Try adding each remaining element
        for i in range(start, len(nums)):
            # Include nums[i]
            path.append(nums[i])
            backtrack(i + 1, path)
            # Exclude nums[i] (backtrack)
            path.pop()
    
    backtrack(0, [])
    return result


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE - Iterative
# ═══════════════════════════════════════════════════════════════════════════
def subsets_iterative(nums):
    """
    Iterative: build subsets incrementally
    
    Start: [[]]
    Add 1: [[], [1]]
    Add 2: [[], [1], [2], [1,2]]
    Add 3: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
    """
    result = [[]]
    
    for num in nums:
        result += [curr + [num] for curr in result]
    
    return result


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],
        [0],
        [1, 2],
    ]
    
    print("=" * 70)
    print("🧪 TESTING SUBSETS")
    print("=" * 70)
    
    for nums in test_cases:
        result1 = subsets(nums)
        result2 = subsets_iterative(nums)
        
        print(f"\nInput: {nums}")
        print(f"Count: {len(result1)} subsets")
        print(f"Backtrack: {result1}")
        print(f"Iterative: {result2}")

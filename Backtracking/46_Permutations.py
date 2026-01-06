"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #46 - Permutations                                ║
║                    Topic: Backtracking                                       ║
║                    Difficulty: Medium                                         ║
║                    Company: Amazon, Google, Microsoft                        ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Given array of DISTINCT integers, return ALL possible permutations.

EXAMPLES:
─────────
✓ Input: [1,2,3]  → Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
✓ Input: [0,1]    → Output: [[0,1],[1,0]]
✓ Input: [1]      → Output: [[1]]

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🎪 You have 3 performers: A, B, C.
   In how many different orders can they perform?
   ABC, ACB, BAC, BCA, CAB, CBA → 6 ways!

🎲 Rolling dice: if you have numbers 1, 2, 3,
   list all different arrangements possible.

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   Amazon delivery routes need all possible orderings of stops
   to find optimal delivery sequence.

📌 TASK:
   Generate all permutations of array.
   Time O(n! × n), Space O(n).

📌 ACTION:
   Backtracking with used tracking:
   1. Try each unused number
   2. Mark as used, recurse
   3. Backtrack: unmark and try next

📌 RESULT:
   ✓ Time: O(n! × n) - n! permutations, n to copy each
   ✓ Space: O(n) recursion depth
   ✓ All routes generated for optimization

"""

# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Backtracking
# ═══════════════════════════════════════════════════════════════════════════
def permute(nums):
    """
    Backtracking with used array
    
    Example: [1,2,3]
    ───────
                    []
          /         |         \\
        [1]        [2]        [3]
       /  \\       /  \\       /  \\
    [1,2] [1,3] [2,1] [2,3] [3,1] [3,2]
      |     |     |     |     |     |
   [1,2,3][1,3,2][2,1,3][2,3,1][3,1,2][3,2,1]
    """
    result = []
    
    def backtrack(path):
        # Base case: permutation complete
        if len(path) == len(nums):
            result.append(path[:])  # Copy path
            return
        
        # Try each number
        for num in nums:
            if num in path:
                continue  # Skip used numbers
            
            # Choose
            path.append(num)
            # Explore
            backtrack(path)
            # Unchoose (backtrack)
            path.pop()
    
    backtrack([])
    return result


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE - Swap Method
# ═══════════════════════════════════════════════════════════════════════════
def permute_swap(nums):
    """
    In-place swapping approach
    
    Time: O(n!)
    Space: O(n)
    """
    result = []
    
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
        
        for i in range(start, len(nums)):
            # Swap
            nums[start], nums[i] = nums[i], nums[start]
            # Recurse
            backtrack(start + 1)
            # Backtrack
            nums[start], nums[i] = nums[i], nums[start]
    
    backtrack(0)
    return result


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],
        [0, 1],
        [1],
    ]
    
    print("=" * 70)
    print("🧪 TESTING PERMUTATIONS")
    print("=" * 70)
    
    for nums in test_cases:
        result1 = permute(nums.copy())
        result2 = permute_swap(nums.copy())
        
        print(f"\nInput: {nums}")
        print(f"Count: {len(result1)} permutations")
        print(f"Result: {result1}")

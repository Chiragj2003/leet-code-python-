"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #152 - Maximum Product Subarray                   ║
║                    Topic: Array (Dynamic Programming)                        ║
║                    Difficulty: Medium                                         ║
║                    Company: Amazon, Google, Apple                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Find contiguous subarray with LARGEST PRODUCT (not sum!).
Watch out for negatives - they can turn small product into big!

EXAMPLES:
─────────
✓ Input: [2,3,-2,4]      → Output: 6 (subarray [2,3])
✓ Input: [-2]            → Output: -2 (only element)
✓ Input: [-2,0,-1]       → Output: 0 (empty subarray = 0)
✓ Input: [0,2]           → Output: 2

KEY INSIGHT:
────────────
Two negatives = positive! So -2 × -3 = 6 (big!)
Must track BOTH maximum AND minimum products.

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🍕 You're multiplying pizza slice sizes.
   Some are positive (extra large), some negative (debt/return).
   Two debts could pay off to huge profit!
   Track both biggest gain and biggest debt.

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   At Amazon, we analyze sales data. Products have price multipliers
   (positive for growth, negative for loss). We need to find best
   performing consecutive product period for Q reports.

📌 TASK:
   Find max product of any contiguous subarray.
   Time O(n), Space O(1).

📌 ACTION:
   Track both max and min products because:
   - min × negative = max (two negatives make positive!)
   
   ✓ Algorithm:
     1. Keep max_prod and min_prod at current position
     2. New max = max of (current, max*current, min*current)
     3. New min = min of (current, max*current, min*current)
     4. Track overall maximum

📌 RESULT:
   ✓ Time Complexity: O(n) - single pass
   ✓ Space Complexity: O(1) - only tracking min/max
   ✓ Reports ready instantly for quarterly analysis

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⏰ COMPLEXITY ANALYSIS                                    ║
╚══════════════════════════════════════════════════════════════════════════════╝

BRUTE FORCE (All Subarrays):
    Time: O(n²) - check all subarrays
    Space: O(1)

DYNAMIC PROGRAMMING (OPTIMAL):
    Time: O(n) - single pass
    Space: O(1) - only variables

"""

# ═══════════════════════════════════════════════════════════════════════════
# 🐢 BRUTE FORCE SOLUTION - O(n²) Time, O(1) Space
# ═══════════════════════════════════════════════════════════════════════════
def maxProduct_bruteforce(nums):
    """
    Brute Force: Check all possible subarrays
    
    STEPS (like a recipe):
    ──────────────────────
    1. For each starting position
    2. Calculate product of all subarrays from that start
    3. Track maximum product seen
    
    Example: [2,3,-2,4]
    ───────
    Start 0: [2]=2, [2,3]=6, [2,3,-2]=-12, [2,3,-2,4]=-48 → max=6
    Start 1: [3]=3, [3,-2]=-6, [3,-2,4]=-24 → max=6
    Start 2: [-2]=-2, [-2,4]=-8 → max=6
    Start 3: [4]=4 → max=6
    
    Final max: 6 ✓
    
    WHY IT'S SLOW:
    ──────────────
    Two nested loops checking all subarrays.
    For n elements, there are n(n+1)/2 subarrays!
    """
    if not nums:
        return 0
    
    max_product = nums[0]
    
    # Try all starting positions
    for i in range(len(nums)):
        current_product = 1
        
        # Try all ending positions from i
        for j in range(i, len(nums)):
            current_product *= nums[j]
            max_product = max(max_product, current_product)
    
    return max_product


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMIZED SOLUTION - DP Tracking Max and Min
# ═══════════════════════════════════════════════════════════════════════════
def maxProduct(nums):
    """
    Dynamic Programming - OPTIMAL for Amazon Interview!
    
    🔑 KEY INSIGHT:
    ───────────────
    At each position, track BOTH maximum and minimum products.
    Why minimum? Because negative × minimum = maximum!
    
    Example: [2,3,-2,4]
    ───────
    
    Position 0 (num=2):
      max_prod = 2, min_prod = 2, result = 2
    
    Position 1 (num=3):
      candidates: 3, 2*3=6, 2*3=6
      max_prod = 6, min_prod = 3, result = 6
    
    Position 2 (num=-2):
      candidates: -2, 6*(-2)=-12, 3*(-2)=-6
      When multiplying by negative, max and min swap!
      max_prod = max(-2, -12, -6) = -2
      min_prod = min(-2, -12, -6) = -12
      result = 6 (no change)
    
    Position 3 (num=4):
      candidates: 4, -2*4=-8, -12*4=-48
      max_prod = 4, min_prod = -48, result = 6
    
    Final: 6 ✓
    
    WHY THIS IS BEST FOR AMAZON:
    ─────────────────────────────
    ✓ O(n) time - single pass only
    ✓ O(1) space - just tracking variables
    ✓ Elegant DP approach
    ✓ Handles negatives perfectly
    """
    if not nums:
        return 0
    
    # Initialize with first element
    max_prod = min_prod = result = nums[0]
    
    # Process remaining elements
    for num in nums[1:]:
        # When multiplying by negative, max/min swap roles
        # So we need to consider all three: num itself, max*num, min*num
        candidates = (num, max_prod * num, min_prod * num)
        
        # Update max and min
        max_prod = max(candidates)
        min_prod = min(candidates)
        
        # Track overall maximum
        result = max(result, max_prod)
    
    return result


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE - Include zero handling explicitly
# ═══════════════════════════════════════════════════════════════════════════
def maxProduct_verbose(nums):
    """
    Verbose version showing logic step-by-step
    
    Same as optimal but with print statements for learning
    """
    if not nums:
        return 0
    
    print(f"\nArray: {nums}\n")
    
    max_prod = min_prod = result = nums[0]
    print(f"Initialize: max_prod={max_prod}, min_prod={min_prod}, result={result}\n")
    
    for i, num in enumerate(nums[1:], 1):
        print(f"Step {i}: num = {num}")
        
        # Calculate candidates
        candidate_current = num
        candidate_max_mult = max_prod * num
        candidate_min_mult = min_prod * num
        
        print(f"  Candidates:")
        print(f"    Just num: {candidate_current}")
        print(f"    max_prod * num: {max_prod} * {num} = {candidate_max_mult}")
        print(f"    min_prod * num: {min_prod} * {num} = {candidate_min_mult}")
        
        # Update max and min
        old_max = max_prod
        old_min = min_prod
        max_prod = max(candidate_current, candidate_max_mult, candidate_min_mult)
        min_prod = min(candidate_current, candidate_max_mult, candidate_min_mult)
        
        print(f"  Updated: max_prod={max_prod}, min_prod={min_prod}")
        
        result = max(result, max_prod)
        print(f"  Result so far: {result}\n")
    
    return result


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES - Verify all solutions work!
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Test cases with expected outputs
    test_cases = [
        ([2, 3, -2, 4], 6),
        ([-2], -2),
        ([0, 2], 2),
        ([-2, 0, -1], 0),
        ([2, -5, -2, -4, 3], 24),  # [-5, -2] = 10, 10*(-4) = -40, wait... [-2,-4,3] = 24
    ]
    
    print("=" * 70)
    print("🧪 TESTING MAXIMUM PRODUCT SUBARRAY SOLUTIONS")
    print("=" * 70)
    
    for nums, expected in test_cases:
        # Test solutions
        result_brute = maxProduct_bruteforce(nums.copy())
        result_optimal = maxProduct(nums.copy())
        
        status = "✓" if result_optimal == expected else "✗"
        
        print(f"\n{status} Input: {nums}")
        print(f"  Expected:      {expected}")
        print(f"  Brute Force:   {result_brute}")
        print(f"  DP (Best):     {result_optimal}")
    
    print("\n" + "=" * 70)
    print("📊 COMPLEXITY COMPARISON")
    print("=" * 70)
    print("| Method      | Time   | Space   | Amazon Recommended |")
    print("|-------------|--------|---------|-------------------|")
    print("| Brute Force | O(n²)  | O(1)    | ❌ Too slow       |")
    print("| DP          | O(n)   | O(1)    | ✅ BEST!          |")

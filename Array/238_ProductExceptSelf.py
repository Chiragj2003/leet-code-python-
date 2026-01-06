"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #238 - Product of Array Except Self               ║
║                    Topic: Array                                              ║
║                    Difficulty: Medium                                         ║
║                    Company: Amazon, Facebook, Google                         ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
For each position, return the PRODUCT of ALL OTHER elements (not including itself).
Can't use division!

EXAMPLES:
─────────
✓ Input: [1,2,3,4]       → Output: [24,12,8,6]
  - Position 0: 2*3*4 = 24
  - Position 1: 1*3*4 = 12
  - Position 2: 1*2*4 = 8
  - Position 3: 1*2*3 = 6

✓ Input: [-1,1,0,-3,3]   → Output: [0,0,9,0,0]

CONSTRAINT: Don't use division! Do in O(n) time, O(n) space for result.

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🎪 You're organizing circus performance times.
   For each performer, how long is total performance time
   when you exclude just that performer?

📊 Sales manager: Each salesperson's bonus depends on other salespeople's sales.
   For each person, calculate what they'd earn without themselves in team.

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   At Amazon, for each product, we calculate its "influence score"
   which is product of all OTHER products' ratings.
   This needs to be calculated without division due to data precision issues.

📌 TASK:
   Given array, return new array where each position contains
   product of all other elements. No division allowed!
   Time O(n), Space O(n) for output only.

📌 ACTION:
   Use two passes - left and right products:
   
   ✓ Algorithm:
     1. Left pass: Calculate product of all elements to the LEFT
     2. Right pass: Calculate product of all elements to the RIGHT
     3. Multiply left and right for each position

📌 RESULT:
   ✓ Time Complexity: O(n) - two passes
   ✓ Space Complexity: O(1) if output doesn't count
   ✓ Calculates influence scores instantly without division

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⏰ COMPLEXITY ANALYSIS                                    ║
╚══════════════════════════════════════════════════════════════════════════════╝

BRUTE FORCE (Calculate Total Product):
    Time: O(n²) - for each position, multiply all others
    Space: O(n)

DIVISION METHOD (if allowed):
    Time: O(n) - but division not allowed!
    Space: O(n)

TWO PASS LEFT-RIGHT (OPTIMAL):
    Time: O(n) - two passes
    Space: O(1) excluding output

"""

# ═══════════════════════════════════════════════════════════════════════════
# 🐢 BRUTE FORCE SOLUTION - O(n²) Time
# ═══════════════════════════════════════════════════════════════════════════
def productExceptSelf_bruteforce(nums):
    """
    Brute Force: For each position, multiply all others
    
    STEPS (like a recipe):
    ──────────────────────
    1. For each position i
    2. Calculate product of all elements except nums[i]
    3. Store in result
    
    Example: [1,2,3,4]
    ───────
    Position 0: 2*3*4 = 24
    Position 1: 1*3*4 = 12
    Position 2: 1*2*4 = 8
    Position 3: 1*2*3 = 6
    
    WHY IT'S SLOW:
    ──────────────
    For each of n positions, we multiply n-1 elements.
    That's O(n²) operations!
    """
    n = len(nums)
    result = [1] * n
    
    # For each position
    for i in range(n):
        # Calculate product of all except nums[i]
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        result[i] = product
    
    return result


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMIZED SOLUTION - Left and Right Products (AMAZON PREFERRED!)
# ═══════════════════════════════════════════════════════════════════════════
def productExceptSelf(nums):
    """
    Two Pass Solution - OPTIMAL for Amazon Interview!
    
    🔑 KEY INSIGHT:
    ───────────────
    For each position, answer = (product of all LEFT) × (product of all RIGHT)
    
    Example: [1,2,3,4]
    ───────
    
    LEFT PASS (product of elements to the left):
    Position 0: nothing to left → 1
    Position 1: 1 to left → 1
    Position 2: 1*2 to left → 2
    Position 3: 1*2*3 to left → 6
    Left = [1, 1, 2, 6]
    
    RIGHT PASS (product of elements to the right):
    Position 0: 2*3*4 to right → 24
    Position 1: 3*4 to right → 12
    Position 2: 4 to right → 4
    Position 3: nothing to right → 1
    
    COMBINE:
    Position 0: left[0] * right = 1 * 24 = 24 ✓
    Position 1: left[1] * right = 1 * 12 = 12 ✓
    Position 2: left[2] * right = 2 * 4 = 8 ✓
    Position 3: left[3] * right = 6 * 1 = 6 ✓
    
    Result: [24, 12, 8, 6] ✓
    
    WHY THIS IS BEST FOR AMAZON:
    ─────────────────────────────
    ✓ O(n) time - just two passes
    ✓ O(1) space - if output doesn't count
    ✓ Elegant and clean approach
    ✓ Scales to millions of products
    """
    n = len(nums)
    result = [1] * n
    
    # ═══ LEFT PASS ═══
    # Calculate product of all elements to LEFT of each position
    # Store in result[i]
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]
    
    # ═══ RIGHT PASS ═══
    # Multiply with product of all elements to RIGHT of each position
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE - Explicit Left and Right Arrays
# ═══════════════════════════════════════════════════════════════════════════
def productExceptSelf_explicit(nums):
    """
    Explicit Arrays - Easier to understand but uses more space
    
    STEPS:
    ──────
    1. Create left[] array - product of all LEFT
    2. Create right[] array - product of all RIGHT
    3. Multiply left[i] * right[i] for result
    
    Time: O(n)
    Space: O(n) - three arrays
    """
    n = len(nums)
    
    # left[i] = product of all elements to left of i
    left = [1] * n
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]
    
    # right[i] = product of all elements to right of i
    right = [1] * n
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]
    
    # Combine left and right
    result = [left[i] * right[i] for i in range(n)]
    return result


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES - Verify all solutions work!
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Test cases with expected outputs
    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([2, 3, 4, 5], [60, 40, 30, 24]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ]
    
    print("=" * 70)
    print("🧪 TESTING PRODUCT OF ARRAY EXCEPT SELF SOLUTIONS")
    print("=" * 70)
    
    for nums, expected in test_cases:
        # Test solutions
        result_brute = productExceptSelf_bruteforce(nums.copy())
        result_optimal = productExceptSelf(nums.copy())
        result_explicit = productExceptSelf_explicit(nums.copy())
        
        status = "✓" if result_optimal == expected else "✗"
        
        print(f"\n{status} Input: {nums}")
        print(f"  Expected:    {expected}")
        print(f"  Brute Force: {result_brute}")
        print(f"  Two Pass (Best): {result_optimal}")
        print(f"  Explicit:    {result_explicit}")
    
    print("\n" + "=" * 70)
    print("📊 COMPLEXITY COMPARISON")
    print("=" * 70)
    print("| Method       | Time   | Space   | Amazon Recommended |")
    print("|--------------|--------|---------|-------------------|")
    print("| Brute Force  | O(n²)  | O(1)    | ❌ Too slow       |")
    print("| Two Pass     | O(n)   | O(1)*   | ✅ BEST!          |")
    print("| Explicit     | O(n)   | O(n)    | ⚠️  More space    |")
    print("| *excluding output array")

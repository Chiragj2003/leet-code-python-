"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #268 - Missing Number                             ║
║                    Topic: Array / Math                                       ║
║                    Difficulty: Easy                                           ║
║                    Company: Amazon, Google, Apple                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
You have n numbers from a set of 0 to n, but ONE number is missing.
Find the missing number.

EXAMPLES:
─────────
✓ Input: [3, 0, 1]       → Output: 2 (missing 2, should have 0,1,2,3)
✓ Input: [0, 1]          → Output: 2 (missing 2)
✓ Input: [9,6,4,2,3,5,7,0,1] → Output: 8 (missing 8)

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🎟️ You have raffle tickets numbered 0 to 10.
   Someone gives you 9 of the 10 tickets, but one is lost!
   Which ticket number is missing?

📚 You have 10 books on a shelf. Books are numbered 0-10, but one isn't there.
   Which book is missing from the shelf?

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   At Amazon, user IDs are assigned sequentially 0 to n.
   We receive a batch of user IDs for processing, but data corruption
   causes one ID to go missing. We need to find which user ID is missing
   so we can investigate their account.

📌 TASK:
   Given array of n numbers from 0 to n, find the one missing number.
   Time O(n), Space O(1).

📌 ACTION:
   Use mathematical formula for sum of 0 to n:
   
   ✓ Algorithm:
     1. Expected sum = n * (n+1) / 2 (mathematical formula)
     2. Actual sum = sum of all array elements
     3. Missing = Expected - Actual

📌 RESULT:
   ✓ Time Complexity: O(n) - single pass to sum
   ✓ Space Complexity: O(1) - only store sum variable
   ✓ Finds missing user ID instantly at Amazon scale

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⏰ COMPLEXITY ANALYSIS                                    ║
╚══════════════════════════════════════════════════════════════════════════════╝

BRUTE FORCE (Check Each):
    Time: O(n²) - for each number, check if in array
    Space: O(1)

SORT APPROACH:
    Time: O(n log n) - sorting takes this time
    Space: O(1) if sorting in-place

MATH APPROACH (OPTIMAL):
    Time: O(n) - single pass
    Space: O(1) - only sum variable

XOR APPROACH:
    Time: O(n) - single pass
    Space: O(1) - only one variable

"""

# ═══════════════════════════════════════════════════════════════════════════
# 🐢 BRUTE FORCE SOLUTION - O(n²) Time, O(1) Space
# ═══════════════════════════════════════════════════════════════════════════
def missingNumber_bruteforce(nums):
    """
    Brute Force: Check each number from 0 to n
    
    STEPS (like a recipe):
    ──────────────────────
    1. For each number 0 to n
    2. Check if it exists in the array
    3. If not found, that's the missing number!
    
    Example: [3, 0, 1]
    ───────
    Check 0: found in array
    Check 1: found in array
    Check 2: NOT found! → Answer is 2
    
    WHY IT'S SLOW:
    ──────────────
    For each number 0 to n, we scan entire array to find it.
    That's n checks × n scans = n² operations!
    """
    n = len(nums)
    
    # Check each number from 0 to n
    for i in range(n + 1):
        if i not in nums:
            return i
    
    return -1


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMIZED SOLUTION 1 - Math Formula (AMAZON PREFERRED!)
# ═══════════════════════════════════════════════════════════════════════════
def missingNumber(nums):
    """
    Math Formula - OPTIMAL for Amazon Interview!
    
    🔑 KEY INSIGHT:
    ───────────────
    Sum of numbers 0 to n is always: n * (n+1) / 2
    
    Why?
    • 0+1+2+3 = 6 = 4*5/2 ✓
    • 0+1+2+3+4 = 10 = 5*6/2 ✓
    
    So: Missing = Expected sum - Actual sum
    
    Example: [3, 0, 1]
    ───────
    n = 3 (length)
    Should have: 0, 1, 2, 3
    Expected sum = 3 * 4 / 2 = 6
    Actual sum = 3 + 0 + 1 = 4
    Missing = 6 - 4 = 2 ✓
    
    Another example: [0, 1]
    ──────────────────────
    n = 2 (length)
    Should have: 0, 1, 2
    Expected sum = 2 * 3 / 2 = 3
    Actual sum = 0 + 1 = 1
    Missing = 3 - 1 = 2 ✓
    
    WHY THIS IS BEST FOR AMAZON:
    ─────────────────────────────
    ✓ O(1) space - just sum variables
    ✓ O(n) time - single pass
    ✓ Clean mathematical approach
    ✓ Elegant and efficient
    """
    n = len(nums)
    
    # Expected sum using mathematical formula
    expected_sum = n * (n + 1) // 2
    
    # Actual sum of array
    actual_sum = sum(nums)
    
    # Missing number
    return expected_sum - actual_sum


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE 1 - XOR Method
# ═══════════════════════════════════════════════════════════════════════════
def missingNumber_xor(nums):
    """
    XOR Method - Also O(n) time, O(1) space
    
    🔑 KEY INSIGHT:
    ───────────────
    XOR properties:
    • a ^ a = 0 (same numbers cancel out)
    • a ^ 0 = a (XOR with 0 gives original)
    • Order doesn't matter
    
    If we XOR all indices with all values:
    • Pairs cancel out (become 0)
    • Missing number remains!
    
    Example: [3, 0, 1]
    ───────
    XOR indices: 0 ^ 1 ^ 2 ^ 3 (indices)
    XOR values:  3 ^ 0 ^ 1 (array values)
    
    Combined: 0^3 ^ 1^0 ^ 2 ^ 3^1
            = 0 ^ 0 ^ 2 ^ 0
            = 2 ✓
    
    Time: O(n)
    Space: O(1)
    """
    n = len(nums)
    result = n  # Start with n
    
    for i, num in enumerate(nums):
        result ^= i ^ num  # XOR with both index and value
    
    return result


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE 2 - Set Method
# ═══════════════════════════════════════════════════════════════════════════
def missingNumber_set(nums):
    """
    Set Method - O(n) time, O(n) space
    
    STEPS (like a recipe):
    ──────────────────────
    1. Create set of all numbers 0 to n
    2. Go through array and remove numbers
    3. Remaining number is missing
    
    Example: [3, 0, 1]
    ───────
    Create set: {0, 1, 2, 3}
    Remove 3: {0, 1, 2}
    Remove 0: {1, 2}
    Remove 1: {2}
    Remaining: 2 ✓
    
    Time: O(n)
    Space: O(n) - create set of size n+1
    """
    n = len(nums)
    num_set = set(range(n + 1))  # {0, 1, 2, ..., n}
    
    for num in nums:
        num_set.remove(num)
    
    return num_set.pop()


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES - Verify all solutions work!
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Test cases with expected outputs
    test_cases = [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ([0], 1),
        ([1], 0),
        ([1, 0], 2),
    ]
    
    print("=" * 70)
    print("🧪 TESTING MISSING NUMBER SOLUTIONS")
    print("=" * 70)
    
    for nums, expected in test_cases:
        # Test all solutions
        result_brute = missingNumber_bruteforce(nums.copy())
        result_math = missingNumber(nums.copy())
        result_xor = missingNumber_xor(nums.copy())
        result_set = missingNumber_set(nums.copy())
        
        status = "✓" if result_math == expected else "✗"
        
        print(f"\n{status} Input: {nums}")
        print(f"  Expected:      {expected}")
        print(f"  Brute Force:   {result_brute}")
        print(f"  Math (Best):   {result_math}")
        print(f"  XOR:           {result_xor}")
        print(f"  Set:           {result_set}")
    
    print("\n" + "=" * 70)
    print("📊 COMPLEXITY COMPARISON")
    print("=" * 70)
    print("| Method      | Time      | Space   | Amazon Recommended |")
    print("|-------------|-----------|---------|-------------------|")
    print("| Brute Force | O(n²)     | O(1)    | ❌ Too slow       |")
    print("| Math        | O(n)      | O(1)    | ✅ BEST!          |")
    print("| XOR         | O(n)      | O(1)    | ✅ BEST!          |")
    print("| Set         | O(n)      | O(n)    | ⚠️  Extra space   |")

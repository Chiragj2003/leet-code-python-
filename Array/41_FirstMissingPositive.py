"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #41 - First Missing Positive                      ║
║                    Topic: Array                                              ║
║                    Difficulty: Hard                                           ║
║                    Company: Amazon, Google, Facebook                         ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Find the SMALLEST POSITIVE INTEGER that is MISSING from array.
(Positive integers start from 1, not 0)

EXAMPLES:
─────────
✓ Input: [3,4,-1,1]     → Output: 2 (1 is there, 2 is missing)
✓ Input: [1,2,0]        → Output: 3 (1,2 are there, 3 is missing)
✓ Input: [7,8,9,11,12]  → Output: 1 (1 is missing, that's first!)

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🎂 You're slicing a birthday cake. You need pieces 1, 2, 3, 4...
   But some pieces are missing or broken!
   What's the first good piece number you don't have?

🎪 Circus seats are numbered 1, 2, 3, 4...
   Some people didn't show up and their seats are empty.
   What's the first empty seat?

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   At Amazon, user accounts are assigned IDs 1, 2, 3, ... sequentially.
   Due to deletions, some IDs are missing. We need to find the first missing
   ID to assign it to the next new account registration.

📌 TASK:
   Given array of integers, find smallest missing positive integer.
   Time O(n), Space O(1), can't use extra space like hashmap.

📌 ACTION:
   Use array itself as a hash table! Place each valid number in its "home":
   
   ✓ Algorithm:
     1. For each number i in range [1, n], place it at index i-1
     2. After arrangement, scan and find first index where number ≠ index+1
     3. Missing number is index+1

📌 RESULT:
   ✓ Time Complexity: O(n) - each element moved at most once
   ✓ Space Complexity: O(1) - in-place arrangement
   ✓ Finds missing account ID instantly without extra memory

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⏰ COMPLEXITY ANALYSIS                                    ║
╚══════════════════════════════════════════════════════════════════════════════╝

BRUTE FORCE (Check Each):
    Time: O(n²) - check each number
    Space: O(1)

HASHMAP APPROACH:
    Time: O(n)
    Space: O(n) - can't use, constraints forbid it

ARRAY AS HASH (OPTIMAL):
    Time: O(n) - clever in-place hashing
    Space: O(1) - no extra space!

"""

# ═══════════════════════════════════════════════════════════════════════════
# 🐢 BRUTE FORCE SOLUTION - O(n²) Time, O(1) Space
# ═══════════════════════════════════════════════════════════════════════════
def firstMissingPositive_bruteforce(nums):
    """
    Brute Force: Check each positive integer starting from 1
    
    STEPS (like a recipe):
    ──────────────────────
    1. Start checking from number 1
    2. Is 1 in array? If no, return 1
    3. Check 2: Is 2 in array? If no, return 2
    4. Keep checking until find missing
    
    Example: [3,4,-1,1]
    ───────
    Check 1: found in array
    Check 2: NOT found in array → Return 2 ✓
    
    WHY IT'S SLOW:
    ──────────────
    For each number, we scan entire array.
    Like checking every person in a concert for identity.
    Takes forever for large arrays!
    """
    n = len(nums)
    
    # Check each positive integer from 1 to n+1
    for i in range(1, n + 2):
        if i not in nums:
            return i
    
    return -1


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMIZED SOLUTION - Array as Hash (AMAZON PREFERRED!)
# ═══════════════════════════════════════════════════════════════════════════
def firstMissingPositive(nums):
    """
    Array as Hash Table - OPTIMAL for Amazon Interview!
    
    🔑 KEY INSIGHT:
    ───────────────
    For array of size n, answer must be in range [1, n+1]
    
    Why? If array has all numbers 1 to n, answer is n+1.
    If array is missing any number in [1, n], that's our answer.
    
    Use array indices as hash keys!
    • Number i should go at index i-1
    • Number 1 at index 0
    • Number 2 at index 1, etc.
    
    Example: [3,4,-1,1]
    ───────
    n = 4, so answer in range [1, 5]
    
    Place numbers in their homes:
    Initial: [3, 4, -1, 1]
    - 3 belongs at index 2: swap(index 0, index 2)
      [-1, 4, 3, 1]
    - Skip -1 (out of range)
    - 4 belongs at index 3: swap(index 1, index 3)
      [-1, 1, 3, 4]
    - Ignore -1
    - 1 belongs at index 0: swap(index 2, index 0)
      [1, -1, 3, 4]
    - Done!
    
    Final: [1, -1, 3, 4]
    
    Now check: Index 1 has -1, but should have 2
    → Answer is 2 ✓
    
    WHY THIS IS BEST FOR AMAZON:
    ─────────────────────────────
    ✓ O(1) space - no extra hashmap!
    ✓ O(n) time - each element moved at most once
    ✓ Clever use of array indices as hash keys
    ✓ Solves hard problem with minimal resources
    """
    n = len(nums)
    
    # Step 1: Place each number in its correct position
    # Number i should be at index i-1
    for i in range(n):
        # Keep swapping until nums[i] is in correct spot OR can't move
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            # Calculate correct index for nums[i]
            correct_idx = nums[i] - 1
            
            # Swap current number with number at correct position
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
    
    # Step 2: Find first number not in correct position
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1  # i should have number i+1
    
    # Step 3: All numbers 1 to n are in place
    return n + 1


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE 1 - Set Method
# ═══════════════════════════════════════════════════════════════════════════
def firstMissingPositive_set(nums):
    """
    Set Method - Simple but uses O(n) space
    
    STEPS (like a recipe):
    ──────────────────────
    1. Create set of all numbers
    2. Check numbers 1, 2, 3, ... until find missing
    
    Time: O(n)
    Space: O(n)
    """
    num_set = set(nums)
    
    # Check from 1 onwards
    i = 1
    while i in num_set:
        i += 1
    
    return i


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES - Verify all solutions work!
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Test cases with expected outputs
    test_cases = [
        ([3, 4, -1, 1], 2),
        ([1, 2, 0], 3),
        ([7, 8, 9, 11, 12], 1),
        ([1], 2),
        ([2], 1),
        ([1, 1], 2),
        ([1, 2, 3], 4),
    ]
    
    print("=" * 70)
    print("🧪 TESTING FIRST MISSING POSITIVE SOLUTIONS")
    print("=" * 70)
    
    for nums, expected in test_cases:
        # Test all solutions
        result_brute = firstMissingPositive_bruteforce(nums.copy())
        result_optimal = firstMissingPositive(nums.copy())
        result_set = firstMissingPositive_set(nums.copy())
        
        status = "✓" if result_optimal == expected else "✗"
        
        print(f"\n{status} Input: {nums}")
        print(f"  Expected:      {expected}")
        print(f"  Brute Force:   {result_brute}")
        print(f"  Array Hash (Best): {result_optimal}")
        print(f"  Set:           {result_set}")
    
    print("\n" + "=" * 70)
    print("📊 COMPLEXITY COMPARISON")
    print("=" * 70)
    print("| Method      | Time   | Space   | Amazon Recommended |")
    print("|-------------|--------|---------|-------------------|")
    print("| Brute Force | O(n²)  | O(1)    | ❌ Too slow       |")
    print("| Set         | O(n)   | O(n)    | ⚠️  Extra memory  |")
    print("| Array Hash  | O(n)   | O(1)    | ✅ BEST!          |")

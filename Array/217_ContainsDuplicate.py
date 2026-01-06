"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #217 - Contains Duplicate                         ║
║                    Topic: Array / Hashmap                                    ║
║                    Difficulty: Easy                                           ║
║                    Company: Amazon, Google, Facebook                         ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Check if array has any duplicate values.
Return True if there's a duplicate, False if all are unique.

EXAMPLES:
─────────
✓ Input: [1, 2, 3, 1]    → Output: True (1 appears twice)
✓ Input: [1, 2, 3, 4]    → Output: False (all unique)
✓ Input: [99, 99]        → Output: True (duplicate)

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🎫 In a movie theater, each person has a unique ticket number.
   You check each person's ticket. If you see the same number twice,
   someone has a fake ticket! Report: "Found a duplicate!"

📋 In a classroom, teacher calls role and remembers who answered.
   If same name called again, teacher knows someone is playing tricks!

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   At Amazon Warehouse, we track product barcodes as items arrive.
   Each unique item should have a unique barcode.
   We need to quickly detect if any duplicate/fake barcode enters the system
   to prevent inventory errors.

📌 TASK:
   Given an array of integers, determine if any value appears more than once.
   Return boolean: True if duplicate exists, False if all unique.

📌 ACTION:
   Use a Set to track seen numbers:
   
   ✓ Algorithm:
     1. Create empty set (memory of seen numbers)
     2. Go through each number
     3. If in set, we found duplicate! Return True
     4. If not in set, add it and continue
     5. If we finish loop, no duplicates. Return False

📌 RESULT:
   ✓ Time Complexity: O(n) - visit each element once
   ✓ Space Complexity: O(n) - set can store all unique elements
   ✓ Fast detection prevents system issues before they multiply

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⏰ COMPLEXITY ANALYSIS                                    ║
╚══════════════════════════════════════════════════════════════════════════════╝

BRUTE FORCE (Nested Loop):
    Time: O(n²) - For each element, check all others
    Space: O(1) - No extra space

SORT APPROACH:
    Time: O(n log n) - Sorting takes this time
    Space: O(1) - If sorting in-place

SET APPROACH (OPTIMAL):
    Time: O(n) - Single pass with hash table
    Space: O(n) - Store seen elements

"""

# ═══════════════════════════════════════════════════════════════════════════
# 🐢 BRUTE FORCE SOLUTION - O(n²) Time, O(1) Space
# ═══════════════════════════════════════════════════════════════════════════
def containsDuplicate_bruteforce(nums):
    """
    Brute Force: Check every pair of numbers
    
    STEPS (like a recipe):
    ──────────────────────
    1. Pick first number
    2. Compare with ALL other numbers
    3. If find match, return True (duplicate found!)
    4. Pick next number and repeat
    
    Example: [1, 2, 3, 1]
    ───────
    Compare 1 (index 0) with: 2, 3, 1 → Found 1 at index 3! Return True
    
    WHY IT'S SLOW:
    ──────────────
    Like checking every person in a concert against every other person
    to see if they're the same person. That's lots of comparing!
    
    Time: O(n²) because of nested loops
    """
    # Check every pair of numbers
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True  # Found duplicate!
    
    return False  # No duplicates


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMIZED SOLUTION 1 - Set (AMAZON PREFERRED!)
# ═══════════════════════════════════════════════════════════════════════════
def containsDuplicate(nums):
    """
    Set Solution - OPTIMAL for Amazon Interview!
    
    🔑 KEY INSIGHT:
    ───────────────
    Set stores unique values only. As we add numbers:
    • If number already in set, we found duplicate!
    • If number not in set, add it and continue
    
    Example: [1, 2, 3, 1]
    ───────
    
    Step 1: num=1, seen={}, add 1 → seen={1}
    Step 2: num=2, seen={1}, add 2 → seen={1, 2}
    Step 3: num=3, seen={1, 2}, add 3 → seen={1, 2, 3}
    Step 4: num=1, seen={1, 2, 3}, 1 already in set! 
            → Duplicate found! Return True ✓
    
    VISUAL REPRESENTATION:
    ─────────────────────
    Array:  [1, 2, 3, 1]
                      ↑ Found duplicate here!
    
    WHY THIS IS BEST FOR AMAZON:
    ─────────────────────────────
    ✓ O(n) time - single pass only
    ✓ Simple and clean code
    ✓ Hash set lookup is O(1) average case
    ✓ Scalable for large datasets
    """
    # Set to track numbers we've seen
    seen = set()
    
    for num in nums:
        # If we've seen this number before → duplicate!
        if num in seen:
            return True
        
        # Remember this number
        seen.add(num)
    
    # No duplicates found
    return False


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE 1 - Pythonic One-Liner
# ═══════════════════════════════════════════════════════════════════════════
def containsDuplicate_pythonic(nums):
    """
    Pythonic: Compare set size with list size
    
    💡 KEY INSIGHT:
       If set size < list size, there must be duplicates!
       set() automatically removes duplicates.
    
    Example: [1, 2, 3, 1]
    ───────
    - List: [1, 2, 3, 1], len = 4
    - Set:  {1, 2, 3}, len = 3
    - 4 ≠ 3, so there are duplicates!
    
    Time: O(n)
    Space: O(n)
    """
    return len(nums) != len(set(nums))


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE 2 - Sort Approach
# ═══════════════════════════════════════════════════════════════════════════
def containsDuplicate_sort(nums):
    """
    Sort: After sorting, duplicates will be adjacent
    
    STEPS (like a recipe):
    ──────────────────────
    1. Sort the array
    2. Check each adjacent pair
    3. If adjacent numbers match, found duplicate!
    
    Example: [1, 2, 3, 1]
    ───────
    After sorting: [1, 1, 2, 3]
    Check pairs: 1==1 → Found duplicate! Return True
    
    Time: O(n log n) for sorting
    Space: O(1) if sorting in-place
    """
    if len(nums) <= 1:
        return False
    
    # Sort the array
    nums_sorted = sorted(nums)
    
    # Check adjacent elements
    for i in range(len(nums_sorted) - 1):
        if nums_sorted[i] == nums_sorted[i + 1]:
            return True
    
    return False


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES - Verify all solutions work!
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Test cases with expected outputs
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([99, 99], True),
        ([1], False),
        ([1, 2, 3, 4, 5, 1], True),
        ([], False),
    ]
    
    print("=" * 70)
    print("🧪 TESTING CONTAINS DUPLICATE SOLUTIONS")
    print("=" * 70)
    
    for nums, expected in test_cases:
        # Test all solutions
        result_brute = containsDuplicate_bruteforce(nums.copy())
        result_set = containsDuplicate(nums.copy())
        result_pythonic = containsDuplicate_pythonic(nums.copy())
        result_sort = containsDuplicate_sort(nums.copy())
        
        status = "✓" if result_set == expected else "✗"
        
        print(f"\n{status} Input: {nums}")
        print(f"  Expected:     {expected}")
        print(f"  Brute Force:  {result_brute}")
        print(f"  Set (Best):   {result_set}")
        print(f"  Pythonic:     {result_pythonic}")
        print(f"  Sort:         {result_sort}")
    
    print("\n" + "=" * 70)
    print("📊 COMPLEXITY COMPARISON")
    print("=" * 70)
    print("| Method      | Time      | Space   | Amazon Recommended |")
    print("|-------------|-----------|---------|-------------------|")
    print("| Brute Force | O(n²)     | O(1)    | ❌ Too slow       |")
    print("| Sort        | O(n log n)| O(1)    | ⚠️  OK            |")
    print("| Set         | O(n)      | O(n)    | ✅ BEST!          |")
    print("| Pythonic    | O(n)      | O(n)    | ✅ BEST!          |")

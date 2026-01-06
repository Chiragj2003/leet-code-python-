"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #136 - Single Number                              ║
║                    Topic: Array / Bit Manipulation                            ║
║                    Difficulty: Easy                                           ║
║                    Company: Amazon, Google, Microsoft                         ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
You have a list of numbers where EVERY number appears TWICE... except ONE!
Find that special number that appears only ONCE.

EXAMPLES:
─────────
✓ Input: [2, 2, 1]         → Output: 1  (2 appears twice, 1 appears once)
✓ Input: [4, 1, 2, 1, 2]   → Output: 4  (1 and 2 appear twice, 4 only once)
✓ Input: [1]               → Output: 1  (only one number)

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🧤 Think of a classroom where everyone has a buddy (partner).
   Everyone is holding hands with their buddy... EXCEPT one person!
   Your job is to find the person without a buddy.

👔 Or imagine socks! You're pairing socks and one sock has no match.
   Which sock is the lonely one? That's our answer!

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   At Amazon, we process millions of transaction IDs. Each valid transaction 
   has a confirmation ID that appears twice (once for request, once for response).
   Sometimes a transaction fails and has only one ID entry.
   We need to find failed transactions efficiently with minimal memory usage.

📌 TASK:
   Given an array where every element appears twice except one,
   find that single element in O(n) time and O(1) space.

📌 ACTION:
   I would use the XOR (Exclusive OR) bit manipulation technique because:
   
   ✓ XOR has special properties:
     • a ^ a = 0  (same numbers cancel out)
     • a ^ 0 = a  (XOR with 0 gives original)
     • Order doesn't matter (commutative)
   
   ✓ Algorithm:
     1. Initialize result = 0
     2. XOR every number with result
     3. All pairs cancel out, single number remains!

📌 RESULT:
   ✓ Time Complexity: O(n) - single pass through array
   ✓ Space Complexity: O(1) - only one variable needed
   ✓ This handles millions of records efficiently at Amazon scale

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⏰ COMPLEXITY ANALYSIS                                    ║
╚══════════════════════════════════════════════════════════════════════════════╝

BRUTE FORCE:
    Time: O(n²) - For each number, scan entire array to count
    Space: O(1) - No extra space

OPTIMIZED:
    Time: O(n) - Single pass using XOR
    Space: O(1) - Only one variable

"""

# ═══════════════════════════════════════════════════════════════════════════
# 🐢 BRUTE FORCE SOLUTION - O(n²) Time, O(1) Space
# ═══════════════════════════════════════════════════════════════════════════
def singleNumber_bruteforce(nums):
    """
    Brute Force: Count occurrence of each number
    
    STEPS (like a recipe):
    ─────────────────────
    1. Pick one number from the list
    2. Count how many times it appears in the list
    3. If it appears only once, that's our answer!
    4. If not, pick the next number and repeat
    
    Example: [4, 1, 2, 1, 2]
    ───────
    Step 1: Pick 4
            Count 4s in list: 4 appears 1 time → Found it! Return 4
    
    (If 4 appeared twice, we'd continue checking 1, then 2, etc.)
    
    WHY IT'S SLOW:
    ──────────────
    For each number, we scan the entire array to count occurrences.
    Like checking every student one by one if they have a buddy.
    
    Time: O(n²) because for each of n elements, we scan all n elements
    """
    # Go through each number in the list
    for i in range(len(nums)):
        # Count how many times this number appears
        count = 0
        for j in range(len(nums)):
            if nums[j] == nums[i]:
                count += 1
        
        # If this number appears only once, it's the answer!
        if count == 1:
            return nums[i]
    
    return -1  # Should never reach here if input is valid


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMIZED SOLUTION - O(n) Time, O(1) Space (AMAZON PREFERRED!)
# ═══════════════════════════════════════════════════════════════════════════
def singleNumber(nums):
    """
    XOR Solution - OPTIMAL for Amazon Interview!
    
    🔑 KEY INSIGHT - XOR Magic Properties:
    ─────────────────────────────────────
    • 5 ^ 5 = 0        (any number XOR itself = 0)
    • 5 ^ 0 = 5        (any number XOR 0 = itself)
    • Order doesn't matter: a ^ b ^ c = c ^ a ^ b
    
    SO WHAT HAPPENS?
    ────────────────
    If we XOR all numbers together:
    • Pairs cancel out (become 0)
    • Single number XOR 0 = single number
    
    Example: [4, 1, 2, 1, 2]
    ───────
    4 ^ 1 ^ 2 ^ 1 ^ 2
    = 4 ^ (1 ^ 1) ^ (2 ^ 2)    ← Rearrange pairs together
    = 4 ^ 0 ^ 0                 ← Pairs become 0
    = 4                         ← Answer!
    
    VISUAL STEP BY STEP:
    ───────────────────
    result = 0 (start with 0)
    
    Step 1: result = 0 ^ 4 = 4
    Step 2: result = 4 ^ 1 = 5
    Step 3: result = 5 ^ 2 = 7
    Step 4: result = 7 ^ 1 = 6  (second 1 starts canceling)
    Step 5: result = 6 ^ 2 = 4  (second 2 cancels, back to 4!)
    
    Final: 4 ✓
    
    WHY THIS IS BEST FOR AMAZON:
    ─────────────────────────────
    ✓ O(1) space - perfect for large-scale systems
    ✓ O(n) time - single pass
    ✓ Elegant and efficient
    ✓ Shows deep understanding of bit operations
    """
    # Start with 0 (identity element for XOR)
    result = 0
    
    # XOR every number
    for num in nums:
        result ^= num  # Same as: result = result ^ num
    
    # All pairs cancelled out, only single number remains!
    return result


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE 1 - HashMap Approach O(n) Time, O(n) Space
# ═══════════════════════════════════════════════════════════════════════════
def singleNumber_hashmap(nums):
    """
    HashMap: Store counts in a dictionary
    
    STEPS (like a recipe):
    ──────────────────────
    1. Create an empty dictionary (like a notebook)
    2. Go through each number, write how many times you see it
    3. Find the number that appears only once
    
    Example: [4, 1, 2, 1, 2]
    ───────
    Building dictionary:
    - See 4: {4: 1}
    - See 1: {4: 1, 1: 1}
    - See 2: {4: 1, 1: 1, 2: 1}
    - See 1: {4: 1, 1: 2, 2: 1}  ← 1 now appears twice
    - See 2: {4: 1, 1: 2, 2: 2}  ← 2 now appears twice
    
    Check dictionary: 4 has count 1 → Answer is 4!
    
    Time: O(n) - Two passes (count + find)
    Space: O(n) - Store all unique numbers
    """
    # Step 1: Create empty dictionary to store counts
    count_dict = {}
    
    # Step 2: Count each number
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1  # Seen before, increase count
        else:
            count_dict[num] = 1   # First time seeing this number
    
    # Step 3: Find the number with count = 1
    for num, count in count_dict.items():
        if count == 1:
            return num
    
    return -1


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE 2 - Math Trick O(n) Time, O(n) Space
# ═══════════════════════════════════════════════════════════════════════════
def singleNumber_math(nums):
    """
    Math Trick: 2 * sum(unique) - sum(all) = single number
    
    WHY DOES THIS WORK?
    ──────────────────
    If array is [a, a, b, b, c]:
    - Sum of unique: a + b + c
    - Sum of all: a + a + b + b + c = 2a + 2b + c
    - 2 * (a + b + c) - (2a + 2b + c) = c (the single one!)
    
    Example: [4, 1, 2, 1, 2]
    ───────
    - Unique numbers: {4, 1, 2}, sum = 7
    - All numbers sum: 4+1+2+1+2 = 10
    - 2 * 7 - 10 = 14 - 10 = 4 ✓
    
    Time: O(n) - Two passes (unique sum + total sum)
    Space: O(n) - set() stores unique numbers
    """
    # set() removes duplicates automatically
    unique_sum = sum(set(nums))
    total_sum = sum(nums)
    
    # Single number = 2 * (sum of unique) - (sum of all)
    return 2 * unique_sum - total_sum


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES - Verify all solutions work!
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Test cases with expected outputs
    test_cases = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
        ([5, 3, 5, 3, 7], 7),
        ([-2, -2, 1, 1, 4], 4),
    ]
    
    print("=" * 70)
    print("🧪 TESTING SINGLE NUMBER SOLUTIONS")
    print("=" * 70)
    
    for nums, expected in test_cases:
        # Test all solutions
        result_brute = singleNumber_bruteforce(nums.copy())
        result_xor = singleNumber(nums.copy())
        result_hash = singleNumber_hashmap(nums.copy())
        result_math = singleNumber_math(nums.copy())
        
        status = "✓" if result_xor == expected else "✗"
        
        print(f"\n{status} Input: {nums}")
        print(f"  Expected:     {expected}")
        print(f"  Brute Force:  {result_brute}")
        print(f"  XOR (Best):   {result_xor}")
        print(f"  HashMap:      {result_hash}")
        print(f"  Math:         {result_math}")
    
    print("\n" + "=" * 70)
    print("📊 COMPLEXITY COMPARISON")
    print("=" * 70)
    print("| Method      | Time    | Space   | Amazon Recommended |")
    print("|-------------|---------|---------|-------------------|")
    print("| Brute Force | O(n²)   | O(1)    | ❌ Too slow       |")
    print("| HashMap     | O(n)    | O(n)    | ⚠️  Good          |")
    print("| XOR         | O(n)    | O(1)    | ✅ BEST!          |")
    print("| Math        | O(n)    | O(n)    | ⚠️  Good          |")

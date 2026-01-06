"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #283 - Move Zeroes                                ║
║                    Topic: Array / Two Pointers                               ║
║                    Difficulty: Easy                                           ║
║                    Company: Amazon, Microsoft, Facebook                      ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Move all zeros to the end while keeping non-zero elements in their original order.
MUST modify array in-place (no extra array allowed).

EXAMPLES:
─────────
✓ Input: [0, 1, 0, 3, 12]  → Output: [1, 3, 12, 0, 0] (in-place)
✓ Input: [0]               → Output: [0]
✓ Input: [1, 2, 3]         → Output: [1, 2, 3]

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🛒 You're cleaning a shelf. You want all the items (non-zero) on the left,
   and all empty spaces (zeros) on the right.
   But you want to keep items in the order you found them!

🧊 Think of ice cubes in a tray with holes. You want all ice cubes pushed
   to one side, leaving empty holes on the other side.

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   At Amazon, we're processing customer IDs in a system. Some entries are
   invalid (represented as 0) and need to be moved to the end for cleanup.
   We need to do this in-place to save memory in AWS cloud systems.

📌 TASK:
   Move all zeros to end of array while maintaining order of non-zero elements.
   Modify array in-place. Time O(n), Space O(1).

📌 ACTION:
   Use two-pointer technique:
   
   ✓ Algorithm:
     1. left pointer tracks where to place next non-zero
     2. right pointer scans for non-zero elements
     3. When right finds non-zero, move it to left position
     4. After all non-zeros placed, fill rest with zeros

📌 RESULT:
   ✓ Time Complexity: O(n) - single pass
   ✓ Space Complexity: O(1) - in-place modification
   ✓ Saves memory in cloud systems, crucial for Amazon scale

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⏰ COMPLEXITY ANALYSIS                                    ║
╚══════════════════════════════════════════════════════════════════════════════╝

BRUTE FORCE (Create New Array):
    Time: O(n) - scan all elements
    Space: O(n) - create new array

TWO POINTERS (OPTIMAL):
    Time: O(n) - two passes
    Space: O(1) - in-place only

"""

# ═══════════════════════════════════════════════════════════════════════════
# 🐢 BRUTE FORCE SOLUTION - O(n) Time, O(n) Space
# ═══════════════════════════════════════════════════════════════════════════
def moveZeroes_bruteforce(nums):
    """
    Brute Force: Create new array with non-zeros first
    
    STEPS (like a recipe):
    ──────────────────────
    1. Create new array
    2. Add all non-zero numbers from original
    3. Add zeros at the end to match original length
    4. Copy back to original array
    
    Example: [0, 1, 0, 3, 12]
    ───────
    1. Create new array
    2. Non-zeros: [1, 3, 12]
    3. Add zeros: [1, 3, 12, 0, 0]
    4. Copy back to original
    
    WHY IT'S WASTEFUL:
    ──────────────────
    We create an entire new array! Uses extra memory.
    For Amazon with millions of arrays, this is expensive.
    """
    n = len(nums)
    
    # Step 1: Collect all non-zero elements
    non_zeros = [x for x in nums if x != 0]
    
    # Step 2: Calculate how many zeros we need
    zero_count = n - len(non_zeros)
    
    # Step 3: Build result array
    result = non_zeros + [0] * zero_count
    
    # Step 4: Copy back to original
    nums[:] = result


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMIZED SOLUTION - Two Pointers (AMAZON PREFERRED!)
# ═══════════════════════════════════════════════════════════════════════════
def moveZeroes(nums):
    """
    Two Pointers - OPTIMAL for Amazon Interview!
    
    🔑 KEY INSIGHT:
    ───────────────
    Use two pointers:
    • left: tracks where to place next non-zero
    • right: scans for non-zero elements
    
    Example: [0, 1, 0, 3, 12]
    ───────
    
    Pointer positions (showing state after each step):
    left=0 (where to place next non-zero)
    
    Step 1: right=0, nums[0]=0 (zero, skip)
    Step 2: right=1, nums[1]=1 (non-zero!)
            Place at left: nums[0]=1 → [1, 1, 0, 3, 12], left=1
    Step 3: right=2, nums[2]=0 (zero, skip)
    Step 4: right=3, nums[3]=3 (non-zero!)
            Place at left: nums[1]=3 → [1, 3, 0, 3, 12], left=2
    Step 5: right=4, nums[4]=12 (non-zero!)
            Place at left: nums[2]=12 → [1, 3, 12, 3, 12], left=3
    Step 6: Fill rest with zeros: [1, 3, 12, 0, 0]
    
    WHY THIS IS BEST FOR AMAZON:
    ─────────────────────────────
    ✓ O(1) space - no extra array needed!
    ✓ O(n) time - still single pass
    ✓ In-place modification saves cloud memory
    ✓ Handles millions of arrays efficiently
    """
    # Pointer for where to place next non-zero
    left = 0
    
    # Find all non-zero elements and move them to front
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left] = nums[right]
            left += 1
    
    # Fill rest with zeros
    for i in range(left, len(nums)):
        nums[i] = 0


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE - Swap Method
# ═══════════════════════════════════════════════════════════════════════════
def moveZeroes_swap(nums):
    """
    Swap Method: Swap non-zero with leftmost zero
    
    STEPS (like a recipe):
    ──────────────────────
    When we find a non-zero, swap it with leftmost zero position
    
    Example: [0, 1, 0, 3, 12]
    ───────
    
    left=0 (tracks leftmost zero position)
    
    i=0: nums[0]=0, left stays 0
    i=1: nums[1]=1 (non-zero!), swap with nums[0]
         → [1, 0, 0, 3, 12], left=1
    i=2: nums[2]=0, left stays 1
    i=3: nums[3]=3 (non-zero!), swap with nums[1]
         → [1, 3, 0, 0, 12], left=2
    i=4: nums[4]=12 (non-zero!), swap with nums[2]
         → [1, 3, 12, 0, 0], left=3
    
    Time: O(n)
    Space: O(1)
    """
    left = 0  # Points to leftmost zero
    
    for right in range(len(nums)):
        if nums[right] != 0:
            # Swap non-zero with leftmost zero
            nums[left], nums[right] = nums[right], nums[left]
            left += 1


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES - Verify all solutions work!
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Test cases
    test_cases = [
        [0, 1, 0, 3, 12],
        [0],
        [1, 2, 3],
        [0, 0, 1],
        [2, 1],
        [0, 1],
    ]
    
    print("=" * 70)
    print("🧪 TESTING MOVE ZEROES SOLUTIONS")
    print("=" * 70)
    
    for original in test_cases:
        # Test brute force
        arr1 = original.copy()
        moveZeroes_bruteforce(arr1)
        
        # Test optimal
        arr2 = original.copy()
        moveZeroes(arr2)
        
        # Test swap
        arr3 = original.copy()
        moveZeroes_swap(arr3)
        
        status = "✓" if arr2 == arr1 else "✗"
        
        print(f"\n{status} Input: {original}")
        print(f"  Brute Force: {arr1}")
        print(f"  Two Pointers (Best): {arr2}")
        print(f"  Swap Method: {arr3}")
    
    print("\n" + "=" * 70)
    print("📊 COMPLEXITY COMPARISON")
    print("=" * 70)
    print("| Method      | Time   | Space   | Amazon Recommended |")
    print("|-------------|--------|---------|-------------------|")
    print("| Brute Force | O(n)   | O(n)    | ❌ Extra memory   |")
    print("| Two Pointers| O(n)   | O(1)    | ✅ BEST!          |")
    print("| Swap        | O(n)   | O(1)    | ✅ BEST!          |")

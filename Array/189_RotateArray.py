"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #189 - Rotate Array                               ║
║                    Topic: Array                                              ║
║                    Difficulty: Medium                                         ║
║                    Company: Amazon, Apple, Microsoft                         ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Rotate an array to the RIGHT by k steps.
MUST do it in-place with minimal extra space.

EXAMPLES:
─────────
✓ Input: [1,2,3,4,5,6,7], k=3 → Output: [5,6,7,1,2,3,4]
✓ Input: [1,2,3], k=1         → Output: [3,1,2]
✓ Input: [1,2,3], k=4         → Output: [3,1,2] (same as k=1)

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🔄 You have a circular merry-go-round with kids.
   Rotate everyone 3 positions to the right!

📿 Beads on a string - shift all beads right by k positions,
   wrapping around from end to start.

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   At Amazon Alexa, voice commands are stored in a rotating buffer.
   When new commands arrive, we need to shift the buffer right by k positions.
   We must save memory by doing this in-place without creating new buffers.

📌 TASK:
   Rotate array right by k steps in-place.
   Time O(n), Space O(1).

📌 ACTION:
   Use three-reverse technique:
   
   ✓ Algorithm:
     1. Reverse entire array
     2. Reverse first k elements
     3. Reverse remaining elements
     
   This achieves 90° rotation through multiple smaller reversals!

📌 RESULT:
   ✓ Time Complexity: O(n) - three passes
   ✓ Space Complexity: O(1) - in-place only
   ✓ Scales to millions of commands at Amazon

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⏰ COMPLEXITY ANALYSIS                                    ║
╚══════════════════════════════════════════════════════════════════════════════╝

BRUTE FORCE (Extra Array):
    Time: O(n)
    Space: O(n) - create new array

CYCLIC ROTATION:
    Time: O(n)
    Space: O(1) - but complex swapping

THREE REVERSE (OPTIMAL):
    Time: O(n) - three passes
    Space: O(1) - in-place

"""

# ═══════════════════════════════════════════════════════════════════════════
# 🐢 BRUTE FORCE SOLUTION - O(n) Time, O(n) Space
# ═══════════════════════════════════════════════════════════════════════════
def rotate_bruteforce(nums, k):
    """
    Brute Force: Use extra array
    
    STEPS (like a recipe):
    ──────────────────────
    1. Create new array of same size
    2. Calculate new position for each element
    3. Copy back to original
    
    Formula for new position: (i + k) % n
    
    Example: [1,2,3,4,5,6,7], k=3
    ───────
    Index 0: (0+3) % 7 = 3 → nums[0]=1 goes to position 3
    Index 1: (1+3) % 7 = 4 → nums[1]=2 goes to position 4
    Index 2: (2+3) % 7 = 5 → nums[2]=3 goes to position 5
    Index 3: (3+3) % 7 = 6 → nums[3]=4 goes to position 6
    Index 4: (4+3) % 7 = 0 → nums[4]=5 goes to position 0
    Index 5: (5+3) % 7 = 1 → nums[5]=6 goes to position 1
    Index 6: (6+3) % 7 = 2 → nums[6]=7 goes to position 2
    
    Result: [5,6,7,1,2,3,4] ✓
    
    WHY IT'S WASTEFUL:
    ──────────────────
    Uses O(n) extra space for new array.
    At Amazon scale, this multiplies memory usage!
    """
    n = len(nums)
    k = k % n  # Handle k > n
    
    # Create new array
    rotated = [0] * n
    
    # Calculate new position for each element
    for i in range(n):
        rotated[(i + k) % n] = nums[i]
    
    # Copy back to original
    nums[:] = rotated


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMIZED SOLUTION - Three Reverse (AMAZON PREFERRED!)
# ═══════════════════════════════════════════════════════════════════════════
def rotate(nums, k):
    """
    Three Reverse - OPTIMAL for Amazon Interview!
    
    🔑 KEY INSIGHT:
    ───────────────
    Three reversals achieve rotation!
    
    Example: [1,2,3,4,5,6,7], k=3
    ───────
    
    Step 1: Reverse entire array
    [1,2,3,4,5,6,7] → [7,6,5,4,3,2,1]
    
    Step 2: Reverse first k elements (k=3)
    [7,6,5,4,3,2,1] → [5,6,7,4,3,2,1]
            ↑↑↑
    
    Step 3: Reverse remaining elements
    [5,6,7,4,3,2,1] → [5,6,7,1,2,3,4]
          ↑↑↑↑↑
    
    Result: [5,6,7,1,2,3,4] ✓
    
    WHY THIS WORKS MATHEMATICALLY:
    ──────────────────────────────
    If we split array at position n-k:
    Original: [1,2,3] + [4,5,6,7]  (k=3, n=7, n-k=4)
    Want:     [5,6,7] + [1,2,3,4]
    
    Reverse all:    [7,6,5] + [4,3,2,1]
    Reverse first:  [5,6,7] + [4,3,2,1]
    Reverse second: [5,6,7] + [1,2,3,4] ✓
    
    WHY THIS IS BEST FOR AMAZON:
    ─────────────────────────────
    ✓ O(1) space - no extra array!
    ✓ O(n) time - just reversals
    ✓ In-place modification
    ✓ Scales to millions of rotations
    """
    n = len(nums)
    k = k % n  # Handle k > n
    
    def reverse(start, end):
        """Reverse array from start to end"""
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    # Step 1: Reverse entire array
    reverse(0, n - 1)
    
    # Step 2: Reverse first k elements
    reverse(0, k - 1)
    
    # Step 3: Reverse remaining elements
    reverse(k, n - 1)


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE - Cyclic Rotation
# ═══════════════════════════════════════════════════════════════════════════
def rotate_cyclic(nums, k):
    """
    Cyclic Rotation - Rotate 4 elements at a time
    
    Time: O(n)
    Space: O(1)
    
    More complex but shows understanding of cyclic patterns.
    """
    n = len(nums)
    k = k % n
    
    if k == 0:
        return
    
    count = 0  # Elements moved
    start = 0
    
    while count < n:
        current = start
        prev = nums[start]
        
        while True:
            next_idx = (current + k) % n
            nums[next_idx], prev = prev, nums[next_idx]
            current = next_idx
            count += 1
            
            if current == start:
                break
        
        start += 1


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES - Verify all solutions work!
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([1, 2, 3], 1, [3, 1, 2]),
        ([1, 2, 3], 4, [3, 1, 2]),  # k=4 same as k=1
        ([1], 1, [1]),
        ([-1], 2, [-1]),
    ]
    
    print("=" * 70)
    print("🧪 TESTING ROTATE ARRAY SOLUTIONS")
    print("=" * 70)
    
    for nums, k, expected in test_cases:
        # Test brute force
        arr1 = nums.copy()
        rotate_bruteforce(arr1, k)
        
        # Test optimal
        arr2 = nums.copy()
        rotate(arr2, k)
        
        # Test cyclic
        arr3 = nums.copy()
        rotate_cyclic(arr3, k)
        
        status = "✓" if arr2 == expected else "✗"
        
        print(f"\n{status} Input: {nums}, k={k}")
        print(f"  Expected:    {expected}")
        print(f"  Brute Force: {arr1}")
        print(f"  Reverse (Best): {arr2}")
        print(f"  Cyclic:      {arr3}")
    
    print("\n" + "=" * 70)
    print("📊 COMPLEXITY COMPARISON")
    print("=" * 70)
    print("| Method      | Time   | Space   | Amazon Recommended |")
    print("|-------------|--------|---------|-------------------|")
    print("| Brute Force | O(n)   | O(n)    | ❌ Extra memory   |")
    print("| Reverse     | O(n)   | O(1)    | ✅ BEST!          |")
    print("| Cyclic      | O(n)   | O(1)    | ⚠️  Complex       |")

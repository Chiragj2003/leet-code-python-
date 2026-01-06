"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #75 - Sort Colors                                 ║
║                    Topic: Array / Two Pointers / Dutch Flag                  ║
║                    Difficulty: Medium                                         ║
║                    Company: Amazon, Google, Microsoft                        ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Sort array containing only 0s, 1s, and 2s IN-PLACE.
(This is called "Dutch National Flag" problem)

EXAMPLES:
─────────
✓ Input: [2,0,2,1,1,0]   → Output: [0,0,1,1,2,2]
✓ Input: [2,0,1]         → Output: [0,1,2]
✓ Input: [0]             → Output: [0]

WHY TRICKY: Can't use sort() - must do in-place in O(n) time!

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🇳🇱 Dutch flags have colors: red (0), white (1), blue (2).
   Sort them from left to right without extra space!

🧿 Beads on a string: red, white, blue.
   Move all reds left, blues right, whites in middle.

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   At Amazon warehouse, items are tagged with colors (0=low, 1=medium, 2=high).
   We need to sort items by priority on conveyor belt in-place
   without stopping the line.

📌 TASK:
   Sort array with values 0, 1, 2 in-place.
   Time O(n), Space O(1).

📌 ACTION:
   Use three pointers technique:
   
   ✓ Algorithm:
     1. left pointer points to where 0s go
     2. curr pointer scans array
     3. right pointer points to where 2s go
     4. Move curr forward:
        - If 0: swap with left, move both
        - If 1: just move curr
        - If 2: swap with right, only move right back

📌 RESULT:
   ✓ Time Complexity: O(n) - single pass
   ✓ Space Complexity: O(1) - in-place
   ✓ Sorts items instantly without stopping conveyor

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⏰ COMPLEXITY ANALYSIS                                    ║
╚══════════════════════════════════════════════════════════════════════════════╝

BRUTE FORCE (Use Sort):
    Time: O(n log n)
    Space: O(1) if in-place

COUNTING METHOD:
    Time: O(n)
    Space: O(1) - count and overwrite

THREE POINTERS (OPTIMAL):
    Time: O(n) - single pass
    Space: O(1) - clever in-place

"""

# ═══════════════════════════════════════════════════════════════════════════
# 🐢 BRUTE FORCE SOLUTION - O(n log n) Time
# ═══════════════════════════════════════════════════════════════════════════
def sortColors_bruteforce(nums):
    """
    Brute Force: Use built-in sort
    
    STEPS:
    ──────
    1. Call built-in sort
    2. Done!
    
    BUT: Not showing understanding of algorithm!
    Interviewer wants to see your skills.
    """
    nums.sort()


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Three Pointers (AMAZON PREFERRED!)
# ═══════════════════════════════════════════════════════════════════════════
def sortColors(nums):
    """
    Three Pointers - OPTIMAL for Amazon Interview!
    
    🔑 KEY INSIGHT:
    ───────────────
    Divide array into three regions:
    [0s] | [1s] | [Unknown] | [2s]
     ↑          ↑           ↑       ↑
    left      curr        right    end
    
    Example: [2,0,2,1,1,0]
    ───────
    
    Initial:
    [2, 0, 2, 1, 1, 0]
     L  C              R
    
    Step 1: curr=0 (num=2), swap with right
    [0, 0, 2, 1, 1, 2]
     L  C           R
    (don't move curr, only right)
    
    Step 2: curr=0 (num=0), swap with left
    [0, 0, 2, 1, 1, 2]
     L  C
    (move both)
    
    Step 3: curr=1 (num=2), swap with right
    [0, 0, 1, 1, 2, 2]
        L  C     R
    
    Step 4: curr=1 (num=1), just move curr
    [0, 0, 1, 1, 2, 2]
        L     C  R
    
    Step 5: curr=2 (num=1), just move curr
    [0, 0, 1, 1, 2, 2]
        L        C R
    
    Step 6: curr >= right, done!
    
    Result: [0, 0, 1, 1, 2, 2] ✓
    
    WHY THIS IS BEST FOR AMAZON:
    ─────────────────────────────
    ✓ O(n) time - single pass
    ✓ O(1) space - no extra array
    ✓ In-place modification
    ✓ Shows deep understanding
    """
    left = 0        # Where 0s go
    curr = 0        # Current scanning position
    right = len(nums) - 1  # Where 2s go
    
    while curr <= right:
        if nums[curr] == 0:
            # Swap with left boundary (for 0s)
            nums[left], nums[curr] = nums[curr], nums[left]
            left += 1
            curr += 1
        elif nums[curr] == 2:
            # Swap with right boundary (for 2s)
            nums[curr], nums[right] = nums[right], nums[curr]
            right -= 1
            # Don't increment curr, need to check swapped value
        else:  # nums[curr] == 1
            # 1 is in correct zone, just move forward
            curr += 1


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE - Counting Method
# ═══════════════════════════════════════════════════════════════════════════
def sortColors_count(nums):
    """
    Counting Method: Count 0s, 1s, 2s then overwrite
    
    STEPS:
    ──────
    1. Count how many 0s, 1s, 2s
    2. Fill array: all 0s first, then 1s, then 2s
    
    Example: [2,0,2,1,1,0]
    ───────
    Count: 0→2, 1→2, 2→2
    Fill: [0,0,1,1,2,2]
    
    Time: O(n)
    Space: O(1) - only count variables
    """
    count = [0, 0, 0]  # count[i] = count of i
    
    # Count each color
    for num in nums:
        count[num] += 1
    
    # Fill array with counts
    idx = 0
    for color in range(3):
        for _ in range(count[color]):
            nums[idx] = color
            idx += 1


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [
        [2, 0, 2, 1, 1, 0],
        [2, 0, 1],
        [0],
        [2, 2, 0, 1],
        [0, 0, 1, 2, 2, 1],
    ]
    
    print("=" * 70)
    print("🧪 TESTING SORT COLORS SOLUTIONS")
    print("=" * 70)
    
    for original in test_cases:
        expected = sorted(original)
        
        # Test three pointers
        arr1 = original.copy()
        sortColors(arr1)
        
        # Test counting
        arr2 = original.copy()
        sortColors_count(arr2)
        
        status = "✓" if arr1 == expected else "✗"
        
        print(f"\n{status} Input:    {original}")
        print(f"  Expected: {expected}")
        print(f"  Pointers: {arr1}")
        print(f"  Counting: {arr2}")
    
    print("\n" + "=" * 70)
    print("📊 COMPLEXITY COMPARISON")
    print("=" * 70)
    print("| Method         | Time      | Space   | Amazon |")
    print("|----------------|-----------|---------|--------|")
    print("| Built-in sort  | O(n log n)| O(1)    | ❌     |")
    print("| Three Pointers | O(n)      | O(1)    | ✅     |")
    print("| Counting       | O(n)      | O(1)    | ✅     |")

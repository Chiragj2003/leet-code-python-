═══════════════════════════════════════════════════════════════════════════════════
                   ARRAY PROBLEMS - QUICK INDEX FOR AMAZON PREP
═══════════════════════════════════════════════════════════════════════════════════

🎯 HOW TO USE THIS FOLDER:
──────────────────────────
Each file is a COMPLETE, PRODUCTION-READY LeetCode solution with:
✓ Simple explanation (child-friendly)
✓ STAR methodology (Amazon interview format)
✓ Brute force solution (O(n²) or similar)
✓ Optimized solution (O(n) or best possible)
✓ Alternative approaches
✓ Real test cases
✓ Complexity analysis
✓ Detailed comments explaining every step

Each file is standalone - you can learn one problem per session!

═══════════════════════════════════════════════════════════════════════════════════

📁 FILE LISTING:
════════════════

🟢 EASY PROBLEMS (Start here for warm-up):
─────────────────────────────────────────
1. 136_SingleNumber.py
   Topic: Bit Manipulation
   Key: XOR cancellation (a ^ a = 0)
   Complexity: O(n) time, O(1) space
   When: Finding unpaired element

2. 217_ContainsDuplicate.py
   Topic: Hashmap
   Key: Set for O(1) lookup
   Complexity: O(n) time, O(n) space
   When: Checking for duplicates

3. 268_MissingNumber.py
   Topic: Math + XOR
   Key: Sum formula or XOR trick
   Complexity: O(n) time, O(1) space
   When: Finding missing from sequence

4. 283_MoveZeroes.py
   Topic: Two Pointers
   Key: In-place array manipulation
   Complexity: O(n) time, O(1) space
   When: Moving elements to end


🟡 MEDIUM PROBLEMS (Core Amazon questions):
────────────────────────────────────────────
5. 48_RotateImage.py
   Topic: Matrix Manipulation
   Key: Transpose + reverse pattern
   Complexity: O(n²) time, O(1) space
   When: 2D array transformations

6. 189_RotateArray.py
   Topic: Array Rotation
   Key: Three reversal technique
   Complexity: O(n) time, O(1) space
   When: Array shifting operations

7. 152_MaxProduct.py
   Topic: Dynamic Programming
   Key: Track both max and min
   Complexity: O(n) time, O(1) space
   When: Finding max subarray product (not sum!)

8. 238_ProductExceptSelf.py
   Topic: Array Manipulation
   Key: Left-right pass approach
   Complexity: O(n) time, O(1) space*
   When: Element-wise product calculation

9. 169_MajorityElement.py
   Topic: Boyer-Moore Voting
   Key: Voting algorithm elegance
   Complexity: O(n) time, O(1) space
   When: Finding majority element

10. 75_SortColors.py
    Topic: Three Pointers / Dutch Flag
    Key: In-place three-way partition
    Complexity: O(n) time, O(1) space
    When: Sorting limited value range

11. 56_MergeIntervals.py
    Topic: Sorting + Greedy
    Key: Sort then merge logic
    Complexity: O(n log n) time, O(n) space
    When: Merging overlapping ranges


🔴 HARD PROBLEMS (Advanced understanding):
──────────────────────────────────────────
12. 41_FirstMissingPositive.py
    Topic: In-Place Array Hashing
    Key: Array indices as hash keys
    Complexity: O(n) time, O(1) space
    When: Finding first missing positive


═══════════════════════════════════════════════════════════════════════════════════

🚀 RECOMMENDED LEARNING PATH:
══════════════════════════════

WEEK 1 (Fundamentals):
├─ 136_SingleNumber.py          ← Start here! Simple XOR
├─ 217_ContainsDuplicate.py     ← Hash basics
├─ 268_MissingNumber.py         ← Math patterns
└─ 283_MoveZeroes.py            ← Two pointers intro

WEEK 2 (Two Pointers):
├─ 189_RotateArray.py           ← Rotation technique
├─ 75_SortColors.py             ← Three pointers
└─ 56_MergeIntervals.py         ← Sorting + logic

WEEK 3 (Advanced):
├─ 152_MaxProduct.py            ← DP thinking
├─ 238_ProductExceptSelf.py     ← Multi-pass technique
├─ 169_MajorityElement.py       ← Voting algorithm
└─ 41_FirstMissingPositive.py   ← Hard problem

WEEK 4 (Matrix):
└─ 48_RotateImage.py            ← 2D arrays


═══════════════════════════════════════════════════════════════════════════════════

💡 KEY PATTERNS IN THIS FOLDER:
════════════════════════════════

BIT MANIPULATION (Saves space!)
└─ #136 - XOR for finding unpaired element

HASH STRUCTURES (Fast lookups!)
└─ #217 - Set for duplicate detection

TWO/THREE POINTERS (In-place!)
├─ #283 - Move zeroes to end
├─ #189 - Rotate array
└─ #75 - Sort three colors

DYNAMIC PROGRAMMING (Track state!)
├─ #152 - Max product subarray
└─ #238 - Product except self

MATHEMATICAL (Clever formulas!)
└─ #268 - Missing number sum

SORTING + GREEDY (Problem simplification!)
└─ #56 - Merge intervals

VOTING (Elegant algorithms!)
└─ #169 - Majority element

IN-PLACE HASHING (Space optimization!)
└─ #41 - First missing positive

MATRIX (2D manipulation!)
└─ #48 - Rotate image


═══════════════════════════════════════════════════════════════════════════════════

🎓 WHAT TO FOCUS ON:
════════════════════

FOR EACH PROBLEM, UNDERSTAND:

1. WHY the brute force is slow
2. WHAT pattern solves it optimally  
3. HOW the pattern works mathematically
4. WHEN to use this pattern in other problems
5. EDGE CASES that might break your solution

AMAZON INTERVIEWER CARES ABOUT:

✓ Can you explain the SITUATION and TASK clearly?
✓ Is your ACTION algorithmically sound?
✓ Did you get the RESULT you claimed?
✓ Can you optimize space? (Amazon scale!)
✓ Did you handle edge cases?
✓ Could you solve similar problems?


═══════════════════════════════════════════════════════════════════════════════════

📚 ADDITIONAL RESOURCES:
═════════════════════════

See: AMAZON_INTERVIEW_PREP.txt for:
✓ Detailed study guide
✓ STAR methodology explained
✓ Interview tips
✓ Quick reference table
✓ Pattern cheat sheet


═══════════════════════════════════════════════════════════════════════════════════

🎯 YOUR INTERVIEW STRATEGY:
════════════════════════════

BEFORE INTERVIEW:
✓ Practice each problem 2-3 times
✓ Time yourself: can you solve in 20 mins?
✓ Explain it out loud to practice communication
✓ Know all complexity trade-offs

DURING INTERVIEW:
✓ Listen carefully to the problem
✓ Explain your approach BEFORE coding
✓ Use STAR format: Situation → Task → Action → Result
✓ Code step-by-step with comments
✓ Test with examples including edge cases
✓ Discuss time/space trade-offs

AFTER CODING:
✓ "Let me trace through this with [example]"
✓ "The time complexity is O(n) because..."
✓ "Edge cases I considered: empty, single element, all zeros..."
✓ "If we had different constraints, I could also..."


═══════════════════════════════════════════════════════════════════════════════════

Good luck! 🚀

Remember: At Amazon, they're not just testing code - 
they're testing if you can think clearly under pressure,
communicate effectively, and solve problems at scale.

These problems teach you HOW to think, not just WHAT to code.

You've got this! 💪

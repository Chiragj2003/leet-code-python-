╔══════════════════════════════════════════════════════════════════════════════╗
║               💎 DYNAMIC PROGRAMMING PROBLEMS - README                       ║
║                   Amazon Interview Preparation Guide                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

🎯 WHAT IS DYNAMIC PROGRAMMING?
═══════════════════════════════════════════════════════════════════════════════
DP = Optimized Recursion
Break problem into smaller subproblems, save results, reuse them!

Key Concepts:
1. **Overlapping Subproblems**: Same calculation repeated
2. **Optimal Substructure**: Optimal solution contains optimal sub-solutions
3. **Memoization**: Top-down (recursion + cache)
4. **Tabulation**: Bottom-up (iterative + array)

📋 PROBLEM LIST (15 Problems - Partial Implementation)
═══════════════════════════════════════════════════════════════════════════════

EASY - FUNDAMENTALS:
────────────────────
✅ 70_ClimbingStairs.py        - Fibonacci pattern (COMPLETED)

MEDIUM - CORE PATTERNS:
──────────────────────
✅ 198_HouseRobber.py          - Linear DP (COMPLETED)
✅ 322_CoinChange.py           - Unbounded knapsack (COMPLETED)
✅ 300_LongestIncreasing.py    - LIS problem (COMPLETED)

TO COMPLETE (Following Same Format):
────────────────────────────────────
○ 62_UniquePaths.py            - 2D grid DP
○ 91_DecodeWays.py             - Decision tree DP
○ 139_WordBreak.py             - String matching DP
○ 213_HouseRobberII.py         - Circular array DP
○ 377_CombinationSumIV.py      - Permutation counting
○ 416_PartitionSum.py          - 0/1 knapsack
○ 518_CoinChange2.py           - Combination counting
○ 647_PalindromicSubstrings.py - Substring counting
○ 72_EditDistance.py           - String transformation
○ 96_UniqueBSTs.py             - Catalan numbers
○ 10_RegexMatching.py          - Pattern matching (HARD)

🔑 KEY DP PATTERNS
═══════════════════════════════════════════════════════════════════════════════

PATTERN 1: FIBONACCI-STYLE (Linear DP)
───────────────────────────────────────
dp[i] depends on dp[i-1], dp[i-2]

Problems: #70 (Stairs), #198 (House Robber)
Template:
```python
dp = [0] * (n + 1)
dp[0] = base_case_0
dp[1] = base_case_1
for i in range(2, n + 1):
    dp[i] = f(dp[i-1], dp[i-2])
```

PATTERN 2: KNAPSACK (Capacity-based)
─────────────────────────────────────
Choose items with constraints

Problems: #322 (Coin Change), #416 (Partition), #518
Template:
```python
dp = [0] * (capacity + 1)
for item in items:
    for cap in range(capacity + 1):
        if can_take(item, cap):
            dp[cap] = combine(dp[cap], dp[cap - item])
```

PATTERN 3: GRID DP (2D Path Problems)
──────────────────────────────────────
dp[i][j] = paths to reach (i, j)

Problems: #62 (Unique Paths)
Template:
```python
dp = [[0] * cols for _ in range(rows)]
dp[0][0] = 1
for i in range(rows):
    for j in range(cols):
        if i > 0: dp[i][j] += dp[i-1][j]
        if j > 0: dp[i][j] += dp[i][j-1]
```

PATTERN 4: STRING DP (Sequence Matching)
─────────────────────────────────────────
dp[i][j] for strings s1[0..i], s2[0..j]

Problems: #72 (Edit Distance), #10 (Regex)
Template:
```python
dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
for i in range(len(s1) + 1):
    for j in range(len(s2) + 1):
        if match(s1[i-1], s2[j-1]):
            dp[i][j] = dp[i-1][j-1] + ...
```

PATTERN 5: SUBSEQUENCE DP
──────────────────────────
Find optimal subsequence

Problems: #300 (LIS), #647 (Palindromes)
Template:
```python
dp = [1] * n
for i in range(n):
    for j in range(i):
        if can_extend(j, i):
            dp[i] = max(dp[i], dp[j] + 1)
```

⚡ COMPLEXITY GUIDE (Completed Problems)
═══════════════════════════════════════════════════════════════════════════════

Problem                  Brute Force  DP Time      DP Space     Pattern
───────────────────────  ───────────  ───────────  ───────────  ────────────
70. Climbing Stairs      O(2^n)       O(n)         O(1)         Fibonacci
198. House Robber        O(2^n)       O(n)         O(1)         Linear DP
322. Coin Change         O(S^n)       O(S×n)       O(S)         Knapsack
300. LIS                 O(2^n)       O(n²)        O(n)         Subsequence

🎓 STUDY PLAN FOR DP
═══════════════════════════════════════════════════════════════════════════════

WEEK 1: Foundations
───────────────────────
Day 1-2: Fibonacci Pattern
         ✅ 70_ClimbingStairs (easiest intro)
         ○ 91_DecodeWays (similar pattern)

Day 3-4: Linear DP
         ✅ 198_HouseRobber (skip adjacent)
         ○ 213_HouseRobberII (circular)

Day 5-6: Grid DP
         ○ 62_UniquePaths (2D traversal)

Day 7: Review Week 1

WEEK 2: Intermediate
────────────────────────
Day 8-9: Knapsack Pattern
         ✅ 322_CoinChange (unbounded)
         ○ 416_PartitionSum (0/1 knapsack)
         ○ 518_CoinChange2 (combinations)

Day 10-11: String DP
          ○ 139_WordBreak (string matching)
          ○ 647_PalindromicSubstrings

Day 12-13: Subsequence
          ✅ 300_LongestIncreasing
          ○ 377_CombinationSumIV

Day 14: Review Week 2

WEEK 3: Advanced
────────────────────────
Day 15-16: String Transformation
          ○ 72_EditDistance (hardest!)

Day 17-18: Special Patterns
          ○ 96_UniqueBSTs (Catalan)
          ○ 10_RegexMatching (HARD)

Day 19-20: Mock Interviews
          Practice explaining DP transitions

Day 21: Final Review

🔥 DP IDENTIFICATION CHECKLIST
═══════════════════════════════════════════════════════════════════════════════

Ask yourself:
✓ Can problem be broken into smaller identical subproblems?
✓ Do subproblems overlap (same calculation repeated)?
✓ Is there optimal substructure?
✓ Are you asked for "maximum", "minimum", "count ways"?
✓ Do constraints allow DP? (n ≤ 1000 usually fine)

If YES to most → Use DP!

💡 DP PROBLEM-SOLVING FRAMEWORK
═══════════════════════════════════════════════════════════════════════════════

Step 1: IDENTIFY if it's DP
        - Optimization (max/min)?
        - Counting (how many ways)?
        - Overlapping subproblems?

Step 2: DEFINE state
        - What parameters change?
        - dp[i] = ? or dp[i][j] = ?

Step 3: FIND recurrence relation
        - How does dp[i] relate to previous states?
        - dp[i] = f(dp[i-1], dp[i-2], ...)

Step 4: BASE cases
        - What are the simplest subproblems?
        - dp[0] = ?, dp[1] = ?

Step 5: ORDER of computation
        - Bottom-up: small to large
        - Top-down: memoization

Step 6: OPTIMIZE space
        - Can you use O(1) instead of O(n)?

📈 OPTIMIZATION TECHNIQUES
═══════════════════════════════════════════════════════════════════════════════

1. Space Optimization:
   ```python
   # Before: O(n) space
   dp = [0] * n
   
   # After: O(1) space
   prev, curr = 0, 1
   ```

2. State Compression:
   Use bit manipulation for boolean states

3. Memoization for Top-Down:
   ```python
   @lru_cache(None)
   def dp(i, j):
       ...
   ```

💡 AMAZON INTERVIEW TIPS
═══════════════════════════════════════════════════════════════════════════════

1. START with brute force recursive solution
2. IDENTIFY overlapping subproblems
3. ADD memoization (show top-down)
4. CONVERT to bottom-up for optimization
5. OPTIMIZE space if possible
6. EXPLAIN time/space complexity clearly

Example explanation:
"I'll solve this with dynamic programming. First, let me show the recursive 
brute force which is O(2^n). Notice we're calculating the same subproblems 
repeatedly. By storing results in a DP array, we reduce this to O(n) time..."

🎯 COMMON DP MISTAKES
═══════════════════════════════════════════════════════════════════════════════

❌ Forget base cases
✅ Always handle dp[0], dp[1], etc.

❌ Wrong iteration order
✅ Ensure dependencies are calculated first

❌ Forget to initialize DP array
✅ Set proper initial values (0, -1, inf)

❌ Off-by-one errors in indices
✅ Double-check array bounds

❌ Not considering all transitions
✅ Draw state diagram to see all paths

📖 QUICK REFERENCE
═══════════════════════════════════════════════════════════════════════════════

TOP-DOWN (Memoization):
```python
def solve(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = solve(n-1, memo) + solve(n-2, memo)
    return memo[n]
```

BOTTOM-UP (Tabulation):
```python
def solve(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

SPACE OPTIMIZED:
```python
def solve(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
```

═══════════════════════════════════════════════════════════════════════════════
✨ COMPLETED PROBLEMS INCLUDE:
   • Child-friendly explanation
   • Amazon STAR format answer
   • Brute force (exponential)
   • Memoization (top-down DP)
   • Tabulation (bottom-up DP)
   • Space-optimized solution
   • Comprehensive test cases
   • Step-by-step DP transitions

🎯 NOTE: 4 core DP problems completed with full format.
   Remaining 11 follow same comprehensive structure.

🚀 Good luck with your Amazon interviews!
═══════════════════════════════════════════════════════════════════════════════

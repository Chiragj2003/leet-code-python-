╔══════════════════════════════════════════════════════════════════════════════╗
║                   📚 BACKTRACKING PROBLEMS - README                          ║
║                   Amazon Interview Preparation Guide                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

🎯 WHAT IS BACKTRACKING?
═══════════════════════════════════════════════════════════════════════════════
Backtracking is like exploring all paths in a maze:
- Try a path (make a choice)
- If it works, continue exploring
- If it fails, go back (backtrack) and try another path

Think of it as: TRY → EXPLORE → UNDO (if fail) → REPEAT

📋 PROBLEM LIST (6 Problems)
═══════════════════════════════════════════════════════════════════════════════

EASY/FOUNDATIONAL:
------------------
None (all Medium)

MEDIUM - CORE PATTERNS:
----------------------
1. ✅ 17_PhoneLetters.py         - Phone number letter combinations
2. ✅ 22_GenerateParentheses.py  - Generate valid parentheses  
3. ✅ 39_CombinationSum.py       - Find sum combinations (reusable)
4. ✅ 46_Permutations.py         - All permutations of array
5. ✅ 78_Subsets.py              - Power set (all subsets)
6. ✅ 79_WordSearch.py           - Search word in 2D grid

🔑 KEY PATTERNS
═══════════════════════════════════════════════════════════════════════════════

PATTERN 1: COMBINATIONS (Order doesn't matter)
───────────────────────────────────────────────
Problems: #78 (Subsets), #39 (Combination Sum)
Template:
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i, path)  # or i+1 if no reuse
            path.pop()

PATTERN 2: PERMUTATIONS (Order matters)
───────────────────────────────────────
Problems: #46 (Permutations)
Template:
    def backtrack(path, used):
        if len(path) == n:
            result.append(path[:])
        for i in range(len(nums)):
            if used[i]: continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False

PATTERN 3: DECISION TREE (Valid choices)
────────────────────────────────────────
Problems: #17 (Phone), #22 (Parentheses)
Template:
    def backtrack(path, state):
        if is_complete(state):
            result.append(path)
        for choice in get_choices(state):
            backtrack(path + choice, new_state)

PATTERN 4: GRID DFS (2D exploration)
────────────────────────────────────
Problems: #79 (Word Search)
Template:
    def dfs(r, c, index):
        if index == len(target):
            return True
        # Mark visited
        temp = grid[r][c]
        grid[r][c] = '#'
        # Explore 4 directions
        found = dfs(r+1,c) or dfs(r-1,c) or ...
        # Backtrack
        grid[r][c] = temp
        return found

⚡ COMPLEXITY GUIDE
═══════════════════════════════════════════════════════════════════════════════

Problem                  Time                Space       Pattern
───────────────────────  ──────────────────  ──────────  ────────────────
17. Phone Letters        O(4^n × n)          O(n)        Decision tree
22. Parentheses          O(4^n / √n)         O(n)        Valid choices
39. Combination Sum      O(2^target)         O(target)   Combinations
46. Permutations         O(n! × n)           O(n)        Permutations
78. Subsets              O(2^n × n)          O(n)        Combinations
79. Word Search          O(m×n × 4^L)        O(L)        Grid DFS

🎓 STUDY PLAN
═══════════════════════════════════════════════════════════════════════════════

DAY 1: Foundations
─────────────────────
□ 78. Subsets (easiest backtracking concept)
□ 46. Permutations (understand used tracking)

DAY 2: Decision Trees
─────────────────────
□ 17. Phone Letters (simple decision tree)
□ 22. Generate Parentheses (constraint-based)

DAY 3: Advanced
───────────────
□ 39. Combination Sum (with reuse)
□ 79. Word Search (2D + backtracking)

🔥 COMMON MISTAKES TO AVOID
═══════════════════════════════════════════════════════════════════════════════

1. ❌ Forgetting to copy path: result.append(path)
   ✅ Always copy: result.append(path[:]) or result.append(list(path))

2. ❌ Not backtracking: path.append(x) ... (no pop)
   ✅ Always undo: path.append(x) → recurse → path.pop()

3. ❌ Mutating global state without restoring
   ✅ Save temp, restore after recursion

4. ❌ Wrong base case placement
   ✅ Check termination BEFORE exploring further

💡 AMAZON INTERVIEW TIPS
═══════════════════════════════════════════════════════════════════════════════

1. ALWAYS explain the "TRY → EXPLORE → UNDO" pattern
2. Draw the decision tree for interviewer
3. Discuss pruning opportunities (early termination)
4. Mention space complexity = recursion depth
5. Start with brute force, then optimize with pruning

Example explanation:
"We'll use backtracking to explore all possibilities. At each step, 
we try a choice, recursively explore that path, and if it doesn't work, 
we backtrack (undo) and try the next choice. This guarantees we explore 
all valid combinations without missing any."

📖 QUICK REFERENCE
═══════════════════════════════════════════════════════════════════════════════

When to use Backtracking?
✓ Generate ALL possible solutions
✓ Explore ALL combinations/permutations
✓ Find ALL paths in grid/graph
✓ Problem has constraints to satisfy
✓ Need to "try and undo" choices

Not suitable for:
✗ Finding optimal value (use DP)
✗ Counting only (might use DP)
✗ Single solution exists (might use greedy/BFS)

═══════════════════════════════════════════════════════════════════════════════
✨ ALL PROBLEMS HAVE:
   • Simple problem explanation (child-friendly)
   • Amazon STAR format answer
   • Complexity analysis
   • Multiple solution approaches
   • Comprehensive test cases
   • Step-by-step traces

🎯 Good luck with your Amazon interviews!
═══════════════════════════════════════════════════════════════════════════════

╔══════════════════════════════════════════════════════════════════════════════╗
║                   🔍 BINARY SEARCH PROBLEMS - README                         ║
║                   Amazon Interview Preparation Guide                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

🎯 WHAT IS BINARY SEARCH?
═══════════════════════════════════════════════════════════════════════════════
Binary Search is like finding a word in a dictionary:
- Open to middle page
- If word comes before, search left half
- If word comes after, search right half
- Repeat until found

Key: Works on SORTED data, O(log n) time!

📋 PROBLEM LIST (11 Problems)
═══════════════════════════════════════════════════════════════════════════════

EASY - FUNDAMENTALS:
-------------------
1. ✅ 69_Sqrt.py                 - Integer square root
2. ✅ 278_FirstBad.py            - First bad version
3. ✅ 349_IntersectionArrays.py  - Array intersection
4. ✅ 441_ArrangingCoins.py      - Staircase coins

MEDIUM - CORE PATTERNS:
----------------------
5. ✅ 33_SearchRotated.py        - Search in rotated array
6. ✅ 153_FindMin.py             - Find minimum in rotated array
7. ✅ 34_FindRange.py            - Find first & last position
8. ✅ 74_Search2D.py             - Search 2D matrix
9. ✅ 475_Heaters.py             - Heater radius problem
10. ✅ 658_ClosestElements.py    - K closest elements
11. ✅ 911_OnlineElection.py     - Time-based queries

🔑 KEY PATTERNS
═══════════════════════════════════════════════════════════════════════════════

PATTERN 1: CLASSIC BINARY SEARCH (Exact match)
───────────────────────────────────────────────
Problems: #33, #74
Template:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

PATTERN 2: FIND BOUNDARY (First/Last occurrence)
─────────────────────────────────────────────────
Problems: #34, #278
Template:
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            # For first: right = mid - 1
            # For last: left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

PATTERN 3: SEARCH ON ANSWER SPACE
──────────────────────────────────
Problems: #69 (sqrt), #441 (coins)
Template:
    left, right = 0, max_possible
    while left <= right:
        mid = (left + right) // 2
        if is_valid(mid):
            left = mid + 1  # Try larger
        else:
            right = mid - 1
    return right

PATTERN 4: ROTATED ARRAY
────────────────────────
Problems: #33, #153
Key: One half is always sorted!
Template:
    if nums[left] <= nums[mid]:
        # Left half sorted
        if nums[left] <= target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        # Right half sorted
        ...

PATTERN 5: 2D MATRIX AS 1D
──────────────────────────
Problems: #74
Template:
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    while left <= right:
        mid = (left + right) // 2
        row = mid // cols
        col = mid % cols
        val = matrix[row][col]
        ...

PATTERN 6: CLOSEST ELEMENT
──────────────────────────
Problems: #658, #475, #349
Template:
    # Find position
    while left < right:
        mid = (left + right) // 2
        if should_go_right(mid):
            left = mid + 1
        else:
            right = mid

⚡ COMPLEXITY GUIDE
═══════════════════════════════════════════════════════════════════════════════

Problem                  Time                Space       Pattern
───────────────────────  ──────────────────  ──────────  ────────────────
69. Sqrt                 O(log x)            O(1)        Answer space
278. First Bad           O(log n)            O(1)        Find boundary
349. Intersection        O(n + m)            O(min(n,m)) Hash set (best)
441. Arranging Coins     O(log n)            O(1)        Answer space
33. Search Rotated       O(log n)            O(1)        Modified binary
153. Find Min            O(log n)            O(1)        Rotated array
34. Find Range           O(log n)            O(1)        Two boundaries
74. Search 2D            O(log(m×n))         O(1)        2D as 1D
475. Heaters             O((n+m) log m)      O(1)        Closest element
658. K Closest           O(log(n-k) + k)     O(1)        Window search
911. Online Election     O(log n) per query  O(n)        Preprocessing

🎓 STUDY PLAN
═══════════════════════════════════════════════════════════════════════════════

DAY 1: Fundamentals
──────────────────────
□ 69. Sqrt (simple binary search)
□ 278. First Bad Version (boundary finding)
□ 441. Arranging Coins (answer space search)

DAY 2: Core Patterns
───────────────────────
□ 34. Find Range (two boundaries)
□ 74. Search 2D (coordinate mapping)
□ 349. Intersection (multiple approaches)

DAY 3: Rotated Arrays
─────────────────────────
□ 33. Search Rotated (modified search)
□ 153. Find Min (find pivot)

DAY 4: Advanced
───────────────
□ 658. K Closest (window optimization)
□ 475. Heaters (closest element)
□ 911. Online Election (preprocessing + queries)

🔥 COMMON MISTAKES TO AVOID
═══════════════════════════════════════════════════════════════════════════════

1. ❌ Integer overflow: mid = (left + right) / 2
   ✅ Use: mid = left + (right - left) // 2

2. ❌ Infinite loop: while left < right with left = mid
   ✅ Use: left = mid + 1 or mid = (left + right + 1) // 2

3. ❌ Off-by-one errors in boundaries
   ✅ Test with: [1], [1,2], [1,2,3]

4. ❌ Using <= when should use <
   ✅ Use left <= right for exact search
   ✅ Use left < right for boundary search

5. ❌ Not handling duplicates
   ✅ Continue searching even after finding target (for boundaries)

💡 AMAZON INTERVIEW TIPS
═══════════════════════════════════════════════════════════════════════════════

1. ALWAYS mention O(log n) time complexity
2. Explain "halving the search space each iteration"
3. Draw the search space on paper
4. Discuss edge cases: empty array, single element
5. For rotated arrays, explain "one half always sorted"

Example explanation:
"I'll use binary search to achieve O(log n) time. The idea is to compare 
the middle element with our target and eliminate half the search space 
each iteration. For a rotated array, we first identify which half is sorted, 
then check if our target lies in that sorted range."

🎯 WHEN TO USE BINARY SEARCH
═══════════════════════════════════════════════════════════════════════════════

Strong Indicators:
✓ Array is sorted (or rotated sorted)
✓ Need to find target in O(log n)
✓ Problem asks for "minimum X such that..."
✓ Search space has monotonic property
✓ Time-based queries on sorted timestamps

Red Flags (Don't use):
✗ Unsorted data (unless you can sort first)
✗ Need to examine all elements
✗ Looking for ALL occurrences (might still use, but modified)

📊 BRUTE FORCE VS BINARY SEARCH
═══════════════════════════════════════════════════════════════════════════════

Problem             Brute Force    Binary Search    Improvement
─────────────────   ────────────   ─────────────    ───────────
Search sorted       O(n)           O(log n)         Exponential!
Find min rotated    O(n)           O(log n)         Exponential!
Sqrt(x)             O(√x)          O(log x)         Huge!
First bad version   O(n)           O(log n)         Exponential!

For n = 1,000,000:
- Brute: 1,000,000 operations
- Binary: ~20 operations
- Speedup: 50,000x faster!

📖 QUICK REFERENCE
═══════════════════════════════════════════════════════════════════════════════

Binary Search Template (Most Common):
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found
```

Finding Left Boundary:
```python
while left < right:
    mid = (left + right) // 2
    if arr[mid] < target:
        left = mid + 1
    else:
        right = mid
return left
```

Finding Right Boundary:
```python
while left < right:
    mid = (left + right + 1) // 2  # Bias right
    if arr[mid] > target:
        right = mid - 1
    else:
        left = mid
return right
```

═══════════════════════════════════════════════════════════════════════════════
✨ ALL PROBLEMS HAVE:
   • Child-friendly explanation with analogies
   • Amazon STAR format answer
   • Brute force solution for comparison
   • Optimal binary search solution
   • Detailed complexity analysis
   • Comprehensive test cases
   • Step-by-step execution traces

🎯 Good luck with your Amazon interviews!
═══════════════════════════════════════════════════════════════════════════════

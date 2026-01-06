"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #56 - Merge Intervals                             ║
║                    Topic: Array / Sorting                                    ║
║                    Difficulty: Medium                                         ║
║                    Company: Amazon, Google, Facebook                         ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Merge all overlapping intervals into single intervals.

EXAMPLES:
─────────
✓ Input:  [[1,3],[2,6],[8,10],[15,18]]
  Output: [[1,6],[8,10],[15,18]]
  (Reason: [1,3] and [2,6] overlap → merge to [1,6])

✓ Input:  [[1,4],[4,5]]
  Output: [[1,5]]

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
📅 You have meeting times: 1-3pm, 2-6pm, 8-10am, 3-5pm.
   Some meetings overlap! Merge overlapping meetings.
   1-3 and 2-6 overlap → one meeting 1-6pm.

🎪 Activities at summer camp: some activities overlap in time.
   Merge overlapping activities into one time block.

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   Amazon calendar has customer meeting times but many overlap.
   We need to merge overlapping slots into single blocks
   to show true availability.

📌 TASK:
   Merge all overlapping intervals.
   Time O(n log n), Space O(n).

📌 ACTION:
   1. Sort intervals by start time
   2. Scan through and merge overlapping
   
   ✓ Algorithm:
     1. Sort by start time
     2. For each interval:
        - If overlaps with last merged, extend it
        - If not, add as new interval

📌 RESULT:
   ✓ Time Complexity: O(n log n) for sorting
   ✓ Space Complexity: O(n) for result
   ✓ Merges calendar slots instantly

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⏰ COMPLEXITY ANALYSIS                                    ║
╚══════════════════════════════════════════════════════════════════════════════╝

BRUTE FORCE (Check All Pairs):
    Time: O(n²) - compare all pairs
    Space: O(n)

SORT + MERGE (OPTIMAL):
    Time: O(n log n) - sorting dominates
    Space: O(n)

"""

# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Sort + Merge
# ═══════════════════════════════════════════════════════════════════════════
def merge(intervals):
    """
    Sort and Merge - OPTIMAL!
    
    🔑 KEY INSIGHT:
    ───────────────
    Sort by start time, then scan left to right.
    Overlapping intervals will be adjacent after sorting.
    
    Example: [[1,3],[2,6],[8,10],[15,18]]
    ───────
    
    After sorting by start: [[1,3],[2,6],[8,10],[15,18]] (already sorted)
    
    Start with [1,3]
    
    Check [2,6]: Does 2 <= 3? YES, overlaps!
      Merge: [1, max(3,6)] = [1,6]
    
    Check [8,10]: Does 8 <= 6? NO, no overlap
      Add [8,10] separately
    
    Check [15,18]: Does 15 <= 10? NO, no overlap
      Add [15,18] separately
    
    Result: [[1,6],[8,10],[15,18]] ✓
    """
    if not intervals:
        return []
    
    # Step 1: Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    # Step 2: Merge overlapping
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        # Check if current overlaps with last merged interval
        if current[0] <= last[1]:
            # Overlaps: merge by extending end
            last[1] = max(last[1], current[1])
        else:
            # No overlap: add as new interval
            merged.append(current)
    
    return merged


# ═══════════════════════════════════════════════════════════════════════════
# 🐢 BRUTE FORCE - Check all pairs
# ═══════════════════════════════════════════════════════════════════════════
def merge_bruteforce(intervals):
    """
    Time: O(n²)
    Space: O(n)
    """
    if not intervals:
        return []
    
    intervals_list = [list(x) for x in intervals]
    merged = True
    
    while merged:
        merged = False
        for i in range(len(intervals_list) - 1):
            # Check if intervals[i] and intervals[i+1] overlap
            if intervals_list[i][1] >= intervals_list[i+1][0]:
                # Merge them
                intervals_list[i][1] = max(intervals_list[i][1], 
                                           intervals_list[i+1][1])
                intervals_list.pop(i + 1)
                merged = True
                break
    
    return intervals_list


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]], [[1,5]]),
        ([[1,4],[2,3]], [[1,4]]),
        ([[0,0]], [[0,0]]),
    ]
    
    print("=" * 70)
    print("🧪 TESTING MERGE INTERVALS SOLUTIONS")
    print("=" * 70)
    
    for intervals, expected in test_cases:
        result_optimal = merge([list(x) for x in intervals])
        result_brute = merge_bruteforce([list(x) for x in intervals])
        
        status = "✓" if result_optimal == expected else "✗"
        
        print(f"\n{status} Input:    {intervals}")
        print(f"  Expected: {expected}")
        print(f"  Optimal:  {result_optimal}")
        print(f"  Brute:    {result_brute}")
    
    print("\n" + "=" * 70)
    print("📊 COMPLEXITY COMPARISON")
    print("=" * 70)
    print("| Method      | Time      | Space   | Amazon |")
    print("|-------------|-----------|---------|--------|")
    print("| Brute Force | O(n²)     | O(n)    | ❌     |")
    print("| Sort+Merge  | O(n log n)| O(n)    | ✅     |")

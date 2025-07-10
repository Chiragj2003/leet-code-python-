"""
LeetCode #56 - Merge Intervals
Topic: Array / Sorting
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Merge all overlapping intervals.

Example:
[[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]
Explanation: [1,3] and [2,6] overlap, merge into [1,6]

Think of it like:
Merging meeting times that overlap into single blocks!

WHY THIS WORKS (Simple Explanation):
1. Sort intervals by start time
2. Go through sorted list:
   - If current overlaps with previous, merge them
   - If no overlap, add current as separate interval

Like organizing events on a calendar!

Time Complexity: O(n log n) for sorting
Space Complexity: O(n) for result
"""

def merge(intervals):
    """
    Merge overlapping intervals
    
    Visual example: [[1,3],[2,6],[8,10],[15,18]]
    
    After sorting: [[1,3],[2,6],[8,10],[15,18]]
    
    Start with [1,3]
    
    Check [2,6]: 2 <= 3, overlaps!
      Merge: [1, max(3,6)] = [1,6]
    
    Check [8,10]: 8 > 6, no overlap
      Add [8,10] separately
    
    Check [15,18]: 15 > 10, no overlap
      Add [15,18] separately
    
    Result: [[1,6],[8,10],[15,18]]
    """
    if not intervals:
        return []
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        # Check if current overlaps with last merged interval
        if current[0] <= last[1]:
            # Merge: extend the end of last interval
            last[1] = max(last[1], current[1])
        else:
            # No overlap, add as new interval
            merged.append(current)
    
    return merged


def merge_verbose(intervals):
    """Detailed version showing merge process"""
    if not intervals:
        return []
    
    print(f"Input intervals: {intervals}\n")
    
    # Sort
    intervals.sort(key=lambda x: x[0])
    print(f"After sorting: {intervals}\n")
    
    merged = [intervals[0]]
    print(f"Start with: {merged[0]}\n")
    
    for i, current in enumerate(intervals[1:], 1):
        last = merged[-1]
        
        print(f"Step {i}: Check {current}")
        print(f"  Last merged: {last}")
        
        if current[0] <= last[1]:
            # Overlaps
            print(f"  {current[0]} <= {last[1]}, OVERLAPS!")
            old_end = last[1]
            last[1] = max(last[1], current[1])
            print(f"  Merge: [{last[0]}, {old_end}] + {current} = [{last[0]}, {last[1]}]")
        else:
            # No overlap
            print(f"  {current[0]} > {last[1]}, NO OVERLAP")
            print(f"  Add {current} as separate interval")
            merged.append(current)
        
        print(f"  Current merged: {merged}")
        print()
    
    print(f"Final result: {merged}")
    return merged


# Test cases
if __name__ == "__main__":
    test_cases = [
        (
            [[1,3],[2,6],[8,10],[15,18]],
            [[1,6],[8,10],[15,18]]
        ),
        (
            [[1,4],[4,5]],
            [[1,5]]
        ),
        (
            [[1,4],[0,4]],
            [[0,4]]
        ),
        (
            [[1,4],[2,3]],
            [[1,4]]
        ),
    ]
    
    print("=== Testing Merge Intervals ===\n")
    
    for intervals, expected in test_cases:
        result = merge([list(x) for x in intervals])  # Copy to avoid mutation
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {intervals}")
        print(f"   Output: {result}")
        print(f"   Expected: {expected}")
        print()
    
    print("="*50)
    print("=== Verbose Example ===")
    print("="*50 + "\n")
    
    merge_verbose([[1,3],[2,6],[8,10],[15,18]])

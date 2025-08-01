"""
LeetCode #435 - Non-overlapping Intervals
Topic: Greedy / Intervals
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Remove minimum intervals to make rest non-overlapping.

Example:
[[1,2],[2,3],[3,4],[1,3]] -> 1 (remove [1,3])

Think of it like:
Scheduling maximum meetings without conflicts!

WHY THIS WORKS:
Sort by end time, greedily pick non-overlapping.

Time: O(n log n)
Space: O(1)
"""

def eraseOverlapIntervals(intervals):
    """Minimum intervals to remove"""
    if not intervals:
        return 0
    
    # Sort by end time
    intervals.sort(key=lambda x: x[1])
    
    end = intervals[0][1]
    count = 0
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            # Overlapping, remove this interval
            count += 1
        else:
            # Non-overlapping, update end
            end = intervals[i][1]
    
    return count


# Test
if __name__ == "__main__":
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    result = eraseOverlapIntervals(intervals)
    print(f"Remove {result} intervals")

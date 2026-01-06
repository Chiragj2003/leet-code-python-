"""LeetCode #435 - Non-overlapping Intervals | Greedy | Medium"""

def eraseOverlapIntervals(intervals):
    """ OPTIMAL - Greedy Sort by End: O(n log n) time, O(1) space"""
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            count += 1
        else:
            end = intervals[i][1]
    
    return count

def eraseOverlapIntervals_dp(intervals):
    """ SOLUTION 2 - DP: O(n) time, O(n) space"""
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[0])
    n = len(intervals)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if intervals[j][1] <= intervals[i][0]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return n - max(dp)

if __name__ == "__main__":
    tests = [([[1,2],[2,3],[3,4],[1,3]], 1), ([[1,2],[1,2],[1,2]], 2)]
    print("Testing Non-overlapping Intervals:")
    for intervals, exp in tests:
        r1, r2 = eraseOverlapIntervals(intervals[:]), eraseOverlapIntervals_dp(intervals[:])
        print(f"{intervals}: Greedy={r1} DP={r2} (exp={exp})")

"""

              LeetCode #539 - Minimum Time Difference                         
              Topic: String/Math | Difficulty: Medium                         
              Company: Amazon, Meta                                           


PROBLEM: Find minimum time difference between any two time points.

Example:
  ["23:59","00:00"]  1 (minute difference)
  ["00:00","04:00","22:00"]  120 (2 hours)
"""

#  SOLUTION 1: Convert to Minutes and Sort (OPTIMAL)
def findMinDifference(timePoints):
    """
    Convert to minutes, sort, find min gap
    Time: O(n log n), Space: O(n)
    
    Also check circular: last to first + 24h.
    """
    def to_minutes(time):
        h, m = map(int, time.split(':'))
        return h * 60 + m
    
    minutes = sorted(to_minutes(t) for t in timePoints)
    
    # Check adjacent pairs
    min_diff = float('inf')
    for i in range(1, len(minutes)):
        min_diff = min(min_diff, minutes[i] - minutes[i-1])
    
    # Check circular (last to first)
    min_diff = min(min_diff, 1440 - minutes[-1] + minutes[0])
    
    return min_diff


#  SOLUTION 2: Bucket Sort (OPTIMAL time)
def findMinDifference_bucket(timePoints):
    """
    Use bucket for each minute (0-1439)
    Time: O(n), Space: O(1) - 1440 buckets
    
    If duplicate time, diff is 0.
    """
    seen = [False] * 1440
    
    for time in timePoints:
        h, m = map(int, time.split(':'))
        minutes = h * 60 + m
        
        if seen[minutes]:  # Duplicate
            return 0
        seen[minutes] = True
    
    # Find min difference
    times = [i for i in range(1440) if seen[i]]
    
    min_diff = float('inf')
    for i in range(1, len(times)):
        min_diff = min(min_diff, times[i] - times[i-1])
    
    # Circular
    min_diff = min(min_diff, 1440 - times[-1] + times[0])
    
    return min_diff


if __name__ == "__main__":
    print("Testing Minimum Time Difference:\n")
    
    tests = [
        (["23:59","00:00"], 1),
        (["00:00","04:00","22:00"], 120),
        (["00:00","23:59","00:00"], 0)
    ]
    
    for times, expected in tests:
        r1 = findMinDifference(times)
        r2 = findMinDifference_bucket(times)
        
        print(f'{times}: Sort={r1} Bucket={r2} (exp={expected}) {"" if r1 == expected else ""}')

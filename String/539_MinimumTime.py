"""
LeetCode #539 - Minimum Time Difference
Topic: String
Difficulty: Medium

PROBLEM EXPLANATION:
Given a list of 24-hour clock time points in "HH:MM" format,
return the minimum minutes difference between any two time-points.

Example:
Input: timePoints = ["23:59","00:00"]
Output: 1

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0

APPROACH:
1. Convert all times to minutes since midnight
2. Sort the times
3. Find minimum difference between adjacent times
4. Also check difference between first and last (circular)

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def findMinDifference(timePoints):
    """
    Returns minimum minutes difference
    """
    # Convert to minutes
    minutes = []
    for time in timePoints:
        h, m = map(int, time.split(':'))
        minutes.append(h * 60 + m)
    
    # Sort times
    minutes.sort()
    
    # Find minimum difference
    min_diff = float('inf')
    
    # Check adjacent times
    for i in range(1, len(minutes)):
        min_diff = min(min_diff, minutes[i] - minutes[i-1])
    
    # Check circular difference (last to first through midnight)
    circular = 1440 - minutes[-1] + minutes[0]
    min_diff = min(min_diff, circular)
    
    return min_diff


# Test cases
if __name__ == "__main__":
    test1 = ["23:59", "00:00"]
    print(f"Test 1: {findMinDifference(test1)}")  # Expected: 1
    
    test2 = ["00:00", "23:59", "00:00"]
    print(f"Test 2: {findMinDifference(test2)}")  # Expected: 0
    
    test3 = ["05:31", "22:08", "00:35"]
    print(f"Test 3: {findMinDifference(test3)}")  # Expected: 147

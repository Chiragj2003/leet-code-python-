"""
LeetCode #253 - Meeting Rooms II
Topic: Heap / Intervals
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Minimum conference rooms needed for meetings.

Example:
[[0,30],[5,10],[15,20]] -> 2 rooms

Think of it like:
How many rooms needed at peak time?

WHY THIS WORKS:
Sort by start time, use min-heap for end times.
Heap size = rooms needed.

Time: O(n log n)
Space: O(n)
"""

import heapq

def minMeetingRooms(intervals):
    """Find minimum meeting rooms"""
    if not intervals:
        return 0
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    # Min-heap of end times
    heap = []
    
    for start, end in intervals:
        # If earliest meeting ended, reuse room
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        
        # Add current meeting's end time
        heapq.heappush(heap, end)
    
    return len(heap)


# Test
if __name__ == "__main__":
    intervals = [[0,30],[5,10],[15,20]]
    result = minMeetingRooms(intervals)
    print(f"Need {result} meeting rooms")

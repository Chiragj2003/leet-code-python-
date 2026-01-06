"""LeetCode #253 - Meeting Rooms II | Heap/Intervals | Medium"""

import heapq

def minMeetingRooms(intervals):
    """ OPTIMAL - Min-Heap: O(n logn) time, O(n) space"""
    if not intervals: return 0
    intervals.sort(key=lambda x: x[0])
    heap = []
    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
    return len(heap)

def minMeetingRooms_sweep(intervals):
    """ SOLUTION 2 - Sweep Line: O(n logn), O(n)"""
    if not intervals: return 0
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])
    rooms = max_rooms = s = e = 0
    while s < len(starts):
        if starts[s] < ends[e]:
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            s += 1
        else:
            rooms -= 1
            e += 1
    return max_rooms

def minMeetingRooms_events(intervals):
    """ SOLUTION 3 - Events: O(n logn), O(n)"""
    if not intervals: return 0
    events = [(start,1) for start,_ in intervals] + [(end,-1) for _,end in intervals]
    events.sort(key=lambda x: (x[0], x[1]))
    rooms = max_rooms = 0
    for _, delta in events:
        rooms += delta
        max_rooms = max(max_rooms, rooms)
    return max_rooms

if __name__ == "__main__":
    tests = [([[0,30],[5,10],[15,20]],2),([[0,5],[5,10]],1),([[7,10],[2,4]],1),([[1,5],[1,5],[1,5]],3)]
    print("Testing Meeting Rooms II:")
    for intervals, exp in tests:
        r1, r2, r3 = minMeetingRooms(intervals[:]), minMeetingRooms_sweep(intervals[:]), minMeetingRooms_events(intervals[:])
        print(f"{intervals} -> {exp}: Heap={r1} Sweep={r2} Events={r3}" if r1==exp and r2==exp and r3==exp else f"{intervals} -> {exp}: FAIL")

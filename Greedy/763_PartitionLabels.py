"""LeetCode #763 - Partition Labels | Greedy/String | Medium"""

def partitionLabels(s):
    """ OPTIMAL - Greedy with Last Index: O(n) time, O(1) space"""
    last = {c: i for i, c in enumerate(s)}
    result = []
    start = end = 0
    
    for i, c in enumerate(s):
        end = max(end, last[c])
        if i == end:
            result.append(end - start + 1)
            start = i + 1
    
    return result

def partitionLabels_intervals(s):
    """ SOLUTION 2 - Merge Intervals: O(n) time, O(n) space"""
    last = {}
    for i, c in enumerate(s):
        if c not in last:
            last[c] = [i, i]
        else:
            last[c][1] = i
    
    intervals = sorted(last.values())
    result = []
    start, end = intervals[0]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] <= end:
            end = max(end, intervals[i][1])
        else:
            result.append(end - start + 1)
            start, end = intervals[i]
    
    result.append(end - start + 1)
    return result

if __name__ == "__main__":
    tests = [("ababcbacadefegdehijhklij", [9,7,8]), ("eccbbbbdec", [10])]
    print("Testing Partition Labels:")
    for s, exp in tests:
        r1, r2 = partitionLabels(s), partitionLabels_intervals(s)
        print(f"{s}: Greedy={r1} Intervals={r2} (exp={exp})")

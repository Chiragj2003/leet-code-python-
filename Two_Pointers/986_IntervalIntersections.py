"""
LeetCode #986 - Interval List Intersections
Topic: Two Pointers
Difficulty: Medium

PROBLEM EXPLANATION:
Given two lists of closed intervals where each list is sorted and pairwise disjoint,
return the intersection of these two interval lists.

Example:
Input: 
firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

APPROACH (Two Pointers):
1. Use two pointers, one for each list
2. For each pair of intervals, check if they overlap
3. If they overlap, the intersection is [max(start1, start2), min(end1, end2)]
4. Move the pointer whose interval ends first
5. Continue until one list is exhausted

Time Complexity: O(m + n)
Space Complexity: O(1) excluding output
"""

def intervalIntersection(firstList, secondList):
    """
    Returns list of interval intersections
    """
    result = []
    i = 0  # pointer for firstList
    j = 0  # pointer for secondList
    
    while i < len(firstList) and j < len(secondList):
        # Get current intervals
        start1, end1 = firstList[i]
        start2, end2 = secondList[j]
        
        # Check if intervals overlap
        # They overlap if start of one is <= end of other
        overlap_start = max(start1, start2)
        overlap_end = min(end1, end2)
        
        if overlap_start <= overlap_end:
            # There is an intersection
            result.append([overlap_start, overlap_end])
        
        # Move pointer of interval that ends first
        if end1 < end2:
            i += 1
        else:
            j += 1
    
    return result


# Test cases
if __name__ == "__main__":
    test1_first = [[0, 2], [5, 10], [13, 23], [24, 25]]
    test1_second = [[1, 5], [8, 12], [15, 24], [25, 26]]
    print(f"Test 1: {intervalIntersection(test1_first, test1_second)}")
    # Expected: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    
    test2_first = [[1, 3], [5, 9]]
    test2_second = []
    print(f"Test 2: {intervalIntersection(test2_first, test2_second)}")
    # Expected: []
    
    test3_first = []
    test3_second = [[4, 8], [10, 12]]
    print(f"Test 3: {intervalIntersection(test3_first, test3_second)}")
    # Expected: []
    
    test4_first = [[1, 7]]
    test4_second = [[3, 10]]
    print(f"Test 4: {intervalIntersection(test4_first, test4_second)}")
    # Expected: [[3,7]]

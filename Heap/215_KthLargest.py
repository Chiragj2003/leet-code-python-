"""
LeetCode #215 - Kth Largest Element in an Array
Topic: Heap / Priority Queue
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Find the kth largest element in unsorted array.

Example:
[3,2,1,5,6,4], k=2 -> 5 (second largest)

Think of it like:
Finding the 2nd place winner in a race!

WHY THIS WORKS (Simple Explanation):
Use min-heap of size k:
- Keep k largest elements in heap
- Top of heap is kth largest!

Time: O(n log k)
Space: O(k)
"""

import heapq

def findKthLargest(nums, k):
    """Find kth largest element"""
    # Min-heap of size k
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        
        # Keep only k largest
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]  # Top is kth largest


# Test
if __name__ == "__main__":
    tests = [
        ([3,2,1,5,6,4], 2, 5),
        ([3,2,3,1,2,4,5,5,6], 4, 4),
    ]
    
    for nums, k, exp in tests:
        result = findKthLargest(nums, k)
        print(f"{nums}, k={k} -> {result} (expected {exp})")

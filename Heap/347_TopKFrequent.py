"""
LeetCode #347 - Top K Frequent Elements
Topic: Heap / Hashmap
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Find k most frequent elements in array.

Example:
[1,1,1,2,2,3], k=2 -> [1,2]

Think of it like:
Finding top k most popular items!

WHY THIS WORKS (Simple Explanation):
1. Count frequencies
2. Use heap to get top k

Time: O(n log k)
Space: O(n)
"""

import heapq
from collections import Counter

def topKFrequent(nums, k):
    """Find k most frequent elements"""
    # Count frequencies
    count = Counter(nums)
    
    # Use heap to get top k
    return heapq.nlargest(k, count.keys(), key=count.get)


# Test
if __name__ == "__main__":
    tests = [
        ([1,1,1,2,2,3], 2, [1,2]),
        ([1], 1, [1]),
    ]
    
    for nums, k, exp in tests:
        result = topKFrequent(nums, k)
        print(f"{nums}, k={k} -> {result} (expected {exp})")

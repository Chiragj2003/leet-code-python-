"""LeetCode #347 - Top K Frequent Elements | Heap/Hashmap | Medium"""

import heapq
from collections import Counter

def topKFrequent(nums, k):
    """ OPTIMAL - Min-Heap k: O(n log k) time, O(n) space"""
    if not nums: return []
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

def topKFrequent_heap(nums, k):
    """ SOLUTION 2 - Manual Heap: O(n log k)"""
    if not nums: return []
    count = Counter(nums)
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [x[1] for x in heap]

def topKFrequent_bucket(nums, k):
    """ SOLUTION 3 - Bucket Sort: O(n) - faster than heap!"""
    if not nums: return []
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums)+1)]
    for num, freq in count.items():
        buckets[freq].append(num)
    result = []
    for i in range(len(buckets)-1, -1, -1):
        result.extend(buckets[i])
        if len(result) == k: break
    return result

def topKFrequent_sorted(nums, k):
    """ SOLUTION 4 - Sort by Frequency: O(n log n)"""
    if not nums: return []
    count = Counter(nums)
    return sorted(count.keys(), key=lambda x: -count[x])[:k]

if __name__ == "__main__":
    tests = [([1,1,1,2,2,3], 2), ([1], 1)]
    print("Testing Top K Frequent:")
    for nums, k in tests:
        r1 = topKFrequent(nums, k)
        r2 = topKFrequent_heap(nums, k)
        r3 = topKFrequent_bucket(nums, k)
        r4 = topKFrequent_sorted(nums, k)
        print(f"{nums}, k={k}: nlargest={sorted(r1)} heap={sorted(r2)} bucket={sorted(r3)} sorted={sorted(r4)}")

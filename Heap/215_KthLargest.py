"""
LeetCode #215 - Kth Largest Element in Array | ENHANCED SOLUTION
Topic: Heap / Priority Queue | Difficulty: Medium

PROBLEM STATEMENT:
Find the kth largest element in an unsorted array. Note that it is the kth largest 
distinct element.

EXAMPLES:
  [3,2,1,5,6,4], k=2 → 5 (sorted: [1,2,3,4,5,6], 2nd largest is 5)
  [3,2,3,1,2,4,5,5,6], k=4 → 4 (4th largest: 6,5,4)
  [99,99], k=2 → 99 (2nd largest is 99)
  [2,1], k=1 → 2 (1st largest is 2)

KEY INSIGHTS:
- Using full sort is O(n log n) - wasteful for small k!
- Using min-heap of size k is O(n log k) - much better!
- The key idea: maintain only k largest elements
- Root of min-heap = kth largest element

WHY MIN-HEAP?
- Min-heap of size k stores k largest elements
- Root = minimum of those k elements = kth largest!
- Each time we exceed k size, pop the minimum (smallest of k largest)

COMPLEXITY:
Time:  O(n log k) - iterate all n elements, each push/pop is O(log k)
Space: O(k) - heap stores at most k elements

APPROACHES:
1. Min-Heap: O(n log k) - Best for small k
2. QuickSelect: O(n) average - Best overall
3. Max-Heap: O(n + k log n) - Alternative
4. Sorting: O(n log n) - Simplest but slowest

EDGE CASES:
- k = 1 → return max element
- k = n → return minimum element
- Duplicates in array → handled correctly
- All same values → still works
"""

import heapq
from typing import List


# ★ MIN-HEAP SOLUTION - Optimal for small k
def findKthLargest(nums: List[int], k: int) -> int:
    """
    Find kth largest using min-heap of size k.
    
    Algorithm:
    1. Maintain a min-heap with maximum k elements
    2. For each number:
       - Push to heap
       - If heap size > k, pop smallest (maintain k largest)
    3. Root of heap = kth largest
    
    Insight: After processing all elements, heap contains k largest.
    The minimum of those k elements is the kth largest!
    
    Example: [3,2,1,5,6,4], k=2
    After heap size 2: [2,3] then [3,4] then [4,5] then [5,6]
    Root = 5 = 2nd largest ✓
    
    Time: O(n log k)
    Space: O(k)
    """
    min_heap = []
    
    # Add first k elements
    for num in nums:
        heapq.heappush(min_heap, num)
        
        # Keep only k largest elements
        if len(min_heap) > k:
            heapq.heappop(min_heap)  # Remove smallest of k largest
    
    return min_heap[0]  # Root is kth largest


# ★ MAX-HEAP SOLUTION - Alternative approach
def findKthLargest_maxheap(nums: List[int], k: int) -> int:
    """
    Use max-heap (negative values) instead.
    
    Python's heapq is min-heap, so we negate values to simulate max-heap.
    
    Algorithm:
    1. Convert all numbers to negative (max-heap simulation)
    2. Heapify in O(n)
    3. Pop k-1 times to get past k-1 largest elements
    4. Return root (kth largest)
    
    Time: O(n + k log n)
    Space: O(1) if we modify in-place, O(n) for heap copy
    """
    # Negate to simulate max-heap
    max_heap = [-num for num in nums]
    heapq.heapify(max_heap)
    
    # Pop k-1 times to reach kth largest
    for _ in range(k - 1):
        heapq.heappop(max_heap)
    
    return -max_heap[0]  # Negate back to positive


# ★ QUICKSELECT SOLUTION - Fastest average O(n)
def findKthLargest_quickselect(nums: List[int], k: int) -> int:
    """
    Use QuickSelect algorithm - like QuickSort but only for partition we need.
    
    Algorithm:
    1. Randomly select pivot
    2. Partition array into smaller/larger than pivot
    3. If kth largest is in left part, recurse left
    4. If kth largest is in right part, recurse right
    5. If pivot is kth largest, return it
    
    Average: O(n) - much better than sorting!
    Worst: O(n²) if pivot always bad (rare with random selection)
    
    Space: O(log n) for recursion
    """
    def partition(left, right, pivot_index):
        pivot_value = nums[pivot_index]
        # Move pivot to end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        store_index = left
        
        # Move all larger elements to left
        for i in range(left, right):
            if nums[i] > pivot_value:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        
        # Move pivot to final position
        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index
    
    def select(left, right, k_smallest):
        if left == right:
            return nums[left]
        
        # Choose random pivot
        import random
        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)
        
        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        else:
            return select(pivot_index + 1, right, k_smallest)
    
    # kth largest = (n - k)th smallest
    return select(0, len(nums) - 1, len(nums) - k)


# ★ VERBOSE SOLUTION - Shows step-by-step
def findKthLargest_verbose(nums: List[int], k: int) -> int:
    """
    Min-heap solution with detailed output.
    """
    print(f"Array: {nums}")
    print(f"Finding {k}th largest element\n")
    
    min_heap = []
    
    for i, num in enumerate(nums):
        heapq.heappush(min_heap, num)
        print(f"Step {i+1}: Add {num}")
        print(f"  Heap: {sorted(min_heap)}")
        
        if len(min_heap) > k:
            removed = heapq.heappop(min_heap)
            print(f"  Remove minimum {removed} (heap size > k)")
            print(f"  Heap: {sorted(min_heap)}")
        print()
    
    result = min_heap[0]
    print(f"Final heap (k largest): {sorted(min_heap)}")
    print(f"Root (kth largest): {result}")
    return result


# COMPREHENSIVE TEST CASES
if __name__ == "__main__":
    test_cases = [
        ([3,2,1,5,6,4], 2, 5),
        ([3,2,3,1,2,4,5,5,6], 4, 4),
        ([1], 1, 1),
        ([1,2], 1, 2),
        ([1,2], 2, 1),
        ([99,99], 2, 99),
    ]
    
    print("="*70)
    print("LeetCode #215 - Kth Largest Element (Complete Solutions)")
    print("="*70)
    
    print("\n✓ MIN-HEAP SOLUTION (Optimal for small k):")
    for nums, k, exp in test_cases:
        result = findKthLargest(nums[:], k)  # Copy array
        status = "✓" if result == exp else "✗"
        print(f"{status} k={k} in {nums} → {result} (expected {exp})")
    
    print("\n✓ MAX-HEAP SOLUTION:")
    for nums, k, exp in test_cases:
        result = findKthLargest_maxheap(nums[:], k)
        status = "✓" if result == exp else "✗"
        print(f"{status} k={k} → {result}")
    
    print("\n✓ QUICKSELECT SOLUTION (Fastest average):")
    for nums, k, exp in test_cases:
        result = findKthLargest_quickselect(nums[:], k)
        status = "✓" if result == exp else "✗"
        print(f"{status} k={k} → {result}")
    
    print("\n" + "="*70)
    print("📚 VERBOSE WALKTHROUGH")
    print("="*70)
    findKthLargest_verbose([3,2,1,5,6,4], 2)

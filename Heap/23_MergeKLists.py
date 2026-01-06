"""
LeetCode #23 - Merge K Sorted Lists | ENHANCED SOLUTION
Topic: Heap / Linked List | Difficulty: Hard

PROBLEM STATEMENT:
You are given an array of k linked-lists lists, each linked-list is sorted in 
ascending order. Merge all the linked-lists into one sorted linked-list and 
return it.

EXAMPLES:
  [[1,4,5],[1,3,4],[2,6]] → 1→1→2→3→4→4→5→6
  [[]] → None (empty input)
  [[1]] → 1 (single list)
  [[], [0]] → 0 (some empty lists)

KEY INSIGHTS:
- Naive approach: merge k lists one by one = O(k²n)
- Heap approach: maintain k heads = O(nk log k) - much better!
- The trick: always take from heap (always minimum)
- Add next node from the list we took from

WHY HEAP?
- Min-heap always gives us the smallest element
- We can have heads from all k lists in heap
- Always merge the two smallest at each step
- Index i distinguishes nodes with same value from different lists

COMPLEXITY:
Time:  O(n log k) where n = total nodes, k = number of lists
       Each of n nodes is pushed/popped once: O(n log k)
Space: O(k) for heap (at most k nodes at a time)

APPROACHES:
1. Heap (Min): O(n log k) - Best!
2. Pairwise Merge: O(n log k) - Alternative
3. Merge One by One: O(nk) - Too slow
4. Divide & Conquer: O(n log k) - Also good

EDGE CASES:
- Empty lists array → return None
- Arrays with None values → handle gracefully
- Single list → return it
- All lists empty → return None
"""

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ★ MIN-HEAP SOLUTION - Optimal
def mergeKLists(lists):
    """
    Merge k sorted lists using min-heap.
    
    Algorithm:
    1. Add head of each non-empty list to min-heap
       - Use tuple: (value, index, node) for comparison
       - Index helps break ties
    2. While heap is not empty:
       - Pop minimum value node
       - Attach to result
       - If node has next, push it to heap
    3. Return result (skip dummy)
    
    Why this works:
    - Heap always gives us the minimum head
    - We build result by always taking minimum
    - Efficiency: Only k elements in heap at once
    
    Example:
    Lists: [1→4→5], [1→3→4], [2→6]
    Heap initially: [(1,0,node1), (1,1,node2), (2,2,node3)]
    
    Step 1: Pop (1,0) → take node with 1 from list1
    Push (4,0) → next from list1
    Heap: [(1,1,node2), (2,2,node3), (4,0)]
    
    Step 2: Pop (1,1) → take node with 1 from list2
    Push (3,1) → next from list2
    Result so far: 1→1
    
    Continue until heap empty...
    
    Time: O(n log k) | Space: O(k)
    """
    heap = []
    
    # Add first node from each non-empty list
    for i, node in enumerate(lists):
        if node:
            # Use (value, index, node) tuple
            # index prevents comparison of nodes (which are not comparable)
            heapq.heappush(heap, (node.val, i, node))
    
    dummy = ListNode(0)
    current = dummy
    
    # Build result by always taking minimum
    while heap:
        val, idx, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        
        # If node has next, add to heap
        if node.next:
            heapq.heappush(heap, (node.next.val, idx, node.next))
    
    return dummy.next


# ★ PAIRWISE MERGE SOLUTION - Alternative
def mergeKLists_pairwise(lists):
    """
    Merge pairwise: divide and conquer approach.
    
    Algorithm:
    1. If 0 or 1 lists, return
    2. Merge lists[0] with lists[1], lists[2] with lists[3], etc.
    3. Repeat with halved list
    4. Continue until single list
    
    Visualization:
    [l1, l2, l3, l4] → [merge(l1,l2), merge(l3,l4)]
                     → [merge(result1, result2)]
    
    Advantage: No heap needed, can reuse merge2 function
    Time: O(n log k) | Space: O(log k) for recursion
    """
    if not lists:
        return None
    
    if len(lists) == 1:
        return lists[0]
    
    def merge2(l1, l2):
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next
    
    # Pairwise merge
    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            if i + 1 < len(lists):
                merged.append(merge2(lists[i], lists[i + 1]))
            else:
                merged.append(lists[i])
        lists = merged
    
    return lists[0]


# ★ VERBOSE SOLUTION - Shows process
def mergeKLists_verbose(lists):
    """
    Shows heap-based merge with detailed output.
    """
    def list_to_string(node):
        vals = []
        while node:
            vals.append(str(node.val))
            node = node.next
        return "→".join(vals) if vals else "∅"
    
    print("Initial lists:")
    for i, lst in enumerate(lists):
        print(f"  List {i}: {list_to_string(lst)}")
    print()
    
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    
    dummy = ListNode(0)
    current = dummy
    step = 0
    
    while heap:
        step += 1
        val, idx, node = heapq.heappop(heap)
        print(f"Step {step}: Take {val} from list {idx}")
        current.next = node
        current = current.next
        
        if node.next:
            print(f"  Push next {node.next.val} back to heap")
            heapq.heappush(heap, (node.next.val, idx, node.next))
    
    print(f"\nMerged result: {list_to_string(dummy.next)}")
    return dummy.next


# COMPREHENSIVE TEST CASES
if __name__ == "__main__":
    def list_to_vals(node):
        vals = []
        while node:
            vals.append(node.val)
            node = node.next
        return vals
    
    def create_list(vals):
        if not vals:
            return None
        head = ListNode(vals[0])
        curr = head
        for val in vals[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head
    
    print("="*70)
    print("LeetCode #23 - Merge K Sorted Lists (Complete Solutions)")
    print("="*70)
    
    # Test 1: Standard merge
    print("\n✓ Test 1: [[1,4,5], [1,3,4], [2,6]]")
    l1 = create_list([1, 4, 5])
    l2 = create_list([1, 3, 4])
    l3 = create_list([2, 6])
    result = mergeKLists([l1, l2, l3])
    print(f"  Heap: {list_to_vals(result)}")
    
    # Test 2: Some empty lists
    print("\n✓ Test 2: [[], [0]]")
    l1 = None
    l2 = create_list([0])
    result = mergeKLists([l1, l2])
    print(f"  Heap: {list_to_vals(result)}")
    
    # Test 3: Empty array
    print("\n✓ Test 3: []")
    result = mergeKLists([])
    print(f"  Heap: {list_to_vals(result) if result else None}")
    
    # Test 4: Pairwise solution
    print("\n✓ Test 4: Pairwise [[1,4,5], [1,3,4], [2,6]]")
    l1 = create_list([1, 4, 5])
    l2 = create_list([1, 3, 4])
    l3 = create_list([2, 6])
    result = mergeKLists_pairwise([l1, l2, l3])
    print(f"  Pairwise: {list_to_vals(result)}")
    
    # Test 5: Verbose
    print("\n✓ Test 5: Verbose walkthrough")
    l1 = create_list([1, 4, 5])
    l2 = create_list([1, 3, 4])
    l3 = create_list([2, 6])
    result = mergeKLists_verbose([l1, l2, l3])
    vals = []
    while result:
        vals.append(result.val)
        result = result.next
    print(f"Merged: {vals}")

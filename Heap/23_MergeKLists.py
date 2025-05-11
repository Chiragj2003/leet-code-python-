"""
LeetCode #23 - Merge K Sorted Lists
Topic: Heap / Linked List
Difficulty: Hard

PROBLEM EXPLANATION (Easy Terms):
Merge k sorted linked lists into one sorted list.

Example:
[[1,4,5],[1,3,4],[2,6]] -> [1,1,2,3,4,4,5,6]

Think of it like:
Merging multiple sorted streams!

WHY THIS WORKS:
Use min-heap to track smallest elements from each list.

Time: O(n log k) where n is total nodes
Space: O(k) for heap
"""

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    """Merge k sorted lists"""
    heap = []
    
    # Add first node from each list
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    
    dummy = ListNode(0)
    curr = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next


# Test
if __name__ == "__main__":
    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))
    
    result = mergeKLists([l1, l2, l3])
    
    vals = []
    while result:
        vals.append(result.val)
        result = result.next
    print(f"Merged: {vals}")

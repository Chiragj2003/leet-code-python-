"""
LeetCode #21 - Merge Two Sorted Lists | ENHANCED SOLUTION
Topic: Linked List | Difficulty: Easy

PROBLEM STATEMENT:
You are given the heads of two sorted linked lists list1 and list2. Merge the two lists 
in a ONE SORTED LIST. The list should be made by splicing together the nodes of the two 
lists. Return the head of the merged linked list.

EXAMPLES:
  list1: 1→2→4  |  list2: 1→3→4  →  1→1→2→3→4→4
  list1: []     |  list2: 0      →  0
  list1: []     |  list2: []     →  []
  list1: 1→5→8 |  list2: 2→3→4  →  1→2→3→4→5→8

KEY INSIGHTS:
- Both input lists are already SORTED
- Just need to merge them maintaining sort order
- Like merging in MergeSort!
- Dummy node trick simplifies the code (no special first node handling)

COMPLEXITY:
Time:  O(n + m) where n, m = lengths of list1 and list2
       (visit each node exactly once)
Space: O(1) - only use a few pointers, don't create new nodes

ALGORITHM:
1. Create dummy node to simplify logic
2. Compare current nodes from both lists
3. Attach the smaller one to result
4. Move pointer in the list we took from
5. When one list is empty, attach the rest of other
6. Return dummy.next

EDGE CASES:
- Empty list1 → return list2
- Empty list2 → return list1
- Both empty → return None
- Different lengths → works correctly
- All values same → works
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ★ STANDARD SOLUTION - Iterative with Dummy Node
def mergeTwoLists(list1, list2):
    """
    Merge two sorted lists iteratively.
    
    Algorithm:
    1. Create dummy node (val=0) to make code simpler
    2. Use current pointer at dummy
    3. While both lists have nodes:
       - Compare list1.val vs list2.val
       - Attach smaller to current
       - Move pointer in that list
       - Move current pointer
    4. After loop, attach remaining (one list might be empty)
    5. Return dummy.next (skip the dummy)
    
    Example step-by-step:
    list1: 1→2→4    list2: 1→3→4
    
    Dummy→
    
    Compare 1 vs 1: tie, take 1 from list1
    Dummy→1 (from list1)→2→4
    
    Compare 2 vs 1: take 1 from list2
    Dummy→1→1 (from list2)→3→4
    
    Compare 2 vs 3: take 2 from list1
    Dummy→1→1→2→4
    
    Compare 4 vs 3: take 3 from list2
    Dummy→1→1→2→3→4
    
    Compare 4 vs 4: take 4 from list1
    Dummy→1→1→2→3→4→4
    
    list2 exhausted, attach rest of list1 (empty)
    Result: 1→1→2→3→4→4 ✓
    
    Time: O(n + m) | Space: O(1)
    """
    # Dummy node simplifies code (no special handling for first node)
    dummy = ListNode(0)
    current = dummy
    
    # Merge both lists
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Attach remaining (only one will be non-empty)
    current.next = list1 if list1 else list2
    
    return dummy.next  # Skip dummy node


# ★ RECURSIVE SOLUTION - Elegant but uses stack space
def mergeTwoLists_recursive(list1, list2):
    """
    Merge two sorted lists recursively.
    
    Base cases:
    - If list1 is empty, return list2
    - If list2 is empty, return list1
    
    Recursive case:
    - Compare list1.val vs list2.val
    - Attach smaller one's next to recursive merge result
    - Return smaller one
    
    Time: O(n + m)
    Space: O(n + m) for recursion call stack
    """
    # Base cases
    if not list1:
        return list2
    if not list2:
        return list1
    
    # Recursive case
    if list1.val < list2.val:
        list1.next = mergeTwoLists_recursive(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists_recursive(list1, list2.next)
        return list2


# ★ VERBOSE SOLUTION - Shows merging step-by-step
def mergeTwoLists_verbose(list1, list2):
    """
    Merge with detailed output showing each step.
    """
    def list_to_string(node):
        vals = []
        while node:
            vals.append(str(node.val))
            node = node.next
        return "→".join(vals) if vals else "None"
    
    print(f"Merging: {list_to_string(list1)} and {list_to_string(list2)}")
    
    dummy = ListNode(0)
    current = dummy
    orig_l1, orig_l2 = list1, list2
    
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            print(f"  Took {list1.val} from list1")
            list1 = list1.next
        else:
            current.next = list2
            print(f"  Took {list2.val} from list2")
            list2 = list2.next
        current = current.next
    
    current.next = list1 or list2
    
    if not list1:
        print(f"  Attached remaining from list2")
    else:
        print(f"  Attached remaining from list1")
    
    result = dummy.next
    print(f"Result: {list_to_string(result)}")
    return result


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
        current = head
        for val in vals[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    print("="*70)
    print("LeetCode #21 - Merge Two Sorted Lists (Complete Solutions)")
    print("="*70)
    
    # Test 1: Standard merge
    print("\n✓ Test 1: [1,2,4] and [1,3,4]")
    l1 = create_list([1, 2, 4])
    l2 = create_list([1, 3, 4])
    result = mergeTwoLists(l1, l2)
    print(f"  Iterative: {list_to_vals(result)}")
    
    # Test 2: Empty list
    print("\n✓ Test 2: [] and [0]")
    l1 = None
    l2 = create_list([0])
    result = mergeTwoLists(l1, l2)
    print(f"  Iterative: {list_to_vals(result)}")
    
    # Test 3: Both empty
    print("\n✓ Test 3: [] and []")
    result = mergeTwoLists(None, None)
    print(f"  Iterative: {list_to_vals(result)}")
    
    # Test 4: Recursive solution
    print("\n✓ Test 4: Recursive [1,5,8] and [2,3,4]")
    l1 = create_list([1, 5, 8])
    l2 = create_list([2, 3, 4])
    result = mergeTwoLists_recursive(l1, l2)
    print(f"  Recursive: {list_to_vals(result)}")
    
    # Test 5: Verbose
    print("\n✓ Test 5: Verbose walkthrough")
    l1 = create_list([1, 2, 4])
    l2 = create_list([1, 3, 4])
    result = result.next
    print(f"Merged: {vals}")

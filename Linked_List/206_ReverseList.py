"""
LeetCode #206 - Reverse Linked List | ENHANCED SOLUTION
Topic: Linked List | Difficulty: Easy

PROBLEM STATEMENT:
Given the head of a singly linked list, reverse the list, and return the reversed list.

EXAMPLES:
  1→2→3→4→5 becomes 5→4→3→2→1
  1→2 becomes 2→1
  1 becomes 1
  None becomes None

KEY INSIGHTS:
- Need to reverse the direction of ALL pointers
- Must save next node before changing current.next
- Three pointer technique: prev, current, next
- Two approaches: Iterative (cleaner) vs Recursive (elegant)

COMPLEXITY:
Time:  O(n) - visit each node once
Space: O(1) iterative, O(n) recursive (call stack)

EDGE CASES:
- Empty list → return None
- Single node → return head
- Two nodes → reverse them
- Already reversed → works
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ★ ITERATIVE SOLUTION - Best (Simple & Space-Efficient)
def reverseList(head):
    """
    Reverse linked list iteratively using three pointers.
    
    Algorithm:
    1. Initialize: prev=None, current=head
    2. While current is not None:
       a. Save next node (current.next)
       b. Reverse current's pointer (current.next = prev)
       c. Move prev to current
       d. Move current to next
    3. Return prev (new head)
    
    Visual:
    Before:  1 → 2 → 3 → None
    Step 1:  None ← 1   2 → 3 → None
    Step 2:  None ← 1 ← 2   3 → None
    Step 3:  None ← 1 ← 2 ← 3
    Return:  3 ← 2 ← 1 (3 is new head)
    
    Time: O(n) | Space: O(1)
    """
    prev = None
    current = head
    
    while current:
        # Save next before we change current.next
        next_temp = current.next
        
        # Reverse the pointer
        current.next = prev
        
        # Move prev and current one step forward
        prev = current
        current = next_temp
    
    return prev  # prev is now the new head


# ★ RECURSIVE SOLUTION - Elegant but uses stack space
def reverseList_recursive(head):
    """
    Reverse linked list recursively.
    
    Algorithm:
    1. Base case: if head is None or single node, return it
    2. Recursively reverse the rest of the list
    3. Point next node back to current node
    4. Set current.next to None (to break original link)
    5. Return new head
    
    Example:
    reverseList(1→2→3→None)
      → reverseList(2→3→None)
        → reverseList(3→None)
          → reverseList(None) returns 3
        → 2.next = None, 3.next = 2, return 3
      → 1.next = None, 2.next = 1, return 3
    Result: 3→2→1→None
    
    Time: O(n) | Space: O(n) for recursion stack
    """
    # Base case
    if not head or not head.next:
        return head
    
    # Recursively reverse the rest
    new_head = reverseList_recursive(head.next)
    
    # Reverse the link between current and next
    head.next.next = head
    head.next = None
    
    return new_head


# ★ DETAILED SOLUTION - With step-by-step visualization
def reverseList_verbose(head):
    """
    Reverse list with detailed output showing each step.
    Great for understanding the algorithm!
    """
    def list_to_string(node):
        vals = []
        while node:
            vals.append(str(node.val))
            node = node.next
        return " → ".join(vals) if vals else "None"
    
    print(f"Original list: {list_to_string(head)}")
    
    prev = None
    current = head
    step = 0
    
    while current:
        step += 1
        next_temp = current.next
        current.next = prev
        
        print(f"Step {step}: Reverse node {current.val}")
        print(f"  Current forward: {list_to_string(next_temp) if next_temp else 'None'}")
        print(f"  Current backward chain: {list_to_string(current)}")
        
        prev = current
        current = next_temp
    
    print(f"\nFinal reversed: {list_to_string(prev)}")
    return prev


# COMPREHENSIVE TEST CASES
if __name__ == "__main__":
    def list_to_vals(node):
        vals = []
        while node:
            vals.append(node.val)
            node = node.next
        return vals
    
    print("="*70)
    print("LeetCode #206 - Reverse Linked List (Complete Solutions)")
    print("="*70)
    
    # Test 1: Normal list
    print("\n✓ Test 1: 1→2→3→4→5")
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reversed1 = reverseList(head1)
    print(f"  Iterative: {list_to_vals(reversed1)}")
    
    # Test 2: Two nodes
    print("\n✓ Test 2: 1→2")
    head2 = ListNode(1, ListNode(2))
    reversed2 = reverseList(head2)
    print(f"  Iterative: {list_to_vals(reversed2)}")
    
    # Test 3: Single node
    print("\n✓ Test 3: 1")
    head3 = ListNode(1)
    reversed3 = reverseList(head3)
    print(f"  Iterative: {list_to_vals(reversed3)}")
    
    # Test 4: Recursive solution
    print("\n✓ Test 4: Recursive 1→2→3→4→5")
    head4 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reversed4 = reverseList_recursive(head4)
    print(f"  Recursive: {list_to_vals(reversed4)}")
    
    # Test 5: Verbose with visualization
    print("\n✓ Test 5: Verbose walkthrough")
    head5 = ListNode(1, ListNode(2, ListNode(3)))
    reverseList_verbose(head5)

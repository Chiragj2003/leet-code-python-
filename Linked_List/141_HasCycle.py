"""
LeetCode #141 - Linked List Cycle | ENHANCED SOLUTION
Topic: Linked List / Two Pointers | Difficulty: Easy

PROBLEM STATEMENT:
Given the head of a linked list, determine if the linked list has a cycle in it.
A cycle exists in a linked list if there is some node in the list that can be reached 
again by continuously following the next pointer.

EXAMPLES:
  1 → 2 → 3 → 4 → 2 (back to 2)  →  True (cycle detected)
  1 → 2 → 3 (ends)  →  False (no cycle)
  1 (single node) →  False (no cycle)

KEY INSIGHTS:
- Cycle means a node's next pointer eventually points back to a previous node
- Can detect without storing all nodes (space-efficient needed!)
- Floyd's Cycle Detection (Tortoise & Hare) is the optimal approach

WHY FLOYD'S ALGORITHM WORKS:
If there's a cycle, two pointers at different speeds MUST eventually meet:
- Slow pointer: 1 step per iteration
- Fast pointer: 2 steps per iteration
- If they're in the same cycle, fast will eventually catch slow
- In a cycle, the relative position changes by 1 each step
- Eventually they must meet if cycle exists

COMPLEXITY:
Time:  O(n) where n = number of nodes in list
Space: O(1) - only uses two pointers, no extra data structures!

EDGE CASES:
- Empty list (head = None) → False
- Single node with no cycle → False
- Single node pointing to itself → True
- Large list with cycle at end → Still O(n)
- Multiple cycles → Works (detects any cycle)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ★ STANDARD SOLUTION - Floyd's Cycle Detection (Optimal!)
def hasCycle(head):
    """
    Detect cycle using Two Pointers (Floyd's Algorithm).
    
    OPTIMAL: O(1) space, O(n) time
    
    Algorithm:
    1. Start both slow and fast at head
    2. Move slow by 1, fast by 2 each iteration
    3. If they meet → cycle exists
    4. If fast reaches end → no cycle
    
    Why it works: In a cycle, fast will lap slow eventually.
    """
    if not head or not head.next:
        return False
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next        # Move 1 step
        fast = fast.next.next   # Move 2 steps
        
        if slow == fast:        # They met = cycle!
            return True
    
    return False


# ★ HASH SET SOLUTION - Alternative (Easier to understand)
def hasCycle_hashset(head):
    """
    Detect cycle using hash set.
    
    Simpler to understand but uses O(n) space.
    
    Algorithm:
    1. Keep set of all visited nodes
    2. Traverse list, adding nodes to set
    3. If we see a node twice → cycle!
    4. If we reach None → no cycle
    """
    visited = set()
    current = head
    
    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next
    
    return False


# ★ FIND CYCLE START NODE
def detectCycle(head):
    """
    Enhanced Floyd's: Also returns the NODE where cycle starts.
    
    Key insight: When pointers meet in cycle, if we reset one to head
    and move both 1 step, they'll meet at cycle start!
    
    Returns: Node where cycle starts, or None if no cycle
    """
    if not head or not head.next:
        return None
    
    slow = fast = head
    
    # Find meeting point
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            # Found meeting point, now find start
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow  # This is the cycle start
    
    return None  # No cycle


# ★ FIND CYCLE LENGTH
def getCycleLength(head):
    """
    Find the LENGTH of the cycle if it exists.
    
    Algorithm:
    1. Find meeting point using Floyd's
    2. Keep one pointer at meeting point
    3. Move other pointer, count steps until meeting again
    4. Count = cycle length
    """
    if not head or not head.next:
        return 0
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            # Found cycle, now count length
            length = 1
            temp = slow.next
            while temp != slow:
                length += 1
                temp = temp.next
            return length
    
    return 0


# COMPREHENSIVE TEST CASES
if __name__ == "__main__":
    print("="*70)
    print("LeetCode #141 - Linked List Cycle (Complete Solutions)")
    print("="*70)
    
    # Test 1: Cycle exists
    print("\n✓ Test 1: Cycle exists (1→2→3→4→2)")
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2  # Cycle!
    
    print(f"  Floyd's: {hasCycle(n1)}")
    print(f"  HashSet: {hasCycle_hashset(n1)}")
    cycle_start = detectCycle(n1)
    print(f"  Cycle starts at node: {cycle_start.val if cycle_start else None}")
    print(f"  Cycle length: {getCycleLength(n1)}")
    
    # Test 2: No cycle
    print("\n✓ Test 2: No cycle (1→2→3→4→None)")
    m1 = ListNode(1)
    m2 = ListNode(2)
    m3 = ListNode(3)
    m4 = ListNode(4)
    m1.next = m2
    m2.next = m3
    m3.next = m4
    
    print(f"  Floyd's: {hasCycle(m1)}")
    print(f"  HashSet: {hasCycle_hashset(m1)}")
    print(f"  Cycle length: {getCycleLength(m1)}")
    
    # Test 3: Single node with cycle
    print("\n✓ Test 3: Single node pointing to itself")
    p1 = ListNode(1)
    p1.next = p1  # Self-cycle
    
    print(f"  Floyd's: {hasCycle(p1)}")
    print(f"  Cycle starts at: {detectCycle(p1).val if detectCycle(p1) else None}")

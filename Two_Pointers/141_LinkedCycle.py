"""
LeetCode #141 - Linked List Cycle
Topic: Two Pointers (Fast & Slow)
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Detect if a linked list has a cycle (a node points back to a previous node).

Example:
3 -> 2 -> 0 -> -4 -> (back to 2)  -> True (cycle exists)
1 -> 2 -> None -> False (no cycle)

Think of it like:
People running on a track. If the track loops, fast runner
will eventually lap the slow runner!

WHY THIS WORKS (Simple Explanation):
Use Floyd's Cycle Detection (Tortoise and Hare):
1. Slow pointer moves 1 step at a time
2. Fast pointer moves 2 steps at a time
3. If cycle exists, fast will eventually catch slow!
4. If fast reaches None, no cycle

Like two runners on a circular track - faster one catches slower one!

Time Complexity: O(n) - at most n iterations
Space Complexity: O(1) - only two pointers
"""

class ListNode:
    """Definition for singly-linked list node"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head):
    """
    Detect cycle using Floyd's algorithm (fast & slow pointers)
    
    Visual example with cycle:
    3 -> 2 -> 0 -> -4
         ^         |
         |_________|
    
    Step 1: slow=3, fast=3
    Step 2: slow=2, fast=0
    Step 3: slow=0, fast=2
    Step 4: slow=-4, fast=-4  -> They meet! Cycle detected!
    
    Example without cycle:
    1 -> 2 -> 3 -> None
    
    Step 1: slow=1, fast=1
    Step 2: slow=2, fast=3
    Step 3: slow=3, fast=None  -> Fast reached end, no cycle
    """
    if not head:
        return False
    
    # Initialize pointers
    slow = head
    fast = head
    
    # Move pointers until fast reaches end
    while fast and fast.next:
        slow = slow.next         # Move 1 step
        fast = fast.next.next    # Move 2 steps
        
        # If they meet, cycle exists!
        if slow == fast:
            return True
    
    # Fast reached end, no cycle
    return False


def hasCycle_hashset(head):
    """
    Alternative: Use hashset to track visited nodes
    
    Simpler but uses O(n) extra space
    
    Keep set of visited nodes.
    If we visit a node twice, cycle exists!
    """
    visited = set()
    current = head
    
    while current:
        # If already visited, cycle!
        if current in visited:
            return True
        
        # Mark as visited
        visited.add(current)
        current = current.next
    
    # Reached end without revisiting
    return False


# Helper functions for testing
def create_linked_list_with_cycle(values, pos):
    """
    Create linked list with cycle
    pos = -1 means no cycle
    pos = index where tail connects
    """
    if not values:
        return None
    
    # Create nodes
    head = ListNode(values[0])
    current = head
    nodes = [head]
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
        nodes.append(current)
    
    # Create cycle if pos >= 0
    if pos >= 0:
        current.next = nodes[pos]
    
    return head


# Test cases
if __name__ == "__main__":
    # Test case 1: Cycle at position 1
    print("=== Test Case 1: [3,2,0,-4] with cycle at pos 1 ===")
    head1 = create_linked_list_with_cycle([3, 2, 0, -4], 1)
    result1 = hasCycle(head1)
    print(f"Has cycle: {result1} (Expected: True)")
    print()
    
    # Test case 2: Cycle at position 0
    print("=== Test Case 2: [1,2] with cycle at pos 0 ===")
    head2 = create_linked_list_with_cycle([1, 2], 0)
    result2 = hasCycle(head2)
    print(f"Has cycle: {result2} (Expected: True)")
    print()
    
    # Test case 3: No cycle
    print("=== Test Case 3: [1] with no cycle ===")
    head3 = create_linked_list_with_cycle([1], -1)
    result3 = hasCycle(head3)
    print(f"Has cycle: {result3} (Expected: False)")
    print()
    
    # Test case 4: Empty list
    print("=== Test Case 4: [] (empty) ===")
    result4 = hasCycle(None)
    print(f"Has cycle: {result4} (Expected: False)")
    print()
    
    # Test hashset method
    print("=== Testing Hashset Method ===")
    head5 = create_linked_list_with_cycle([3, 2, 0, -4], 1)
    result5 = hasCycle_hashset(head5)
    print(f"[3,2,0,-4] with cycle: {result5} (Expected: True)")

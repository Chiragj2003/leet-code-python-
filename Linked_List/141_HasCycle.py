"""
LeetCode #141 - Linked List Cycle
Topic: Linked List / Two Pointers
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Detect if linked list has a cycle.

Think of it like:
Does the path loop back on itself?

WHY THIS WORKS (Simple Explanation):
Floyd's Cycle Detection (Tortoise & Hare):
- Slow pointer moves 1 step
- Fast pointer moves 2 steps
- If they meet, there's a cycle!

Time: O(n)
Space: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head):
    """Detect cycle in linked list"""
    if not head:
        return False
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False


# Test
if __name__ == "__main__":
    # Create cycle: 1->2->3->4->2 (back to 2)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2  # Cycle!
    
    print(f"Has cycle: {hasCycle(n1)}")

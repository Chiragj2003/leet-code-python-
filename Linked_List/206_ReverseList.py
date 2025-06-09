"""
LeetCode #206 - Reverse Linked List
Topic: Linked List
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Reverse a singly linked list.

Example:
1->2->3->4->5 becomes 5->4->3->2->1

Think of it like:
Flipping the direction of arrows!

WHY THIS WORKS (Simple Explanation):
Iterate through list, reverse each pointer:
- Save next node
- Point current to previous
- Move forward

Time: O(n)
Space: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    """Reverse linked list iteratively"""
    prev = None
    current = head
    
    while current:
        next_node = current.next  # Save next
        current.next = prev       # Reverse pointer
        prev = current            # Move prev forward
        current = next_node       # Move current forward
    
    return prev


# Test
if __name__ == "__main__":
    # Create list: 1->2->3->4->5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    
    reversed_head = reverseList(head)
    
    # Print
    vals = []
    while reversed_head:
        vals.append(reversed_head.val)
        reversed_head = reversed_head.next
    print(f"Reversed: {vals}")

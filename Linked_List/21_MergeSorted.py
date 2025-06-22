"""
LeetCode #21 - Merge Two Sorted Lists
Topic: Linked List
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Merge two sorted linked lists into one sorted list.

Example:
1->2->4 and 1->3->4 -> 1->1->2->3->4->4

Think of it like:
Merging two sorted piles of cards!

WHY THIS WORKS (Simple Explanation):
Compare heads of both lists, take smaller one.
Repeat until one list is empty, attach remaining.

Time: O(n + m)
Space: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    """Merge two sorted linked lists"""
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Attach remaining
    current.next = list1 or list2
    
    return dummy.next


# Test
if __name__ == "__main__":
    # Create lists
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    
    result = mergeTwoLists(l1, l2)
    
    # Print result
    vals = []
    while result:
        vals.append(result.val)
        result = result.next
    print(f"Merged: {vals}")

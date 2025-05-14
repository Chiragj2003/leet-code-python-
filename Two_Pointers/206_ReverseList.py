"""
LeetCode #206 - Reverse Linked List
Topic: Two Pointers (Linked List)
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Reverse a singly linked list.

Example:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> None
Output: 5 -> 4 -> 3 -> 2 -> 1 -> None

Think of it like:
Imagine a chain of people holding hands.
You want to reverse who's holding whose hand!

WHY THIS WORKS (Simple Explanation):
Keep track of three nodes at a time:
1. Previous node (starts as None)
2. Current node
3. Next node (to not lose the rest of the list)

For each node:
- Save next node (don't lose it!)
- Point current to previous (reverse the link)
- Move pointers forward

Like flipping arrows one by one!

Time Complexity: O(n) - visit each node once
Space Complexity: O(1) - only few pointers
"""

class ListNode:
    """Definition for singly-linked list node"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    """
    Reverse linked list iteratively
    
    Visual example: 1 -> 2 -> 3 -> None
    
    Step 1: prev=None, curr=1, next=2
            None <- 1    2 -> 3 -> None
            
    Step 2: prev=1, curr=2, next=3
            None <- 1 <- 2    3 -> None
            
    Step 3: prev=2, curr=3, next=None
            None <- 1 <- 2 <- 3
            
    Return prev (which is new head = 3)
    """
    prev = None
    curr = head
    
    while curr:
        # Save next node (don't lose it!)
        next_node = curr.next
        
        # Reverse the link
        curr.next = prev
        
        # Move pointers forward
        prev = curr
        curr = next_node
    
    # prev is now the new head
    return prev


def reverseList_recursive(head):
    """
    Reverse linked list recursively
    
    Base case: empty list or single node
    
    Recursive case:
    1. Reverse the rest of the list
    2. Make the next node point back to current
    3. Remove current's forward pointer
    
    Example: 1 -> 2 -> 3 -> None
    
    reverseList(1):
      reverseList(2):
        reverseList(3):
          return 3 (base case)
        Make 3.next = 2
        return 3
      Make 2.next = 1
      return 3
    
    Result: None <- 1 <- 2 <- 3
    """
    # Base case
    if not head or not head.next:
        return head
    
    # Reverse the rest
    new_head = reverseList_recursive(head.next)
    
    # Make next node point back to current
    head.next.next = head
    
    # Remove current's forward pointer
    head.next = None
    
    return new_head


# Helper functions for testing
def create_linked_list(values):
    """Create linked list from list of values"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head


def linked_list_to_list(head):
    """Convert linked list to Python list for display"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([1], [1]),
        ([], []),
    ]
    
    print("=== Testing Iterative Solution ===")
    for input_list, expected in test_cases:
        head = create_linked_list(input_list)
        reversed_head = reverseList(head)
        result = linked_list_to_list(reversed_head)
        
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {input_list}")
        print(f"   Output: {result}")
        print(f"   Expected: {expected}")
        print()
    
    print("=== Testing Recursive Solution ===")
    for input_list, expected in test_cases:
        head = create_linked_list(input_list)
        reversed_head = reverseList_recursive(head)
        result = linked_list_to_list(reversed_head)
        
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {input_list}")
        print(f"   Output: {result}")
        print(f"   Expected: {expected}")
        print()

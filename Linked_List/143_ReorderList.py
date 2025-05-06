"""
LeetCode #143 - Reorder List
Topic: Linked List
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Reorder list: L0 → L1 → L2 → ... → Ln-1 → Ln
Into: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

Example:
1 -> 2 -> 3 -> 4 -> 5
Becomes: 1 -> 5 -> 2 -> 4 -> 3

Think of it like:
Weave the list - take from front, then back, then front, then back...
Like shuffling a deck by splitting and alternating cards!

WHY THIS WORKS (Simple Explanation):
Three steps:
1. Find middle of list (fast/slow pointers)
2. Reverse second half
3. Merge two halves alternately

Like two lines merging - one person from each line!

Time Complexity: O(n) - three passes
Space Complexity: O(1) - in-place modification
"""

class ListNode:
    """Definition for singly-linked list node"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head):
    """
    Reorder list in-place
    
    Visual example: 1 -> 2 -> 3 -> 4 -> 5
    
    Step 1: Find middle
      slow at 3
      First half: 1 -> 2 -> 3
      Second half: 4 -> 5
    
    Step 2: Reverse second half
      First half: 1 -> 2 -> 3
      Second half: 5 -> 4
    
    Step 3: Merge alternately
      Take from first: 1
      Take from second: 5
      Take from first: 2
      Take from second: 4
      Take from first: 3
      
      Result: 1 -> 5 -> 2 -> 4 -> 3
    """
    if not head or not head.next:
        return
    
    # Step 1: Find middle using slow/fast pointers
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse second half
    # slow.next is start of second half
    second = reverse_list(slow.next)
    slow.next = None  # Cut the list in half
    
    # Step 3: Merge two halves
    first = head
    while second:
        # Save next nodes
        temp1 = first.next
        temp2 = second.next
        
        # Weave nodes
        first.next = second
        second.next = temp1
        
        # Move to next pair
        first = temp1
        second = temp2


def reverse_list(head):
    """Helper: Reverse a linked list"""
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev


def reorderList_verbose(head):
    """
    Detailed version showing each step
    """
    if not head or not head.next:
        return
    
    # Show original list
    print("Original list:", list_to_values(head))
    
    # Step 1: Find middle
    print("\nStep 1: Finding middle...")
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    print(f"Middle node value: {slow.val}")
    
    # Step 2: Reverse second half
    print("\nStep 2: Reversing second half...")
    second = reverse_list(slow.next)
    slow.next = None
    
    print(f"First half: {list_to_values(head)}")
    print(f"Second half (reversed): {list_to_values(second)}")
    
    # Step 3: Merge
    print("\nStep 3: Merging alternately...")
    first = head
    step = 0
    while second:
        step += 1
        print(f"  Weave step {step}: {first.val} -> {second.val}")
        
        temp1 = first.next
        temp2 = second.next
        
        first.next = second
        second.next = temp1
        
        first = temp1
        second = temp2
    
    print(f"\nFinal list: {list_to_values(head)}")


def list_to_values(head):
    """Helper: Convert linked list to list of values"""
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values


def create_linked_list(values):
    """Helper: Create linked list from list of values"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([1, 2], [1, 2]),
        ([1], [1]),
    ]
    
    print("=== Testing Reorder List ===")
    for input_vals, expected in test_cases:
        head = create_linked_list(input_vals)
        reorderList(head)
        result = list_to_values(head)
        
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {input_vals}")
        print(f"   Output: {result}")
        print(f"   Expected: {expected}")
        print()
    
    print("=== Verbose Example ===")
    head = create_linked_list([1, 2, 3, 4, 5])
    reorderList_verbose(head)

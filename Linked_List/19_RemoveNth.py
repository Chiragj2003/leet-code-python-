"""
LeetCode #19 - Remove Nth Node From End of List
Topic: Linked List / Two Pointers
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Remove the nth node from the END of the linked list.

Example:
1 -> 2 -> 3 -> 4 -> 5, n=2
Remove 4 (2nd from end): 1 -> 2 -> 3 -> 5

Think of it like:
In a line of people, remove the nth person from the back.
But you can only walk forward through the line!

WHY THIS WORKS (Simple Explanation):
Use TWO POINTERS with a gap of n between them:
1. Move first pointer n steps ahead
2. Move both pointers together until first reaches end
3. Second pointer is now at node BEFORE the target
4. Remove the target node

Like a train with two cars - keep them n steps apart!

Time Complexity: O(n) - single pass
Space Complexity: O(1) - only two pointers
"""

class ListNode:
    """Definition for singly-linked list node"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    """
    Remove nth node from end using two pointers
    
    Visual example: 1 -> 2 -> 3 -> 4 -> 5, n=2
    
    Step 1: Create dummy node (handles edge case of removing head)
    dummy -> 1 -> 2 -> 3 -> 4 -> 5
    
    Step 2: Move fast pointer n+1 steps ahead
    dummy -> 1 -> 2 -> 3 -> 4 -> 5
    slow^              fast^
    
    Step 3: Move both until fast reaches end
    dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> None
                   slow^              fast^
    
    Step 4: slow is before target (4), remove it
    slow.next = slow.next.next
    Result: 1 -> 2 -> 3 -> 5
    """
    # Dummy node simplifies edge cases
    dummy = ListNode(0)
    dummy.next = head
    
    # Initialize two pointers
    slow = fast = dummy
    
    # Move fast pointer n+1 steps ahead
    # +1 to position slow BEFORE the node to remove
    for _ in range(n + 1):
        if not fast:
            return head  # n is too large
        fast = fast.next
    
    # Move both pointers until fast reaches end
    while fast:
        slow = slow.next
        fast = fast.next
    
    # Remove the nth node
    # slow is now at node BEFORE the target
    slow.next = slow.next.next
    
    return dummy.next


def removeNthFromEnd_two_pass(head, n):
    """
    Alternative: Two-pass solution
    
    Pass 1: Count total length
    Pass 2: Go to (length - n)th node and remove next
    
    Easier to understand but requires two passes
    """
    # First pass: Count length
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    
    # Edge case: removing head
    if length == n:
        return head.next
    
    # Second pass: Find node before target
    target_pos = length - n
    current = head
    for _ in range(target_pos - 1):
        current = current.next
    
    # Remove target node
    current.next = current.next.next
    
    return head


def removeNthFromEnd_verbose(head, n):
    """
    Detailed version showing the process
    """
    # Convert to list for visualization
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    
    print(f"Original list: {values}")
    print(f"Remove {n}th node from end\n")
    
    # Perform removal
    dummy = ListNode(0)
    dummy.next = head
    slow = fast = dummy
    
    # Move fast n+1 steps
    print("Step 1: Move fast pointer n+1 steps ahead")
    for i in range(n + 1):
        if not fast:
            print("Error: n is too large!")
            return head
        fast = fast.next
        print(f"  Step {i+1}: fast moved")
    
    print(f"\nStep 2: Move both pointers until fast reaches end")
    step = 0
    while fast:
        slow = slow.next
        fast = fast.next
        step += 1
        print(f"  Step {step}: Both pointers moved")
    
    print(f"\nStep 3: Remove target node")
    if slow.next:
        target_val = slow.next.val
        print(f"  Removing node with value: {target_val}")
        slow.next = slow.next.next
    
    # Show result
    result = []
    current = dummy.next
    while current:
        result.append(current.val)
        current = current.next
    
    print(f"\nResult: {result}")
    return dummy.next


# Helper functions
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
    """Convert linked list to Python list"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([1, 2, 3], 3, [2, 3]),
    ]
    
    print("=== Testing Two-Pointer Solution ===")
    for values, n, expected in test_cases:
        head = create_linked_list(values)
        result_head = removeNthFromEnd(head, n)
        result = linked_list_to_list(result_head)
        
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {values}, n={n}")
        print(f"   Output: {result}")
        print(f"   Expected: {expected}")
        print()
    
    print("=== Testing Two-Pass Solution ===")
    for values, n, expected in test_cases:
        head = create_linked_list(values)
        result_head = removeNthFromEnd_two_pass(head, n)
        result = linked_list_to_list(result_head)
        
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {values}, n={n} -> {result}")
    
    print("\n=== Verbose Example ===")
    head = create_linked_list([1, 2, 3, 4, 5])
    removeNthFromEnd_verbose(head, 2)

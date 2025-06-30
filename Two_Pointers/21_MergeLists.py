"""
LeetCode #21 - Merge Two Sorted Lists
Topic: Two Pointers (Linked List)
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Merge two sorted linked lists into one sorted list.

Example:
List1: 1 -> 2 -> 4
List2: 1 -> 3 -> 4
Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

Think of it like:
Two lines of people sorted by height.
Merge them into one line, keeping shortest to tallest!

WHY THIS WORKS (Simple Explanation):
Use two pointers (one for each list):
1. Compare values at both pointers
2. Take the smaller one, add to result
3. Move that pointer forward
4. Repeat until both lists exhausted

Like merging two sorted decks of cards!

Time Complexity: O(n + m) - visit all nodes
Space Complexity: O(1) - only pointers (excluding result)
"""

class ListNode:
    """Definition for singly-linked list node"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    """
    Merge two sorted linked lists
    
    Visual example:
    list1: 1 -> 2 -> 4
    list2: 1 -> 3 -> 4
    
    Step 1: Compare 1 and 1 -> take list1's 1
    Step 2: Compare 2 and 1 -> take list2's 1
    Step 3: Compare 2 and 3 -> take 2
    Step 4: Compare 4 and 3 -> take 3
    Step 5: Compare 4 and 4 -> take list1's 4
    Step 6: Only list2's 4 left -> append
    
    Result: 1 -> 1 -> 2 -> 3 -> 4 -> 4
    """
    # Create dummy node to simplify logic
    dummy = ListNode(0)
    current = dummy
    
    # While both lists have nodes
    while list1 and list2:
        if list1.val <= list2.val:
            # Take from list1
            current.next = list1
            list1 = list1.next
        else:
            # Take from list2
            current.next = list2
            list2 = list2.next
        
        # Move result pointer forward
        current = current.next
    
    # Append remaining nodes (one list is exhausted)
    if list1:
        current.next = list1
    if list2:
        current.next = list2
    
    # Return head (skip dummy)
    return dummy.next


def mergeTwoLists_recursive(list1, list2):
    """
    Recursive approach
    
    Base cases:
    - If one list empty, return the other
    
    Recursive case:
    - Take smaller head
    - Recursively merge rest
    
    Example: list1=[1,2,4], list2=[1,3,4]
    
    merge([1,2,4], [1,3,4]):
      1 <= 1, take list1's 1
      1.next = merge([2,4], [1,3,4])
        2 > 1, take list2's 1
        1.next = merge([2,4], [3,4])
          2 < 3, take 2
          2.next = merge([4], [3,4])
            ...
    """
    # Base cases
    if not list1:
        return list2
    if not list2:
        return list1
    
    # Choose smaller head and recurse
    if list1.val <= list2.val:
        list1.next = mergeTwoLists_recursive(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists_recursive(list1, list2.next)
        return list2


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
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([1], [2], [1, 2]),
        ([5], [1, 2, 3], [1, 2, 3, 5]),
    ]
    
    print("=== Testing Iterative Solution ===")
    for list1_vals, list2_vals, expected in test_cases:
        list1 = create_linked_list(list1_vals)
        list2 = create_linked_list(list2_vals)
        merged = mergeTwoLists(list1, list2)
        result = linked_list_to_list(merged)
        
        status = "✓" if result == expected else "✗"
        print(f"{status} list1={list1_vals}, list2={list2_vals}")
        print(f"   Output: {result}")
        print(f"   Expected: {expected}")
        print()
    
    print("=== Testing Recursive Solution ===")
    for list1_vals, list2_vals, expected in test_cases:
        list1 = create_linked_list(list1_vals)
        list2 = create_linked_list(list2_vals)
        merged = mergeTwoLists_recursive(list1, list2)
        result = linked_list_to_list(merged)
        
        status = "✓" if result == expected else "✗"
        print(f"{status} list1={list1_vals}, list2={list2_vals}")
        print(f"   Output: {result}")
        print(f"   Expected: {expected}")
        print()

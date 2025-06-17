"""
LeetCode #234 - Palindrome Linked List
Topic: Linked List / Two Pointers
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Check if a linked list is a palindrome (reads same forwards and backwards).

Example:
1 -> 2 -> 2 -> 1 -> True
1 -> 2 -> None -> False

Think of it like:
Does the list read the same from both ends?
Like checking if "racecar" is same forwards and backwards!

WHY THIS WORKS (Simple Explanation):
Method 1: Copy to array and check (simple but uses O(n) space)
Method 2: Find middle, reverse second half, compare (O(1) space)

Steps for Method 2:
1. Find middle using fast/slow pointers
2. Reverse second half of list
3. Compare first half with reversed second half

Like folding a paper in half to see if both sides match!

Time Complexity: O(n) - traverse list
Space Complexity: O(1) for method 2
"""

class ListNode:
    """Definition for singly-linked list node"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):
    """
    Check if linked list is palindrome (O(n) space)
    
    Simple approach: Copy values to array, check if palindrome
    
    Example: 1 -> 2 -> 2 -> 1
    
    Copy to array: [1, 2, 2, 1]
    Check: array == array[::-1] -> [1,2,2,1] == [1,2,2,1] -> True
    """
    # Copy values to array
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    
    # Check if palindrome
    return values == values[::-1]


def isPalindrome_optimal(head):
    """
    Optimal solution with O(1) space
    
    Steps:
    1. Find middle of list (fast/slow pointers)
    2. Reverse second half
    3. Compare first half with reversed second half
    
    Example: 1 -> 2 -> 2 -> 1
    
    Step 1: Find middle
      slow will be at second 2
    
    Step 2: Reverse from middle
      First half: 1 -> 2 -> 2
      Second half (reversed): 1 -> 2
    
    Step 3: Compare
      1==1 ✓, 2==2 ✓ -> Palindrome!
    """
    if not head or not head.next:
        return True
    
    # Step 1: Find middle using fast/slow pointers
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse second half
    # slow.next is start of second half
    second_half = reverse_list(slow.next)
    
    # Step 3: Compare first half with reversed second half
    first_half = head
    second_half_copy = second_half  # Save for restoration
    
    is_palindrome = True
    while second_half:
        if first_half.val != second_half.val:
            is_palindrome = False
            break
        first_half = first_half.next
        second_half = second_half.next
    
    # Optional: Restore list to original state
    slow.next = reverse_list(second_half_copy)
    
    return is_palindrome


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


def isPalindrome_verbose(head):
    """
    Detailed version showing the process
    """
    # Convert to list for visualization
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    
    print(f"Linked list values: {values}")
    print(f"Reversed: {values[::-1]}")
    
    is_pal = values == values[::-1]
    
    if is_pal:
        print("✓ It's a palindrome!")
    else:
        print("✗ Not a palindrome")
    
    return is_pal


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
        ([1, 2, 2, 1], True),
        ([1, 2], False),
        ([1], True),
        ([1, 2, 3, 2, 1], True),
        ([1, 2, 3, 4, 5], False),
    ]
    
    print("=== Testing Simple Solution (Array) ===")
    for values, expected in test_cases:
        head = create_linked_list(values)
        result = isPalindrome(head)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {values}")
        print(f"   Is Palindrome: {result} (Expected: {expected})")
        print()
    
    print("=== Testing Optimal Solution (O(1) space) ===")
    for values, expected in test_cases:
        head = create_linked_list(values)
        result = isPalindrome_optimal(head)
        status = "✓" if result == expected else "✗"
        
        # Verify list wasn't corrupted
        final_values = linked_list_to_list(head)
        
        print(f"{status} Input: {values}")
        print(f"   Is Palindrome: {result} (Expected: {expected})")
        print(f"   List after check: {final_values}")
        print()
    
    print("=== Verbose Examples ===")
    head1 = create_linked_list([1, 2, 2, 1])
    isPalindrome_verbose(head1)
    print()
    
    head2 = create_linked_list([1, 2, 3])
    isPalindrome_verbose(head2)

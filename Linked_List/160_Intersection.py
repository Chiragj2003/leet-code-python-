"""
LeetCode #160 - Intersection of Two Linked Lists
Topic: Linked List / Two Pointers
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Find the node where two linked lists intersect (merge together).

Example:
List A: 4 -> 1 -> 8 -> 4 -> 5
List B:      5 -> 0 -> 1 -> 8 -> 4 -> 5
                         ^
                         Intersection at node with value 8

Think of it like:
Two roads that merge into one. Find where they meet!

WHY THIS WORKS (Simple Explanation):
The KEY INSIGHT:
If two pointers traverse both lists, they'll meet at intersection!

Path for pointer A: ListA -> ListB
Path for pointer B: ListB -> ListA

Both paths have SAME LENGTH! So they meet at intersection.

Example:
ListA length = 5, ListB length = 6
A's path: 5 + 6 = 11 steps
B's path: 6 + 5 = 11 steps (same!)

Like two runners on different tracks that meet when they switch!

Time Complexity: O(m + n) - traverse both lists
Space Complexity: O(1) - only two pointers
"""

class ListNode:
    """Definition for singly-linked list node"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getIntersectionNode(headA, headB):
    """
    Find intersection using two pointers
    
    Visual example:
    A: 4 -> 1 -> 8 -> 4 -> 5
    B: 5 -> 0 -> 1 -> 8 -> 4 -> 5
    
    Pointer A path: 4->1->8->4->5->None->5->0->1->8 (meets at 8)
    Pointer B path: 5->0->1->8->4->5->None->4->1->8 (meets at 8)
    
    Both travel same total distance and meet at intersection!
    """
    if not headA or not headB:
        return None
    
    # Two pointers
    pA = headA
    pB = headB
    
    # Traverse until they meet
    # When pointer reaches end, switch to other list
    while pA != pB:
        # Move to next or switch list
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    
    # Either intersection node or None
    return pA


def getIntersectionNode_hashset(headA, headB):
    """
    Alternative: Use hashset to track visited nodes
    
    Simpler but uses O(n) extra space
    
    1. Add all nodes from list A to set
    2. Traverse list B, first node in set is intersection
    """
    visited = set()
    
    # Add all nodes from list A
    current = headA
    while current:
        visited.add(current)
        current = current.next
    
    # Find first node from list B that's in set
    current = headB
    while current:
        if current in visited:
            return current
        current = current.next
    
    return None


def getIntersectionNode_length_diff(headA, headB):
    """
    Alternative: Calculate length difference
    
    1. Find lengths of both lists
    2. Advance longer list by difference
    3. Move both pointers together until they meet
    """
    def get_length(head):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        return length
    
    lenA = get_length(headA)
    lenB = get_length(headB)
    
    # Make A the longer list
    if lenB > lenA:
        headA, headB = headB, headA
        lenA, lenB = lenB, lenA
    
    # Advance longer list by difference
    diff = lenA - lenB
    for _ in range(diff):
        headA = headA.next
    
    # Move both together until they meet
    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next
    
    return None


# Helper functions
def create_intersection_lists(listA_vals, listB_vals, intersect_val):
    """
    Create two lists that intersect at a node with given value
    intersect_val = None means no intersection
    """
    if not listA_vals or not listB_vals:
        return None, None
    
    # Create list A
    headA = ListNode(listA_vals[0])
    currentA = headA
    for val in listA_vals[1:]:
        currentA.next = ListNode(val)
        currentA = currentA.next
    
    # Create list B
    headB = ListNode(listB_vals[0])
    currentB = headB
    for val in listB_vals[1:]:
        currentB.next = ListNode(val)
        currentB = currentB.next
    
    if intersect_val is None:
        return headA, headB
    
    # Find intersection node in A
    intersect_node = headA
    while intersect_node and intersect_node.val != intersect_val:
        intersect_node = intersect_node.next
    
    if intersect_node:
        # Point B's tail to intersection
        currentB.next = intersect_node
    
    return headA, headB


def list_to_values(head, max_nodes=20):
    """Convert linked list to list of values (handle cycles)"""
    values = []
    current = head
    count = 0
    while current and count < max_nodes:
        values.append(current.val)
        current = current.next
        count += 1
    return values


# Test cases
if __name__ == "__main__":
    # Test case 1: Intersection at value 8
    print("=== Test Case 1: Lists with intersection ===")
    headA = ListNode(4)
    headA.next = ListNode(1)
    
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    
    # Common part
    intersection = ListNode(8)
    intersection.next = ListNode(4)
    intersection.next.next = ListNode(5)
    
    headA.next.next = intersection
    headB.next.next.next = intersection
    
    result = getIntersectionNode(headA, headB)
    print(f"List A: {list_to_values(headA)}")
    print(f"List B: {list_to_values(headB)}")
    print(f"Intersection at node with value: {result.val if result else None}")
    print(f"Expected: 8")
    print()
    
    # Test case 2: No intersection
    print("=== Test Case 2: No intersection ===")
    headA2 = ListNode(1)
    headA2.next = ListNode(2)
    headA2.next.next = ListNode(3)
    
    headB2 = ListNode(4)
    headB2.next = ListNode(5)
    
    result2 = getIntersectionNode(headA2, headB2)
    print(f"List A: {list_to_values(headA2)}")
    print(f"List B: {list_to_values(headB2)}")
    print(f"Intersection: {result2}")
    print(f"Expected: None")
    print()
    
    # Test all methods
    print("=== Testing All Methods ===")
    result1 = getIntersectionNode(headA, headB)
    result2 = getIntersectionNode_hashset(headA, headB)
    result3 = getIntersectionNode_length_diff(headA, headB)
    
    print(f"Two-pointer method: {result1.val if result1 else None}")
    print(f"Hashset method: {result2.val if result2 else None}")
    print(f"Length-diff method: {result3.val if result3 else None}")

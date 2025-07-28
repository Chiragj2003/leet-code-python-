"""
LeetCode #2 - Add Two Numbers
Topic: Linked List
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Add two numbers represented as linked lists (reversed).

Example:
2->4->3 (represents 342)
+ 5->6->4 (represents 465)
= 7->0->8 (represents 807)

Think of it like:
Column addition from right to left!

WHY THIS WORKS (Simple Explanation):
Add digit by digit with carry:
- Add values + carry
- New digit = sum % 10
- New carry = sum // 10

Time: O(max(m,n))
Space: O(max(m,n))
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    """Add two numbers as linked lists"""
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10
        
        current.next = ListNode(digit)
        current = current.next
        
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummy.next


# Test
if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    
    result = addTwoNumbers(l1, l2)
    
    vals = []
    while result:
        vals.append(result.val)
        result = result.next
    print(f"Sum: {vals}")  # [7,0,8]

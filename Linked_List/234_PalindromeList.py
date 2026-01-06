"""LeetCode #234 - Palindrome Linked List | LinkedList | Easy"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    """ SIMPLE - Array Copy: O(n) time, O(n) space"""
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next
    return vals == vals[::-1]

def isPalindrome_two_pointer(head):
    """ OPTIMAL - Find Middle, Reverse, Compare: O(n) time, O(1) space"""
    if not head or not head.next: return True
    
    # Find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    second = reverse(slow.next)
    slow.next = None
    
    # Compare
    first = head
    while first and second:
        if first.val != second.val: return False
        first = first.next
        second = second.next
    
    return True

def isPalindrome_stack(head):
    """ SOLUTION 3 - Stack: O(n) time, O(n) space"""
    if not head: return True
    stack = []
    slow = fast = head
    
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    
    # Skip middle for odd length
    if fast: slow = slow.next
    
    while slow:
        if stack.pop() != slow.val: return False
        slow = slow.next
    
    return True

def isPalindrome_recursive(head):
    """ SOLUTION 4 - Recursion: O(n) time, O(n) space"""
    def check(node):
        if not node: return True, head
        is_pal, left = check(node.next)
        if not is_pal: return False, left
        is_equal = (node.val == left.val)
        return is_equal, left.next
    
    result, _ = check(head)
    return result

def reverse(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev

def to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

def from_list(vals):
    if not vals: return None
    head = ListNode(vals[0])
    curr = head
    for val in vals[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

if __name__ == "__main__":
    tests = [([1,2,2,1], True), ([1,2], False), ([1,2,3,2,1], True)]
    print("Testing Palindrome Linked List:")
    for vals, exp in tests:
        r1 = isPalindrome(from_list(vals))
        r2 = isPalindrome_two_pointer(from_list(vals))
        r3 = isPalindrome_stack(from_list(vals))
        r4 = isPalindrome_recursive(from_list(vals))
        print(f"{vals}: Array={r1} TwoPtr={r2} Stack={r3} Rec={r4} (exp={exp})")

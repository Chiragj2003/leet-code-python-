"""LeetCode #19 - Remove Nth Node From End of List | LinkedList | Medium"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    """ OPTIMAL - Two Pointers with Dummy: O(n) time, O(1) space"""
    dummy = ListNode(0)
    dummy.next = head
    slow = fast = dummy
    
    for _ in range(n + 1):
        if not fast: return head
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next
    return dummy.next

def removeNthFromEnd_two_pass(head, n):
    """ SOLUTION 2 - Two Pass: O(n) time, O(1) space"""
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    
    if length == n: return head.next
    
    curr = head
    for _ in range(length - n - 1):
        curr = curr.next
    
    curr.next = curr.next.next
    return head

def removeNthFromEnd_stack(head, n):
    """ SOLUTION 3 - Stack: O(n) time, O(n) space"""
    stack = []
    curr = head
    while curr:
        stack.append(curr)
        curr = curr.next
    
    for _ in range(n):
        stack.pop()
    
    if not stack: return head.next
    stack[-1].next = stack[-1].next.next if stack[-1].next else None
    return head

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
    tests = [([1,2,3,4,5], 2, [1,2,3,5]), ([1], 1, []), ([1,2], 2, [2])]
    print("Testing Remove Nth From End:")
    for vals, n, exp in tests:
        r1 = removeNthFromEnd(from_list(vals), n)
        r2 = removeNthFromEnd_two_pass(from_list(vals), n)
        r3 = removeNthFromEnd_stack(from_list(vals), n)
        r1, r2, r3 = to_list(r1), to_list(r2), to_list(r3)
        print(f"{vals}, n={n}: {r1} {'' if r1==exp else ''}")

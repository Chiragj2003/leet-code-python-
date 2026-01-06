"""LeetCode #143 - Reorder List | LinkedList | Medium"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    """ OPTIMAL - Find Middle, Reverse, Merge: O(n) time, O(1) space"""
    if not head or not head.next: return
    
    # Step 1: Find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse second half
    second = reverse(slow.next)
    slow.next = None
    
    # Step 3: Merge  
    first = head
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2

def reorderList_stack(head):
    """ SOLUTION 2 - Stack: O(n) time, O(n) space"""
    if not head: return
    stack = []
    curr = head
    while curr:
        stack.append(curr)
        curr = curr.next
    
    curr = head
    while len(stack) > 1:
        tail = stack.pop()
        next_node = curr.next
        curr.next = tail
        tail.next = next_node
        curr = next_node

def reorderList_recursive(head):
    """ SOLUTION 3 - Recursive: O(n) time, O(n) space"""
    def reorder(node, n):
        if n == 1: return node
        if n == 2: return node.next
        next_node = reorder(node.next, n - 2)
        if next_node: 
            tmp = next_node.next
            next_node.next = node.next
            node.next = next_node
            return tmp
        return None
    
    if not head: return
    curr = head
    n = 0
    while curr:
        n += 1
        curr = curr.next
    reorder(head, n)

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
    tests = [[1,2,3,4],[1,2,3,4,5]]
    print("Testing Reorder List:")
    for vals in tests:
        head = from_list(vals[:])
        reorderList(head)
        print(f"{vals} -> {to_list(head)}")

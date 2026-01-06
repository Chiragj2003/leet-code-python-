"""LeetCode #160 - Intersection of Two Linked Lists | LinkedList | Easy"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersectionNode(headA, headB):
    """ OPTIMAL - Two Pointers: O(m+n) time, O(1) space"""
    if not headA or not headB: return None
    pA, pB = headA, headB
    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    return pA

def getIntersectionNode_hashset(headA, headB):
    """ SOLUTION 2 - HashSet: O(m+n) time, O(m) or O(n) space"""
    visited = set()
    curr = headA
    while curr:
        visited.add(curr)
        curr = curr.next
    curr = headB
    while curr:
        if curr in visited: return curr
        curr = curr.next
    return None

def getIntersectionNode_length(headA, headB):
    """ SOLUTION 3 - Length Diff: O(m+n) time, O(1) space"""
    def get_length(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    lenA, lenB = get_length(headA), get_length(headB)
    long, short = (headA, headB) if lenA > lenB else (headB, headA)
    
    for _ in range(abs(lenA - lenB)):
        long = long.next
    
    while long and short:
        if long == short: return long
        long, short = long.next, short.next
    return None

def from_list(vals):
    if not vals: return None
    head = ListNode(vals[0])
    curr = head
    for val in vals[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

if __name__ == "__main__":
    print("Testing Intersection of Two Linked Lists:")
    # Create lists with intersection at node 8
    headA = from_list([4,1,8,4,5])
    headB = from_list([5,6,1])
    # Manually connect to same intersection node
    headA.next.next.next = ListNode(4)
    headA.next.next.next.next = ListNode(5)
    headB.next.next = headA.next.next
    
    r1 = getIntersectionNode(headA, headB)
    r2 = getIntersectionNode_hashset(headA, headB)
    r3 = getIntersectionNode_length(headA, headB)
    print(f"Two Pointers: {r1.val if r1 else None}")
    print(f"HashSet: {r2.val if r2 else None}")
    print(f"Length Diff: {r3.val if r3 else None}")

"""
LeetCode #2 - Add Two Numbers | ENHANCED SOLUTION
Topic: Linked List | Difficulty: Medium

PROBLEM STATEMENT:
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in REVERSE ORDER, and each node contains a SINGLE DIGIT. 
Add the two numbers and return the sum as a linked list (also in reverse order).

EXAMPLES:
  Input:  l1 = 2→4→3, l2 = 5→6→4
  Output: 7→0→8
  Explanation: 342 + 465 = 807
  
  Input:  l1 = 0, l2 = 0
  Output: 0
  
  Input:  l1 = 9→9→9→9→9→9→9, l2 = 9→9→9→9
  Output: 8→9→9→9→0→0→0→1
  Explanation: 9999999 + 9999 = 10009998

KEY INSIGHTS:
- Numbers are stored in REVERSE order (easy for addition!)
- Addition happens digit by digit with carry
- Both lists might have different lengths
- Need to handle carry at the end
- Result list length = max(len(l1), len(l2)) or +1 if final carry

WHY REVERSE ORDER?
- Normal number: 342 = [3,4,2] (significant digits first)
- Reverse: 342 = [2,4,3] (least significant first)
- This is PERFECT for linked list addition (we naturally traverse left to right)
- No need to reverse before/after!

ALGORITHM:
1. Create dummy node
2. Initialize carry = 0
3. While at least one list or carry exists:
   - Get values from l1 and l2 (0 if list is empty/None)
   - Calculate sum = val1 + val2 + carry
   - New digit = sum % 10
   - New carry = sum // 10
   - Create new node with digit
   - Move pointers forward
4. Return dummy.next (skip dummy)

COMPLEXITY:
Time:  O(max(m, n)) where m, n = lengths of lists
Space: O(max(m, n)) for result list (not counting output)

EDGE CASES:
- Different length lists → handle with 0 values
- Final carry → create extra node
- All zeros → works
- Very large numbers → works
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ★ STANDARD SOLUTION - Iterative with Carry
def addTwoNumbers(l1, l2):
    """
    Add two linked list numbers (in reverse order).
    
    Algorithm:
    1. Create dummy node for simplified code
    2. Track carry across digits
    3. Process both lists simultaneously
    4. Handle different lengths with 0 padding
    5. Don't forget final carry!
    
    Step-by-step for 342 + 465:
    
    l1: 2→4→3 (342 in reverse)
    l2: 5→6→4 (465 in reverse)
    
    Step 1: 2 + 5 = 7 (sum=7, carry=0, digit=7)
    Result: 7
    
    Step 2: 4 + 6 = 10 (sum=10, carry=1, digit=0)
    Result: 7→0
    
    Step 3: 3 + 4 + 1(carry) = 8 (sum=8, carry=0, digit=8)
    Result: 7→0→8
    
    Time: O(max(m,n)) | Space: O(max(m,n)) for result
    """
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        # Get values (0 if node doesn't exist)
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Add with carry
        total = val1 + val2 + carry
        
        # Extract digit and new carry
        carry = total // 10
        digit = total % 10
        
        # Create node for this digit
        current.next = ListNode(digit)
        current = current.next
        
        # Move to next nodes
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummy.next


# ★ RECURSIVE SOLUTION - Elegant
def addTwoNumbers_recursive(l1, l2, carry=0):
    """
    Add two numbers recursively.
    
    Base case:
    - Both lists empty AND no carry → return None
    
    Recursive case:
    - Calculate sum for current digits
    - Recursively add rest of lists
    
    Advantage: Cleaner code, no dummy node needed
    Disadvantage: Uses call stack space
    
    Time: O(max(m,n)) | Space: O(max(m,n)) call stack
    """
    if not l1 and not l2 and carry == 0:
        return None
    
    val1 = l1.val if l1 else 0
    val2 = l2.val if l2 else 0
    
    total = val1 + val2 + carry
    new_carry = total // 10
    digit = total % 10
    
    node = ListNode(digit)
    node.next = addTwoNumbers_recursive(
        l1.next if l1 else None,
        l2.next if l2 else None,
        new_carry
    )
    
    return node


# ★ VERBOSE SOLUTION - Shows calculation steps
def addTwoNumbers_verbose(l1, l2):
    """
    Add numbers with detailed output showing carry propagation.
    """
    def list_to_number(node):
        digits = []
        while node:
            digits.append(str(node.val))
            node = node.next
        return ''.join(reversed(digits))
    
    print(f"Number 1: {list_to_number(l1)}")
    print(f"Number 2: {list_to_number(l2)}")
    print()
    
    dummy = ListNode(0)
    current = dummy
    carry = 0
    step = 0
    
    while l1 or l2 or carry:
        step += 1
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10
        
        print(f"Step {step}: {val1} + {val2} + {total-val1-val2 if total-val1-val2 > 0 else 0}(carry) = {total}")
        print(f"  → Digit: {digit}, New carry: {carry}")
        
        current.next = ListNode(digit)
        current = current.next
        
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    print()
    result = dummy.next
    print(f"Result: {list_to_number(result)}")
    return result


# COMPREHENSIVE TEST CASES
if __name__ == "__main__":
    def list_to_vals(node):
        vals = []
        while node:
            vals.append(node.val)
            node = node.next
        return vals
    
    def create_list(vals):
        if not vals:
            return None
        head = ListNode(vals[0])
        curr = head
        for val in vals[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head
    
    print("="*70)
    print("LeetCode #2 - Add Two Numbers (Complete Solutions)")
    print("="*70)
    
    # Test 1: Standard addition
    print("\n✓ Test 1: 342 + 465 = 807")
    l1 = create_list([2, 4, 3])
    l2 = create_list([5, 6, 4])
    result = addTwoNumbers(l1, l2)
    print(f"  Iterative: {list_to_vals(result)}")
    
    # Test 2: Both zeros
    print("\n✓ Test 2: 0 + 0 = 0")
    l1 = create_list([0])
    l2 = create_list([0])
    result = addTwoNumbers(l1, l2)
    print(f"  Iterative: {list_to_vals(result)}")
    
    # Test 3: Carry propagation
    print("\n✓ Test 3: 9999999 + 9999 = 10009998")
    l1 = create_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_list([9, 9, 9, 9])
    result = addTwoNumbers(l1, l2)
    print(f"  Iterative: {list_to_vals(result)}")
    
    # Test 4: Recursive solution
    print("\n✓ Test 4: Recursive 342 + 465")
    l1 = create_list([2, 4, 3])
    l2 = create_list([5, 6, 4])
    result = addTwoNumbers_recursive(l1, l2)
    print(f"  Recursive: {list_to_vals(result)}")
    
    # Test 5: Verbose walkthrough
    print("\n✓ Test 5: Verbose walkthrough")
    l1 = create_list([2, 4, 3])
    l2 = create_list([5, 6, 4])
    addTwoNumbers_verbose(l1, l2)
    
    # Additional tests
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    
    result = addTwoNumbers(l1, l2)
    
    vals = []
    while result:
        vals.append(result.val)
        result = result.next
    print(f"Sum: {vals}")  # [7,0,8]

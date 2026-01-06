"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #371 - Sum of Two Integers                        ║
║                    Topic: Bit Manipulation                                   ║
║                    Difficulty: Medium                                         ║
║                    Company: Amazon, Meta, Apple                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Add two integers WITHOUT using + or - operators.

EXAMPLES:
─────────
✓ Input: a = 1, b = 2 → Output: 3
✓ Input: a = 2, b = 3 → Output: 5
✓ Input: a = -1, b = 1 → Output: 0

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🧮 Adding with XOR and AND:
   Think of addition in two parts:
   1. Sum without carry: XOR (^)
   2. Carry: AND (&) then shift left

   Example: 5 + 3
   5:  101
   3:  011
   ───────
   XOR: 110 (sum without carry)
   AND: 001 (where carry happens)
   Shift carry left: 010
   
   Now add 110 + 010 (repeat process)

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   Amazon hardware interface: implement addition at bit level
   for custom processor without ALU support.

📌 TASK:
   Add two integers using only bit operations.
   Time O(1), Space O(1).

📌 ACTION:
   Bit manipulation:
   1. XOR for sum without carry
   2. AND for carry positions
   3. Shift carry left
   4. Repeat until no carry

📌 RESULT:
   ✓ Time: O(1) - fixed iterations
   ✓ Space: O(1) - constant variables
   ✓ Addition without + operator

"""

# ═══════════════════════════════════════════════════════════════════════════
# 💡 BRUTE FORCE - Using Built-in
# ═══════════════════════════════════════════════════════════════════════════
def getSum_builtin(a, b):
    """
    This is what we're NOT allowed to do!
    
    Time: O(1)
    Space: O(1)
    """
    return a + b  # Not allowed!


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Bit Manipulation
# ═══════════════════════════════════════════════════════════════════════════
def getSum(a, b):
    """
    Add using XOR and AND
    
    Key concepts:
    - a ^ b gives sum without carry
    - (a & b) << 1 gives carry
    - Repeat until carry is 0
    
    Example: 5 + 3 = 8
    ────────
    Step 1:
      a = 5 (101), b = 3 (011)
      sum = 5 ^ 3 = 110 (6)
      carry = (5 & 3) << 1 = 001 << 1 = 010 (2)
    
    Step 2:
      a = 6 (110), b = 2 (010)
      sum = 6 ^ 2 = 100 (4)
      carry = (6 & 2) << 1 = 010 << 1 = 100 (4)
    
    Step 3:
      a = 4 (100), b = 4 (100)
      sum = 4 ^ 4 = 000 (0)
      carry = (4 & 4) << 1 = 100 << 1 = 1000 (8)
    
    Step 4:
      a = 0, b = 8
      sum = 0 ^ 8 = 8
      carry = (0 & 8) << 1 = 0
    
    Done! Result = 8
    """
    # Mask to handle 32-bit integers
    MASK = 0xFFFFFFFF
    
    while b != 0:
        # Sum without carry
        sum_without_carry = (a ^ b) & MASK
        # Carry
        carry = ((a & b) << 1) & MASK
        
        a = sum_without_carry
        b = carry
    
    # Handle negative numbers (if a is negative in 32-bit)
    if a > 0x7FFFFFFF:
        return ~(a ^ MASK)
    
    return a


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE - Recursive
# ═══════════════════════════════════════════════════════════════════════════
def getSum_recursive(a, b):
    """
    Recursive version
    
    Time: O(1) - limited recursion depth
    Space: O(1) - recursion stack
    """
    MASK = 0xFFFFFFFF
    
    if b == 0:
        # Handle negative
        if a > 0x7FFFFFFF:
            return ~(a ^ MASK)
        return a
    
    # Sum without carry
    sum_without_carry = (a ^ b) & MASK
    # Carry
    carry = ((a & b) << 1) & MASK
    
    return getSum_recursive(sum_without_carry, carry)


# ═══════════════════════════════════════════════════════════════════════════
# 📊 COMPLEXITY COMPARISON
# ═══════════════════════════════════════════════════════════════════════════
"""
╔════════════════╦════════════╦═══════════╦═════════════════════════╗
║   Approach     ║    Time    ║   Space   ║       Notes             ║
╠════════════════╬════════════╬═══════════╬═════════════════════════╣
║ Built-in (+)   ║   O(1)     ║   O(1)    ║ Not allowed!            ║
║ Iterative      ║   O(1)     ║   O(1)    ║ Standard solution       ║
║ Recursive      ║   O(1)     ║   O(1)    ║ Elegant but stack used  ║
╚════════════════╩════════════╩═══════════╩═════════════════════════╝

Note: O(1) because limited to 32-bit integers (max ~32 iterations)
"""


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [
        (1, 2, 3),
        (2, 3, 5),
        (-1, 1, 0),
        (5, 3, 8),
        (0, 0, 0),
    ]
    
    print("=" * 70)
    print("🧪 TESTING SUM OF TWO INTEGERS")
    print("=" * 70)
    
    for a, b, expected in test_cases:
        optimal = getSum(a, b)
        recursive = getSum_recursive(a, b)
        
        print(f"\nInput: a = {a}, b = {b}")
        print(f"Expected: {expected}")
        print(f"Iterative: {optimal} {'✓' if optimal == expected else '✗'}")
        print(f"Recursive: {recursive} {'✓' if recursive == expected else '✗'}")
        print(f"Binary: {a} = {bin(a & 0xFFFFFFFF)}, {b} = {bin(b & 0xFFFFFFFF)}")

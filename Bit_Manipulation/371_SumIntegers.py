"""
LeetCode #371 - Sum of Two Integers
Topic: Bit Manipulation
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Add two integers WITHOUT using + or - operators!

Example:
1 + 2 = 3
-2 + 3 = 1

Think of it like:
Binary addition using bitwise operations!

WHY THIS WORKS:
XOR gives sum without carry.
AND + left shift gives carry.
Repeat until no carry!

Time: O(1)
Space: O(1)
"""

def getSum(a, b):
    """Add two integers without +/-"""
    # Mask to get 32-bit integer
    mask = 0xFFFFFFFF
    
    while b != 0:
        # Calculate sum without carry (XOR)
        temp_sum = (a ^ b) & mask
        
        # Calculate carry (AND + left shift)
        carry = ((a & b) << 1) & mask
        
        a = temp_sum
        b = carry
    
    # Handle negative numbers
    return a if a <= 0x7FFFFFFF else ~(a ^ mask)


# Test
if __name__ == "__main__":
    tests = [
        (1, 2, 3),
        (2, 3, 5),
        (-1, 1, 0),
    ]
    
    for a, b, exp in tests:
        result = getSum(a, b)
        print(f"{a} + {b} = {result} (expected {exp})")

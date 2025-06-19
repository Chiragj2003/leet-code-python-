"""
LeetCode #190 - Reverse Bits
Topic: Bit Manipulation
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Reverse bits of 32-bit unsigned integer.

Example:
00000010100101000001111010011100 -> 
00111001011110000010100101000000

Think of it like:
Flipping binary number backwards!

WHY THIS WORKS:
Build result bit by bit from right to left.

Time: O(1) - fixed 32 bits
Space: O(1)
"""

def reverseBits(n):
    """Reverse bits of 32-bit integer"""
    result = 0
    
    for i in range(32):
        # Shift result left and add rightmost bit of n
        result = (result << 1) | (n & 1)
        # Shift n right
        n >>= 1
    
    return result


# Test
if __name__ == "__main__":
    n = 0b00000010100101000001111010011100
    result = reverseBits(n)
    print(f"Reversed: {bin(result)}")

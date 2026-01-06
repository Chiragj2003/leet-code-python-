"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #190 - Reverse Bits                               ║
║                    Topic: Bit Manipulation                                   ║
║                    Difficulty: Easy                                           ║
║                    Company: Amazon, Apple, Airbnb                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Reverse bits of a 32-bit unsigned integer.

EXAMPLES:
─────────
✓ Input:  00000010100101000001111010011100 (43261596 in decimal)
  Output: 00111001011110000010100101000000 (964176192 in decimal)

✓ Input:  11111111111111111111111111111101 (4294967293 in decimal)
  Output: 10111111111111111111111111111111 (3221225471 in decimal)

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🎨 String of beads: You have 32 beads (white=0, black=1).
   Flip the string backwards!
   
   Original: ⚪⚫⚫⚪⚫
   Reversed: ⚫⚪⚫⚫⚪

🔢 Number palindrome: Read number backwards in binary!

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   Amazon networking: reverse bit order for endianness conversion
   between different system architectures.

📌 TASK:
   Reverse all 32 bits of unsigned integer.
   Time O(1), Space O(1).

📌 ACTION:
   Bit manipulation:
   1. Extract rightmost bit of input
   2. Shift result left, add bit
   3. Shift input right
   4. Repeat 32 times

📌 RESULT:
   ✓ Time: O(1) - always 32 iterations
   ✓ Space: O(1) - constant variables
   ✓ Efficient bit reversal

"""

# ═══════════════════════════════════════════════════════════════════════════
# 💡 BRUTE FORCE - String Conversion
# ═══════════════════════════════════════════════════════════════════════════
def reverseBits_bruteforce(n):
    """
    Convert to binary string, reverse, convert back
    
    Time: O(1) - 32 bits fixed
    Space: O(1) - string of 32 chars
    """
    # Convert to 32-bit binary string
    binary = bin(n)[2:].zfill(32)
    # Reverse the string
    reversed_binary = binary[::-1]
    # Convert back to integer
    return int(reversed_binary, 2)


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Bit Shifting
# ═══════════════════════════════════════════════════════════════════════════
def reverseBits(n):
    """
    Bit-by-bit reversal using shifts
    
    Example: n = 00000000000000000000000000001101 (13 in decimal)
    ────────
    Iteration 1:
      n & 1 = 1 (rightmost bit)
      result = 0 << 1 | 1 = 1
      n >> 1 = 00000000000000000000000000000110
    
    Iteration 2:
      n & 1 = 0
      result = 1 << 1 | 0 = 10
      n >> 1 = 00000000000000000000000000000011
    
    Iteration 3:
      n & 1 = 1
      result = 10 << 1 | 1 = 101
      n >> 1 = 00000000000000000000000000000001
    
    Iteration 4:
      n & 1 = 1
      result = 101 << 1 | 1 = 1011
      n >> 1 = 00000000000000000000000000000000
    
    Continue 28 more iterations...
    Final: 10110000000000000000000000000000
    """
    result = 0
    
    for i in range(32):
        # Shift result left to make room
        result <<= 1
        # Add rightmost bit of n
        result |= (n & 1)
        # Shift n right to process next bit
        n >>= 1
    
    return result


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE - Divide and Conquer
# ═══════════════════════════════════════════════════════════════════════════
def reverseBits_divideconquer(n):
    """
    Divide and conquer: swap adjacent bits, then pairs, then quads...
    
    Time: O(1)
    Space: O(1)
    """
    # Swap every adjacent bit
    n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)
    # Swap every 2 bits
    n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)
    # Swap every 4 bits
    n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)
    # Swap every 8 bits
    n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)
    # Swap every 16 bits
    n = (n >> 16) | (n << 16)
    
    return n


# ═══════════════════════════════════════════════════════════════════════════
# 📊 COMPLEXITY COMPARISON
# ═══════════════════════════════════════════════════════════════════════════
"""
╔════════════════╦════════════╦═══════════╦═════════════════════════╗
║   Approach     ║    Time    ║   Space   ║       Notes             ║
╠════════════════╬════════════╬═══════════╬═════════════════════════╣
║ Brute Force    ║   O(1)     ║   O(1)    ║ String operations       ║
║ Bit Shifting   ║   O(1)     ║   O(1)    ║ Clean and efficient     ║
║ Divide/Conquer ║   O(1)     ║   O(1)    ║ Fastest (5 operations)  ║
╚════════════════╩════════════╩═══════════╩═════════════════════════╝
"""


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [
        (0b00000010100101000001111010011100, 0b00111001011110000010100101000000),
        (0b11111111111111111111111111111101, 0b10111111111111111111111111111111),
        (0b00000000000000000000000000001101, 0b10110000000000000000000000000000),
    ]
    
    print("=" * 70)
    print("🧪 TESTING REVERSE BITS")
    print("=" * 70)
    
    for n, expected in test_cases:
        brute = reverseBits_bruteforce(n)
        optimal = reverseBits(n)
        divide = reverseBits_divideconquer(n)
        
        print(f"\nInput:  {bin(n)}")
        print(f"Expected: {bin(expected)}")
        print(f"Brute: {bin(brute)} {'✓' if brute == expected else '✗'}")
        print(f"Optimal: {bin(optimal)} {'✓' if optimal == expected else '✗'}")
        print(f"D&C: {bin(divide)} {'✓' if divide == expected else '✗'}")

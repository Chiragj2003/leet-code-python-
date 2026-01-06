╔══════════════════════════════════════════════════════════════════════════════╗
║                   ⚡ BIT MANIPULATION PROBLEMS - README                       ║
║                   Amazon Interview Preparation Guide                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

🎯 WHAT IS BIT MANIPULATION?
═══════════════════════════════════════════════════════════════════════════════
Working with individual bits (0s and 1s) of numbers.
Lightning fast operations at the hardware level!

Key Operations:
- AND (&): Both bits must be 1
- OR (|): At least one bit is 1
- XOR (^): Bits are different
- NOT (~): Flip all bits
- Left Shift (<<): Multiply by 2
- Right Shift (>>): Divide by 2

📋 PROBLEM LIST (3 Problems)
═══════════════════════════════════════════════════════════════════════════════

EASY:
─────
1. ✅ 190_ReverseBits.py        - Reverse 32-bit integer
2. ✅ 338_CountingBits.py       - Count 1's for 0 to n

MEDIUM:
───────
3. ✅ 371_SumIntegers.py        - Add without + operator

🔑 KEY PATTERNS & TRICKS
═══════════════════════════════════════════════════════════════════════════════

PATTERN 1: XOR PROPERTIES
──────────────────────────
• x ^ 0 = x (identity)
• x ^ x = 0 (self-cancel)
• x ^ y ^ x = y (find unique)

Use cases:
- Find single number in pairs
- Swap without temp variable
- Check if numbers are different

PATTERN 2: AND TRICKS
──────────────────────
• x & 1 → Get rightmost bit
• x & (x-1) → Remove rightmost 1
• x & -x → Get rightmost 1 bit only

Use cases:
- Check if odd/even
- Count set bits
- Check power of 2

PATTERN 3: SHIFT OPERATIONS
────────────────────────────
• x << 1 → Multiply by 2
• x >> 1 → Divide by 2
• x << n → Multiply by 2^n

Use cases:
- Fast multiplication/division
- Access specific bits
- Build numbers bit by bit

PATTERN 4: COMMON CHECKS
─────────────────────────
```python
# Check if power of 2
x > 0 and (x & (x - 1)) == 0

# Count set bits (Hamming weight)
count = 0
while n:
    count += n & 1
    n >>= 1

# Check if bit i is set
(n & (1 << i)) != 0

# Set bit i
n |= (1 << i)

# Clear bit i
n &= ~(1 << i)

# Toggle bit i
n ^= (1 << i)
```

⚡ COMPLEXITY GUIDE
═══════════════════════════════════════════════════════════════════════════════

Problem                  Time                Space       Key Technique
───────────────────────  ──────────────────  ──────────  ────────────────
190. Reverse Bits        O(1)                O(1)        Bit shifting
338. Counting Bits       O(n)                O(n)        DP with bits
371. Sum Integers        O(1)                O(1)        XOR + AND

Note: O(1) for bit operations means fixed 32/64 bits

🎓 STUDY PLAN
═══════════════════════════════════════════════════════════════════════════════

DAY 1: Fundamentals
───────────────────
□ Learn basic bit operations (&, |, ^, ~, <<, >>)
□ Practice: 338_CountingBits (DP + bits combo)

DAY 2: Bit Tricks
─────────────────
□ 190_ReverseBits (bit manipulation)
□ 371_SumIntegers (XOR magic for addition)

🔥 COMMON BIT TRICKS
═══════════════════════════════════════════════════════════════════════════════

1. Swap two numbers without temp:
   ```python
   a ^= b
   b ^= a
   c ^= b
   ```

2. Check if two numbers have opposite signs:
   ```python
   (x ^ y) < 0
   ```

3. Find position of rightmost set bit:
   ```python
   position = (n & -n).bit_length() - 1
   ```

4. Turn off rightmost 1-bit:
   ```python
   n &= (n - 1)
   ```

5. Isolate rightmost 1-bit:
   ```python
   n & -n
   ```

6. Right propagate rightmost 1-bit:
   ```python
   n | (n - 1)
   ```

💡 AMAZON INTERVIEW TIPS
═══════════════════════════════════════════════════════════════════════════════

1. ALWAYS explain bit operations clearly
2. Draw binary representations on whiteboard
3. Mention O(1) time for bit operations
4. Explain how bits represent numbers
5. Show step-by-step bit transformations

Example explanation:
"I'll use XOR because it has a useful property: any number XOR itself is 0,
and any number XOR 0 is itself. This means if we XOR all numbers together,
pairs will cancel out, leaving only the unique number."

📖 QUICK REFERENCE
═══════════════════════════════════════════════════════════════════════════════

Operator | Name            | Example      | Result
─────────|─────────────────|──────────────|─────────
&        | AND             | 5 & 3        | 1 (101 & 011 = 001)
|        | OR              | 5 | 3        | 7 (101 | 011 = 111)
^        | XOR             | 5 ^ 3        | 6 (101 ^ 011 = 110)
~        | NOT             | ~5           | -6 (invert all bits)
<<       | Left Shift      | 5 << 1       | 10 (101 → 1010)
>>       | Right Shift     | 5 >> 1       | 2 (101 → 10)

Common Bit Masks:
0x1        = 0b00000001  (check last bit)
0xFFFFFFFF = 0b11111111... (32-bit mask)
0x55555555 = 0b01010101... (alternating bits)
0xAAAAAAAA = 0b10101010... (alternating bits)

🎯 WHEN TO USE BIT MANIPULATION
═══════════════════════════════════════════════════════════════════════════════

Strong Indicators:
✓ Problem mentions "bits" or "binary"
✓ Need O(1) space and time
✓ Working with powers of 2
✓ Find unique/missing numbers
✓ Optimize space (bit flags)

Not Suitable:
✗ Complex business logic
✗ Need floating point
✗ Human-readable code priority

═══════════════════════════════════════════════════════════════════════════════
✨ ALL PROBLEMS HAVE:
   • Child-friendly explanation (even kids can grasp!)
   • Amazon STAR format answer
   • Brute force approach
   • Optimal bit manipulation solution
   • Alternative methods
   • Step-by-step bit traces
   • Comprehensive test cases

🎯 Good luck with your Amazon interviews!
═══════════════════════════════════════════════════════════════════════════════

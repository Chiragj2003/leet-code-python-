"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #338 - Counting Bits                              ║
║                    Topic: Bit Manipulation / Dynamic Programming             ║
║                    Difficulty: Easy                                           ║
║                    Company: Amazon, Meta, Apple                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Given integer n, return array of length n+1 where ans[i] is
the number of 1's in binary representation of i.

EXAMPLES:
─────────
✓ Input: n = 2
  Output: [0,1,1]
  Explanation: 
    0 → 0 (zero 1's)
    1 → 1 (one 1)
    2 → 10 (one 1)

✓ Input: n = 5
  Output: [0,1,1,2,1,2]
  Explanation:
    0 → 0   (zero 1's)
    1 → 1   (one 1)
    2 → 10  (one 1)
    3 → 11  (two 1's)
    4 → 100 (one 1)
    5 → 101 (two 1's)

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🔢 Counting lights: How many lights are ON (1) for each number?
   0: ⚪ → 0 lights
   1: ⚫ → 1 light
   2: ⚫⚪ → 1 light
   3: ⚫⚫ → 2 lights

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   Amazon metrics: count active features (1 bits) for
   configuration flags 0 to n.

📌 TASK:
   Count 1's in binary for all numbers 0 to n.
   Time O(n), Space O(n).

📌 ACTION:
   Dynamic programming with bit trick:
   - bits[i] = bits[i >> 1] + (i & 1)
   - Reuse previous results

📌 RESULT:
   ✓ Time: O(n) single pass
   ✓ Space: O(n) for output
   ✓ Efficient bit counting

"""

# ═══════════════════════════════════════════════════════════════════════════
# 💡 BRUTE FORCE - Count Each Number
# ═══════════════════════════════════════════════════════════════════════════
def countBits_bruteforce(n):
    """
    Count 1's for each number individually
    
    Time: O(n × log n) - n numbers, log n bits each
    Space: O(n) for output
    """
    result = []
    
    for i in range(n + 1):
        count = 0
        num = i
        # Count 1's in binary
        while num:
            count += num & 1
            num >>= 1
        result.append(count)
    
    return result


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Dynamic Programming
# ═══════════════════════════════════════════════════════════════════════════
def countBits(n):
    """
    DP: Reuse previous results
    
    Key insight: bits[i] = bits[i >> 1] + (i & 1)
    
    Explanation:
    - i >> 1 removes rightmost bit
    - i & 1 gets rightmost bit
    - If we know count for i>>1, just add rightmost bit!
    
    Example: n = 5
    ────────
    i=0: 0   → bits[0] = 0
    i=1: 1   → bits[0>>1] + (1&1) = 0 + 1 = 1
    i=2: 10  → bits[1>>1] + (2&1) = bits[1] + 0 = 1 + 0 = 1
    i=3: 11  → bits[1>>1] + (3&1) = bits[1] + 1 = 1 + 1 = 2
    i=4: 100 → bits[2>>1] + (4&1) = bits[2] + 0 = 1 + 0 = 1
    i=5: 101 → bits[2>>1] + (5&1) = bits[2] + 1 = 1 + 1 = 2
    
    Result: [0,1,1,2,1,2]
    """
    result = [0] * (n + 1)
    
    for i in range(1, n + 1):
        # Count = count of (i >> 1) + rightmost bit
        result[i] = result[i >> 1] + (i & 1)
    
    return result


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE - Last Set Bit
# ═══════════════════════════════════════════════════════════════════════════
def countBits_lastbit(n):
    """
    DP using i & (i-1) trick
    
    Key: i & (i-1) removes rightmost 1
    So: bits[i] = bits[i & (i-1)] + 1
    
    Time: O(n)
    Space: O(n)
    """
    result = [0] * (n + 1)
    
    for i in range(1, n + 1):
        # Remove last set bit, add 1
        result[i] = result[i & (i - 1)] + 1
    
    return result


# ═══════════════════════════════════════════════════════════════════════════
# 🎯 ALTERNATIVE - Popcount (Built-in)
# ═══════════════════════════════════════════════════════════════════════════
def countBits_popcount(n):
    """
    Using Python's built-in bit_count (Python 3.10+)
    
    Time: O(n)
    Space: O(n)
    """
    return [bin(i).count('1') for i in range(n + 1)]


# ═══════════════════════════════════════════════════════════════════════════
# 📊 COMPLEXITY COMPARISON
# ═══════════════════════════════════════════════════════════════════════════
"""
╔════════════════╦════════════╦═══════════╦═════════════════════════╗
║   Approach     ║    Time    ║   Space   ║       Notes             ║
╠════════════════╬════════════╬═══════════╬═════════════════════════╣
║ Brute Force    ║ O(n log n) ║   O(n)    ║ Count each separately   ║
║ DP (Right Shift)║   O(n)    ║   O(n)    ║ Optimal, clean          ║
║ DP (Last Bit)  ║   O(n)    ║   O(n)    ║ Alternative DP          ║
║ Popcount       ║   O(n)    ║   O(n)    ║ Concise, built-in       ║
╚════════════════╩════════════╩═══════════╩═════════════════════════╝
"""


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2]),
        (0, [0]),
    ]
    
    print("=" * 70)
    print("🧪 TESTING COUNTING BITS")
    print("=" * 70)
    
    for n, expected in test_cases:
        brute = countBits_bruteforce(n)
        optimal = countBits(n)
        lastbit = countBits_lastbit(n)
        popcount = countBits_popcount(n)
        
        print(f"\nInput: n = {n}")
        print(f"Expected: {expected}")
        print(f"Brute: {brute} {'✓' if brute == expected else '✗'}")
        print(f"DP (Shift): {optimal} {'✓' if optimal == expected else '✗'}")
        print(f"DP (Last): {lastbit} {'✓' if lastbit == expected else '✗'}")
        print(f"Popcount: {popcount} {'✓' if popcount == expected else '✗'}")

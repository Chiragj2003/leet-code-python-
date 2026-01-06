"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #69 - Sqrt(x)                                     ║
║                    Topic: Binary Search                                      ║
║                    Difficulty: Easy                                           ║
║                    Company: Amazon, Bloomberg, Adobe                         ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Compute and return the square root of x (rounded down to nearest integer).

EXAMPLES:
─────────
✓ Input: x = 4 → Output: 2
✓ Input: x = 8 → Output: 2 (√8 ≈ 2.828, rounded down)
✓ Input: x = 1 → Output: 1

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🔢 Number game: What number times itself equals (or is close to) x?
   8: Try 3×3=9 (too big), 2×2=4 (good!), answer is 2.

📦 Square tiles: You have 8 tiles. What's biggest square you can make?
   2×2 = 4 tiles used. Answer: 2.

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   Amazon graphics: Calculate image dimensions. Need integer
   square root without using built-in functions.

📌 TASK:
   Compute floor(√x) without math.sqrt().
   Time O(log x), Space O(1).

📌 ACTION:
   Binary search on answer range [0, x]:
   1. Try mid as answer
   2. Check if mid*mid ≤ x
   3. Narrow search range

📌 RESULT:
   ✓ Time: O(log x) binary search
   ✓ Space: O(1) constant
   ✓ Accurate integer sqrt

"""

# ═══════════════════════════════════════════════════════════════════════════
# 💡 BRUTE FORCE - Linear Search
# ═══════════════════════════════════════════════════════════════════════════
def mySqrt_bruteforce(x):
    """
    Try every number from 0 to x
    
    Time: O(√x) - check up to sqrt(x)
    Space: O(1)
    """
    if x < 2:
        return x
    
    for i in range(x):
        if i * i > x:
            return i - 1
    
    return x


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Binary Search
# ═══════════════════════════════════════════════════════════════════════════
def mySqrt(x):
    """
    Binary search for sqrt
    
    Search range: [0, x]
    
    Example: x = 8
    ────────
    left=0, right=8, mid=4
    4*4=16 > 8 → Too big, search left
    
    left=0, right=3, mid=1
    1*1=1 < 8 → Too small, search right
    
    left=2, right=3, mid=2
    2*2=4 < 8 → Too small, search right
    
    left=3, right=3, mid=3
    3*3=9 > 8 → Too big, search left
    
    left=3, right=2 → Done! Return 2
    """
    if x < 2:
        return x
    
    left, right = 0, x
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right  # Return floor value


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE - Newton's Method
# ═══════════════════════════════════════════════════════════════════════════
def mySqrt_newton(x):
    """
    Newton-Raphson method for faster convergence
    
    Formula: x_new = (x_old + n/x_old) / 2
    
    Time: O(log x)
    Space: O(1)
    """
    if x < 2:
        return x
    
    # Start with x/2 as guess
    guess = x
    while guess * guess > x:
        guess = (guess + x // guess) // 2
    
    return guess


# ═══════════════════════════════════════════════════════════════════════════
# 📊 COMPLEXITY COMPARISON
# ═══════════════════════════════════════════════════════════════════════════
"""
╔════════════════╦════════════╦═══════════╦═════════════════════════╗
║   Approach     ║    Time    ║   Space   ║       Notes             ║
╠════════════════╬════════════╬═══════════╬═════════════════════════╣
║ Brute Force    ║   O(√x)    ║   O(1)    ║ Linear search           ║
║ Binary Search  ║  O(log x)  ║   O(1)    ║ Standard approach       ║
║ Newton Method  ║  O(log x)  ║   O(1)    ║ Faster convergence      ║
╚════════════════╩════════════╩═══════════╩═════════════════════════╝
"""


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [4, 8, 1, 0, 16, 25, 26]
    
    print("=" * 70)
    print("🧪 TESTING SQRT(X)")
    print("=" * 70)
    
    for x in test_cases:
        brute = mySqrt_bruteforce(x)
        binary = mySqrt(x)
        newton = mySqrt_newton(x)
        
        print(f"\nInput: x = {x}")
        print(f"Brute Force: {brute}")
        print(f"Binary Search: {binary}")
        print(f"Newton: {newton}")
        print(f"Verify: {binary}² = {binary*binary}, {binary+1}² = {(binary+1)*(binary+1)}")

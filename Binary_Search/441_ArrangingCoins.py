"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #441 - Arranging Coins                            ║
║                    Topic: Binary Search / Math                               ║
║                    Difficulty: Easy                                           ║
║                    Company: Amazon, Bloomberg                                ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
You have n coins. Build staircase where row k has k coins.
Return how many COMPLETE rows you can build.

EXAMPLES:
─────────
✓ Input: n = 5
  Staircase:
    ¢
    ¢¢
    ¢¢    (incomplete row)
  Output: 2

✓ Input: n = 8
  Staircase:
    ¢
    ¢¢
    ¢¢¢
    ¢¢    (incomplete)
  Output: 3

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
📚 Stacking books: Row 1 has 1 book, row 2 has 2 books...
   With 8 books, you can complete 3 rows (1+2+3=6, need 4 more for row 4).

🎂 Cake tower: Layer 1 has 1 cake, layer 2 has 2 cakes...
   With 5 cakes, complete 2 layers (1+2=3, only 2 left).

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   Amazon packaging: arrange n items in pyramid display.
   Find max complete rows.

📌 TASK:
   Find k where k(k+1)/2 ≤ n.
   Time O(log n), Space O(1).

📌 ACTION:
   Binary search on answer:
   1. Try k rows
   2. Check if k(k+1)/2 ≤ n
   3. Search higher or lower

📌 RESULT:
   ✓ Time: O(log n) binary search
   ✓ Space: O(1) constant
   ✓ Fast row calculation

"""

# ═══════════════════════════════════════════════════════════════════════════
# 💡 BRUTE FORCE - Count Rows
# ═══════════════════════════════════════════════════════════════════════════
def arrangeCoins_bruteforce(n):
    """
    Subtract coins row by row until can't complete row
    
    Time: O(√n)
    Space: O(1)
    """
    row = 0
    while n >= row + 1:
        row += 1
        n -= row
    return row


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Binary Search
# ═══════════════════════════════════════════════════════════════════════════
def arrangeCoins(n):
    """
    Binary search on number of complete rows
    
    Formula: Sum of first k integers = k(k+1)/2
    Find max k where k(k+1)/2 ≤ n
    
    Example: n = 8
    ────────
    left=0, right=8, mid=4
    4×5/2 = 10 > 8 → Too many, search left
    
    left=0, right=3, mid=1
    1×2/2 = 1 < 8 → Too few, search right
    
    left=2, right=3, mid=2
    2×3/2 = 3 < 8 → Too few, search right
    
    left=3, right=3, mid=3
    3×4/2 = 6 < 8 → Too few, search right
    
    left=4, right=3 → Done! Return 3
    """
    left, right = 0, n
    
    while left <= right:
        mid = (left + right) // 2
        coins_needed = mid * (mid + 1) // 2
        
        if coins_needed == n:
            return mid
        elif coins_needed < n:
            left = mid + 1
        else:
            right = mid - 1
    
    return right


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE - Math Formula
# ═══════════════════════════════════════════════════════════════════════════
def arrangeCoins_math(n):
    """
    Solve quadratic equation: k(k+1)/2 = n
    k² + k - 2n = 0
    k = (-1 + √(1 + 8n)) / 2
    
    Time: O(1)
    Space: O(1)
    """
    import math
    return int((-1 + math.sqrt(1 + 8 * n)) / 2)


# ═══════════════════════════════════════════════════════════════════════════
# 📊 COMPLEXITY COMPARISON
# ═══════════════════════════════════════════════════════════════════════════
"""
╔════════════════╦════════════╦═══════════╦═════════════════════════╗
║   Approach     ║    Time    ║   Space   ║       Notes             ║
╠════════════════╬════════════╬═══════════╬═════════════════════════╣
║ Brute Force    ║   O(√n)    ║   O(1)    ║ Row by row subtraction  ║
║ Binary Search  ║  O(log n)  ║   O(1)    ║ Search on answer        ║
║ Math Formula   ║    O(1)    ║   O(1)    ║ Direct calculation      ║
╚════════════════╩════════════╩═══════════╩═════════════════════════╝
"""


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [5, 8, 1, 0, 10, 1804289383]
    
    print("=" * 70)
    print("🧪 TESTING ARRANGING COINS")
    print("=" * 70)
    
    for n in test_cases:
        brute = arrangeCoins_bruteforce(n) if n < 1000000 else "Skipped (too slow)"
        optimal = arrangeCoins(n)
        math_sol = arrangeCoins_math(n)
        
        print(f"\nInput: n = {n}")
        print(f"Brute: {brute}")
        print(f"Binary: {optimal}")
        print(f"Math: {math_sol}")
        if isinstance(brute, int):
            print(f"Verify: {optimal}×{optimal+1}//2 = {optimal*(optimal+1)//2} ≤ {n}")

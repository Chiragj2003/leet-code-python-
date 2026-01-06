"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #278 - First Bad Version                          ║
║                    Topic: Binary Search                                      ║
║                    Difficulty: Easy                                           ║
║                    Company: Amazon, Meta, Google                             ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
You have n versions [1,2,3,...,n]. Find first bad version.
All versions after bad version are also bad.
Minimize calls to isBadVersion(version) API.

EXAMPLES:
─────────
✓ Input: n = 5, bad = 4
  Versions: [good, good, good, bad, bad]
  Output: 4

✓ Input: n = 1, bad = 1
  Output: 1

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🍪 Cookie batch: Made 100 cookies. At some point, recipe got bad.
   Find first bad cookie. Can only taste each cookie once.
   [good, good, good, BAD, bad, bad...]

📚 Book printing: 1000 copies. Printer broke at some page.
   Find first broken page efficiently.

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   Amazon app versions: bug introduced in some version.
   Find first bad version with minimal API calls.

📌 TASK:
   Find first bad version in [1, n].
   Time O(log n), Space O(1).
   Minimize isBadVersion() calls.

📌 ACTION:
   Binary search:
   1. Check middle version
   2. If bad, search left (including mid)
   3. If good, search right

📌 RESULT:
   ✓ Time: O(log n) binary search
   ✓ Space: O(1) constant
   ✓ Minimal API calls (log n instead of n)

"""

# ═══════════════════════════════════════════════════════════════════════════
# 🔧 MOCK API (for testing)
# ═══════════════════════════════════════════════════════════════════════════
BAD_VERSION = 4  # Global variable for testing

def isBadVersion(version):
    """Mock API that checks if version is bad"""
    return version >= BAD_VERSION


# ═══════════════════════════════════════════════════════════════════════════
# 💡 BRUTE FORCE - Linear Search
# ═══════════════════════════════════════════════════════════════════════════
def firstBadVersion_bruteforce(n):
    """
    Check each version sequentially
    
    Time: O(n) - check all versions
    Space: O(1)
    API Calls: O(n)
    """
    for i in range(1, n + 1):
        if isBadVersion(i):
            return i
    return n


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Binary Search
# ═══════════════════════════════════════════════════════════════════════════
def firstBadVersion(n):
    """
    Binary search for first bad version
    
    Key: All versions after first bad are also bad.
    This creates a sorted pattern: [False, False, True, True...]
    
    Example: n = 5, bad = 4
    ────────
    Versions: [1, 2, 3, 4, 5]
    Status:   [G, G, G, B, B]
    
    left=1, right=5, mid=3
    isBadVersion(3)=False → Search right
    
    left=4, right=5, mid=4
    isBadVersion(4)=True → Search left (keep mid)
    
    left=4, right=4 → Found! Return 4
    """
    left, right = 1, n
    
    while left < right:
        mid = left + (right - left) // 2  # Avoid overflow
        
        if isBadVersion(mid):
            # Mid is bad, first bad might be mid or earlier
            right = mid
        else:
            # Mid is good, first bad is after mid
            left = mid + 1
    
    return left


# ═══════════════════════════════════════════════════════════════════════════
# 📊 COMPLEXITY COMPARISON
# ═══════════════════════════════════════════════════════════════════════════
"""
╔════════════════╦════════════╦═══════════╦═════════════════════════╗
║   Approach     ║    Time    ║   Space   ║     API Calls           ║
╠════════════════╬════════════╬═══════════╬═════════════════════════╣
║ Brute Force    ║   O(n)     ║   O(1)    ║ O(n) worst case         ║
║ Binary Search  ║  O(log n)  ║   O(1)    ║ O(log n) - optimal      ║
╚════════════════╩════════════╩═══════════╩═════════════════════════╝

For n = 1,000,000:
- Brute Force: up to 1,000,000 calls
- Binary Search: ~20 calls
"""


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [
        (5, 4),   # bad at 4
        (1, 1),   # bad at 1
        (10, 6),  # bad at 6
    ]
    
    print("=" * 70)
    print("🧪 TESTING FIRST BAD VERSION")
    print("=" * 70)
    
    for n, bad in test_cases:
        # Set global bad version for testing
        BAD_VERSION = bad
        
        result_brute = firstBadVersion_bruteforce(n)
        result_optimal = firstBadVersion(n)
        
        print(f"\nInput: n = {n}, first bad = {bad}")
        print(f"Brute Force: {result_brute} {'✓' if result_brute == bad else '✗'}")
        print(f"Binary Search: {result_optimal} {'✓' if result_optimal == bad else '✗'}")

"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #658 - Find K Closest Elements                    ║
║                    Topic: Binary Search                                      ║
║                    Difficulty: Medium                                         ║
║                    Company: Amazon, Meta, LinkedIn                           ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Given sorted array, find k closest elements to x.
Return result in sorted order.

EXAMPLES:
─────────
✓ Input: arr = [1,2,3,4,5], k = 4, x = 3
  Output: [1,2,3,4]

✓ Input: arr = [1,2,3,4,5], k = 4, x = -1
  Output: [1,2,3,4]

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
📏 Number line: Find 4 numbers closest to 3.
   Numbers: 1,2,3,4,5
   Closest 4: [1,2,3,4] (distances: 2,1,0,1)

🎯 Dartboard scores: [10,20,30,40,50].
   Find 3 scores closest to 35.
   Answer: [20,30,40]

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   Amazon recommendations: find k products with prices
   closest to customer's budget.

📌 TASK:
   Find k closest elements to x in sorted array.
   Time O(log n + k), Space O(1).

📌 ACTION:
   Binary search for window start:
   1. Find position where k-window should start
   2. Use two pointers to maintain window

📌 RESULT:
   ✓ Time: O(log(n-k) + k) binary search + result
   ✓ Space: O(1) excluding output
   ✓ Efficient closest elements

"""

# ═══════════════════════════════════════════════════════════════════════════
# 💡 BRUTE FORCE - Sort by Distance
# ═══════════════════════════════════════════════════════════════════════════
def findClosestElements_bruteforce(arr, k, x):
    """
    Sort all elements by distance from x
    
    Time: O(n log n)
    Space: O(n)
    """
    # Sort by distance, then by value
    sorted_arr = sorted(arr, key=lambda num: (abs(num - x), num))
    # Take first k and sort them
    return sorted(sorted_arr[:k])


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Binary Search + Two Pointers
# ═══════════════════════════════════════════════════════════════════════════
def findClosestElements(arr, k, x):
    """
    Binary search for window start position
    
    Key insight: Find starting index of k-length window
    where all elements are closest to x
    
    Example: arr = [1,2,3,4,5], k = 4, x = 3
    ────────
    We want window of size 4 closest to 3.
    
    Compare windows:
    [1,2,3,4]: distances [2,1,0,1] → good
    [2,3,4,5]: distances [1,0,1,2] → not better
    
    Use binary search on window start position.
    """
    left, right = 0, len(arr) - k
    
    while left < right:
        mid = (left + right) // 2
        
        # Compare: should window start at mid or mid+1?
        # If arr[mid] is farther from x than arr[mid+k], move right
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    
    return arr[left:left + k]


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE - Two Pointers from Center
# ═══════════════════════════════════════════════════════════════════════════
def findClosestElements_expand(arr, k, x):
    """
    Find closest element, then expand window
    
    Time: O(log n + k)
    Space: O(1)
    """
    # Binary search for closest element
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    
    # Expand window from closest position
    left = right - 1
    
    for _ in range(k):
        if left < 0:
            right += 1
        elif right >= len(arr):
            left -= 1
        elif x - arr[left] <= arr[right] - x:
            left -= 1
        else:
            right += 1
    
    return arr[left + 1:right]


# ═══════════════════════════════════════════════════════════════════════════
# 📊 COMPLEXITY COMPARISON
# ═══════════════════════════════════════════════════════════════════════════
"""
╔════════════════╦════════════════╦═══════════╦═════════════════════════╗
║   Approach     ║      Time      ║   Space   ║       Notes             ║
╠════════════════╬════════════════╬═══════════╬═════════════════════════╣
║ Brute Force    ║   O(n log n)   ║   O(n)    ║ Sort by distance        ║
║ Binary+Window  ║ O(log(n-k)+k)  ║   O(1)    ║ Optimal solution        ║
║ Expand Window  ║  O(log n + k)  ║   O(1)    ║ Intuitive approach      ║
╚════════════════╩════════════════╩═══════════╩═════════════════════════╝
"""


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4]),
        ([1, 1, 2, 3, 4, 5], 3, 3, [2, 3, 4]),
    ]
    
    print("=" * 70)
    print("🧪 TESTING FIND K CLOSEST ELEMENTS")
    print("=" * 70)
    
    for arr, k, x, expected in test_cases:
        brute = findClosestElements_bruteforce(arr.copy(), k, x)
        optimal = findClosestElements(arr.copy(), k, x)
        expand = findClosestElements_expand(arr.copy(), k, x)
        
        print(f"\nInput: arr = {arr}, k = {k}, x = {x}")
        print(f"Expected: {expected}")
        print(f"Brute: {brute} {'✓' if brute == expected else '✗'}")
        print(f"Binary: {optimal} {'✓' if optimal == expected else '✗'}")
        print(f"Expand: {expand} {'✓' if expand == expected else '✗'}")

"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #153 - Find Minimum in Rotated Array              ║
║                    Topic: Binary Search                                      ║
║                    Difficulty: Medium                                         ║
║                    Company: Amazon, Meta, Bloomberg                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Sorted array rotated at unknown pivot. Find minimum element in O(log n).

EXAMPLES:
─────────
✓ Input: [3,4,5,1,2] → Output: 1
✓ Input: [4,5,6,7,0,1,2] → Output: 0
✓ Input: [11,13,15,17] → Output: 11

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🎢 Roller coaster: Heights go up (1,2,3,4,5) then loop back.
   Now: 3,4,5,1,2. Find lowest point!

🌡️ Temperature chart: was 10,20,30,40,50 but rotated.
   Now: 30,40,50,10,20. Find coldest day.

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   Amazon pricing: sorted prices rotated. Need to find
   lowest price quickly for competitor analysis.

📌 TASK:
   Find minimum in rotated sorted array.
   Time O(log n), Space O(1).

📌 ACTION:
   Binary search:
   1. If mid > right, min in right half
   2. Else, min in left half (including mid)

📌 RESULT:
   ✓ Time: O(log n) binary search
   ✓ Space: O(1) constant
   ✓ Fast minimum lookup

"""

# ═══════════════════════════════════════════════════════════════════════════
# 💡 BRUTE FORCE - Linear Scan
# ═══════════════════════════════════════════════════════════════════════════
def findMin_bruteforce(nums):
    """
    Simple scan for minimum
    
    Time: O(n)
    Space: O(1)
    """
    return min(nums)


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Binary Search
# ═══════════════════════════════════════════════════════════════════════════
def findMin(nums):
    """
    Binary search for minimum
    
    Key: Compare mid with right
    
    Example: [4,5,6,7,0,1,2]
    ────────
    left=0, right=6, mid=3
    nums[mid]=7 > nums[right]=2 → Min in RIGHT half
    
    left=4, right=6, mid=5
    nums[mid]=1 < nums[right]=2 → Min in LEFT half (including mid)
    
    left=4, right=5, mid=4
    nums[mid]=0 < nums[right]=1 → Min in LEFT half
    
    left=4, right=4 → FOUND! Return nums[4]=0
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # Min is in right half
        if nums[mid] > nums[right]:
            left = mid + 1
        # Min is in left half (including mid)
        else:
            right = mid
    
    return nums[left]


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE - Check Both Sides
# ═══════════════════════════════════════════════════════════════════════════
def findMin_verbose(nums):
    """
    More explicit comparisons
    """
    left, right = 0, len(nums) - 1
    
    # Already sorted (no rotation)
    if nums[left] < nums[right]:
        return nums[left]
    
    while left < right:
        mid = (left + right) // 2
        
        # Check if mid is pivot
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        if nums[mid] < nums[mid - 1]:
            return nums[mid]
        
        # Decide which half
        if nums[mid] > nums[0]:
            left = mid + 1
        else:
            right = mid
    
    return nums[left]


# ═══════════════════════════════════════════════════════════════════════════
# 📊 COMPLEXITY COMPARISON
# ═══════════════════════════════════════════════════════════════════════════
"""
╔════════════════╦════════════╦═══════════╦═════════════════════════╗
║   Approach     ║    Time    ║   Space   ║       Notes             ║
╠════════════════╬════════════╬═══════════╬═════════════════════════╣
║ Brute Force    ║   O(n)     ║   O(1)    ║ Simple min() function   ║
║ Binary Search  ║  O(log n)  ║   O(1)    ║ Optimal solution        ║
╚════════════════╩════════════╩═══════════╩═════════════════════════╝
"""


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [
        [3, 4, 5, 1, 2],
        [4, 5, 6, 7, 0, 1, 2],
        [11, 13, 15, 17],
        [2, 1],
    ]
    
    print("=" * 70)
    print("🧪 TESTING FIND MINIMUM IN ROTATED ARRAY")
    print("=" * 70)
    
    for nums in test_cases:
        result_brute = findMin_bruteforce(nums)
        result_optimal = findMin(nums)
        result_verbose = findMin_verbose(nums)
        
        print(f"\nInput: {nums}")
        print(f"Brute Force: {result_brute}")
        print(f"Binary Search: {result_optimal}")
        print(f"Verbose: {result_verbose}")

"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #33 - Search in Rotated Sorted Array              ║
║                    Topic: Binary Search                                      ║
║                    Difficulty: Medium                                         ║
║                    Company: Amazon, Meta, Microsoft                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Sorted array rotated at unknown pivot. Search for target in O(log n).

EXAMPLES:
─────────
✓ Input: nums = [4,5,6,7,0,1,2], target = 0 → Output: 4
✓ Input: nums = [4,5,6,7,0,1,2], target = 3 → Output: -1
✓ Input: nums = [1], target = 0 → Output: -1

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🎪 Circular queue: People lined up 1,2,3,4,5 but rotated!
   Now: 4,5,1,2,3. Find person #2.

📚 Bookshelf: Books sorted A-Z but someone rotated it.
   P,Q,R,S,T,A,B,C... Find book 'C'.

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   Amazon inventory: rotated sorted array of product IDs.
   Need fast O(log n) search.

📌 TASK:
   Find target in rotated sorted array.
   Time O(log n), Space O(1).

📌 ACTION:
   Modified binary search:
   1. Find which half is sorted
   2. Check if target in sorted half
   3. Search appropriate half

📌 RESULT:
   ✓ Time: O(log n) binary search
   ✓ Space: O(1) constant
   ✓ Fast inventory lookup

"""

# ═══════════════════════════════════════════════════════════════════════════
# 💡 BRUTE FORCE - Linear Search
# ═══════════════════════════════════════════════════════════════════════════
def search_bruteforce(nums, target):
    """
    Simple scan through array
    
    Time: O(n) - check each element
    Space: O(1)
    """
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Modified Binary Search
# ═══════════════════════════════════════════════════════════════════════════
def search(nums, target):
    """
    Binary search on rotated array
    
    Key Insight: One half is always sorted!
    
    Example: [4,5,6,7,0,1,2], target = 0
    ────────
    left=0, right=6, mid=3
    nums[mid]=7 > nums[left]=4 → LEFT half sorted
    target=0 not in [4,7] → search RIGHT
    
    left=4, right=6, mid=5
    nums[mid]=1 < nums[right]=2 → RIGHT half sorted
    target=0 not in [1,2] → search LEFT
    
    left=4, right=4, mid=4
    nums[mid]=0 → FOUND! Return 4
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Left half is sorted
        if nums[left] <= nums[mid]:
            # Target in sorted left half?
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            # Target in sorted right half?
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1


# ═══════════════════════════════════════════════════════════════════════════
# 📊 COMPLEXITY COMPARISON
# ═══════════════════════════════════════════════════════════════════════════
"""
╔════════════════╦════════════╦═══════════╦═════════════════════════╗
║   Approach     ║    Time    ║   Space   ║       Notes             ║
╠════════════════╬════════════╬═══════════╬═════════════════════════╣
║ Brute Force    ║   O(n)     ║   O(1)    ║ Simple linear scan      ║
║ Binary Search  ║  O(log n)  ║   O(1)    ║ Optimal for this case   ║
╚════════════════╩════════════╩═══════════╩═════════════════════════╝
"""


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([1, 3], 3, 1),
    ]
    
    print("=" * 70)
    print("🧪 TESTING SEARCH IN ROTATED SORTED ARRAY")
    print("=" * 70)
    
    for nums, target, expected in test_cases:
        result_brute = search_bruteforce(nums, target)
        result_optimal = search(nums, target)
        
        print(f"\nInput: nums = {nums}, target = {target}")
        print(f"Expected: {expected}")
        print(f"Brute Force: {result_brute} {'✓' if result_brute == expected else '✗'}")
        print(f"Binary Search: {result_optimal} {'✓' if result_optimal == expected else '✗'}")

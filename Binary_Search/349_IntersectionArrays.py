"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #349 - Intersection of Two Arrays                 ║
║                    Topic: Binary Search / Hash Set                           ║
║                    Difficulty: Easy                                           ║
║                    Company: Amazon, Meta, Apple                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Given two integer arrays, return array of their intersection.
Each element must appear UNIQUE (no duplicates in output).

EXAMPLES:
─────────
✓ Input: nums1 = [1,2,2,1], nums2 = [2,2] → Output: [2]
✓ Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4] → Output: [9,4] or [4,9]

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🎨 Paint colors: You have [red, blue, blue, red].
   Friend has [blue, blue]. Common color: [blue].

🧸 Toys: Your toys [car, doll, doll, car].
   Friend's toys [doll, doll]. Shared: [doll].

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   Amazon recommendations: find products viewed by both users.

📌 TASK:
   Find unique intersection of two arrays.
   Time O(n+m), Space O(min(n,m)).

📌 ACTION:
   Hash set approach:
   1. Put smaller array in set
   2. Check each element of larger array
   3. Add to result if in set

📌 RESULT:
   ✓ Time: O(n + m) linear
   ✓ Space: O(min(n,m)) for set
   ✓ Fast common element finding

"""

# ═══════════════════════════════════════════════════════════════════════════
# 💡 BRUTE FORCE - Nested Loop
# ═══════════════════════════════════════════════════════════════════════════
def intersection_bruteforce(nums1, nums2):
    """
    Check each pair
    
    Time: O(n × m)
    Space: O(1) excluding result
    """
    result = set()
    
    for num1 in nums1:
        for num2 in nums2:
            if num1 == num2:
                result.add(num1)
                break
    
    return list(result)


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Hash Set
# ═══════════════════════════════════════════════════════════════════════════
def intersection(nums1, nums2):
    """
    Hash set for O(1) lookups
    
    Example: [1,2,2,1] and [2,2]
    ────────
    set1 = {1, 2}
    Check each in nums2:
    - 2 in set1? Yes → add to result
    - 2 in set1? Yes (but already in result)
    Result: [2]
    """
    set1 = set(nums1)
    result = set()
    
    for num in nums2:
        if num in set1:
            result.add(num)
    
    return list(result)


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE - Binary Search
# ═══════════════════════════════════════════════════════════════════════════
def intersection_binary(nums1, nums2):
    """
    Binary search approach (if arrays sorted)
    
    Time: O(n log n + m log m) for sorting + O(n log m)
    Space: O(1) excluding result
    """
    nums1.sort()
    nums2.sort()
    result = set()
    
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
    # Search for each nums1 element in nums2
    for num in nums1:
        if binary_search(nums2, num):
            result.add(num)
    
    return list(result)


# ═══════════════════════════════════════════════════════════════════════════
# 🎯 ALTERNATIVE - Two Pointers (for sorted arrays)
# ═══════════════════════════════════════════════════════════════════════════
def intersection_twopointer(nums1, nums2):
    """
    Two pointers on sorted arrays
    
    Time: O(n log n + m log m + n + m)
    Space: O(1) excluding result
    """
    nums1.sort()
    nums2.sort()
    
    i = j = 0
    result = set()
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.add(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    
    return list(result)


# ═══════════════════════════════════════════════════════════════════════════
# 📊 COMPLEXITY COMPARISON
# ═══════════════════════════════════════════════════════════════════════════
"""
╔════════════════╦════════════════╦═══════════╦═════════════════════════╗
║   Approach     ║      Time      ║   Space   ║       Notes             ║
╠════════════════╬════════════════╬═══════════╬═════════════════════════╣
║ Brute Force    ║    O(n×m)      ║   O(1)    ║ Nested loops            ║
║ Hash Set       ║    O(n+m)      ║ O(min(n,m))║ Best for unsorted       ║
║ Binary Search  ║O(n log m+sort) ║   O(1)    ║ Good if sorted          ║
║ Two Pointers   ║  O(n+m+sort)   ║   O(1)    ║ Clean if sorted         ║
╚════════════════╩════════════════╩═══════════╩═════════════════════════╝
"""


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 2, 1], [2, 2]),
        ([4, 9, 5], [9, 4, 9, 8, 4]),
        ([1, 2, 3], [4, 5, 6]),
    ]
    
    print("=" * 70)
    print("🧪 TESTING INTERSECTION OF TWO ARRAYS")
    print("=" * 70)
    
    for nums1, nums2 in test_cases:
        brute = sorted(intersection_bruteforce(nums1.copy(), nums2.copy()))
        optimal = sorted(intersection(nums1.copy(), nums2.copy()))
        binary = sorted(intersection_binary(nums1.copy(), nums2.copy()))
        twoptr = sorted(intersection_twopointer(nums1.copy(), nums2.copy()))
        
        print(f"\nInput: nums1 = {nums1}, nums2 = {nums2}")
        print(f"Brute: {brute}")
        print(f"Hash Set: {optimal}")
        print(f"Binary: {binary}")
        print(f"Two Pointer: {twoptr}")

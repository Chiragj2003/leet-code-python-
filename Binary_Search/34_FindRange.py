"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #34 - Find First and Last Position                ║
║                    Topic: Binary Search                                      ║
║                    Difficulty: Medium                                         ║
║                    Company: Amazon, Meta, Google                             ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Given sorted array, find starting and ending position of target.
If target not found, return [-1, -1].
Must run in O(log n).

EXAMPLES:
─────────
✓ Input: nums = [5,7,7,8,8,10], target = 8 → Output: [3,4]
✓ Input: nums = [5,7,7,8,8,10], target = 6 → Output: [-1,-1]
✓ Input: nums = [], target = 0 → Output: [-1,-1]

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
📚 Library: Books sorted by ID. Find first and last book with ID "007".
   Books: [001, 005, 007, 007, 007, 010]
   First 007 at position 2, last at position 4.

🎯 Archery scores: [5,7,7,8,8,10]. Find range where score is 8.
   Starts at index 3, ends at index 4.

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   Amazon inventory: sorted product IDs with duplicates.
   Find all occurrences efficiently.

📌 TASK:
   Find first and last positions of target.
   Time O(log n), Space O(1).

📌 ACTION:
   Two binary searches:
   1. Find leftmost (first) occurrence
   2. Find rightmost (last) occurrence

📌 RESULT:
   ✓ Time: O(log n) - two binary searches
   ✓ Space: O(1) constant
   ✓ Efficient range finding

"""

# ═══════════════════════════════════════════════════════════════════════════
# 💡 BRUTE FORCE - Linear Scan
# ═══════════════════════════════════════════════════════════════════════════
def searchRange_bruteforce(nums, target):
    """
    Scan array to find first and last
    
    Time: O(n)
    Space: O(1)
    """
    if not nums:
        return [-1, -1]
    
    first = last = -1
    
    for i in range(len(nums)):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    
    return [first, last]


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Two Binary Searches
# ═══════════════════════════════════════════════════════════════════════════
def searchRange(nums, target):
    """
    Binary search for left and right boundaries
    
    Example: [5,7,7,8,8,10], target = 8
    ────────
    Find leftmost 8:
    left=0, right=5, mid=2, nums[2]=7 < 8 → search right
    left=3, right=5, mid=4, nums[4]=8 == 8 → continue left (might be earlier)
    left=3, right=3, nums[3]=8 → Found leftmost = 3
    
    Find rightmost 8:
    left=0, right=5, mid=2, nums[2]=7 < 8 → search right
    left=3, right=5, mid=4, nums[4]=8 == 8 → continue right (might be later)
    left=5, right=5, nums[5]=10 > 8 → Found rightmost = 4
    """
    def findBound(isLeft):
        left, right = 0, len(nums) - 1
        bound = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                bound = mid
                # Continue searching
                if isLeft:
                    right = mid - 1  # Look left for earlier occurrence
                else:
                    left = mid + 1   # Look right for later occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return bound
    
    if not nums:
        return [-1, -1]
    
    leftBound = findBound(True)
    if leftBound == -1:
        return [-1, -1]
    
    rightBound = findBound(False)
    
    return [leftBound, rightBound]


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE - Single Pass with Expansion
# ═══════════════════════════════════════════════════════════════════════════
def searchRange_expand(nums, target):
    """
    Binary search + linear expansion
    
    Time: O(log n + k) where k is count of target
    Space: O(1)
    """
    if not nums:
        return [-1, -1]
    
    # Find any occurrence
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            # Expand left and right
            first = last = mid
            while first > 0 and nums[first - 1] == target:
                first -= 1
            while last < len(nums) - 1 and nums[last + 1] == target:
                last += 1
            return [first, last]
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return [-1, -1]


# ═══════════════════════════════════════════════════════════════════════════
# 📊 COMPLEXITY COMPARISON
# ═══════════════════════════════════════════════════════════════════════════
"""
╔════════════════╦════════════╦═══════════╦═════════════════════════╗
║   Approach     ║    Time    ║   Space   ║       Notes             ║
╠════════════════╬════════════╬═══════════╬═════════════════════════╣
║ Brute Force    ║   O(n)     ║   O(1)    ║ Linear scan             ║
║ Two Binary     ║  O(log n)  ║   O(1)    ║ Optimal solution        ║
║ Binary+Expand  ║ O(log n+k) ║   O(1)    ║ k = target count        ║
╚════════════════╩════════════╩═══════════╩═════════════════════════╝
"""


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
        ([1], 1, [0, 0]),
    ]
    
    print("=" * 70)
    print("🧪 TESTING FIND FIRST AND LAST POSITION")
    print("=" * 70)
    
    for nums, target, expected in test_cases:
        brute = searchRange_bruteforce(nums, target)
        optimal = searchRange(nums, target)
        expand = searchRange_expand(nums, target)
        
        print(f"\nInput: nums = {nums}, target = {target}")
        print(f"Expected: {expected}")
        print(f"Brute: {brute} {'✓' if brute == expected else '✗'}")
        print(f"Binary: {optimal} {'✓' if optimal == expected else '✗'}")
        print(f"Expand: {expand} {'✓' if expand == expected else '✗'}")

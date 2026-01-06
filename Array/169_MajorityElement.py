"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #169 - Majority Element                           ║
║                    Topic: Array / Boyer-Moore Voting                         ║
║                    Difficulty: Easy                                           ║
║                    Company: Amazon, Adobe, Google                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Find element that appears MORE THAN n/2 times.
(There's always exactly one such element)

EXAMPLES:
─────────
✓ Input: [3,2,3]            → Output: 3 (appears 2 times, n=3, 2>3/2)
✓ Input: [2,2,1,1,1,2,2]    → Output: 2 (appears 4 times, n=7, 4>7/2)
✓ Input: [1]                → Output: 1

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🗳️ In an election with n voters, one candidate gets MORE than half votes.
   Find the winner! (Majority wins)

🎉 In a class party, one activity is chosen by more than half the kids.
   What activity will most kids do?

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   At Amazon, we analyze customer reviews. One product rating dominates
   (appears more than 50% of time). We need to identify the majority
   rating for dashboard display without scanning all reviews.

📌 TASK:
   Find element appearing more than n/2 times.
   Time O(n), Space O(1).

📌 ACTION:
   Use Boyer-Moore Voting Algorithm:
   
   ✓ Algorithm:
     1. Maintain a candidate and count
     2. If count = 0, pick new candidate
     3. If element matches candidate, count++
     4. If element different, count--
     5. Majority always survives!

📌 RESULT:
   ✓ Time Complexity: O(n) - single pass
   ✓ Space Complexity: O(1) - elegant algorithm
   ✓ Majority rating found instantly from billions of reviews

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⏰ COMPLEXITY ANALYSIS                                    ║
╚══════════════════════════════════════════════════════════════════════════════╝

BRUTE FORCE (Count All):
    Time: O(n²) - for each element, count occurrences
    Space: O(1)

HASHMAP (Count Frequencies):
    Time: O(n)
    Space: O(n) - store all elements

BOYER-MOORE VOTING (OPTIMAL):
    Time: O(n) - single pass
    Space: O(1) - genius algorithm!

"""

# ═══════════════════════════════════════════════════════════════════════════
# 🐢 BRUTE FORCE SOLUTION - O(n²) Time, O(1) Space
# ═══════════════════════════════════════════════════════════════════════════
def majorityElement_bruteforce(nums):
    """
    Brute Force: Count each element
    
    STEPS:
    ──────
    1. For each element
    2. Count how many times it appears
    3. If count > n/2, return it
    
    Example: [2,2,1,1,1,2,2]
    ───────
    Check 2: appears 4 times, 4 > 7/2=3.5 → Return 2 ✓
    """
    n = len(nums)
    target = n // 2
    
    for num in nums:
        count = 0
        for x in nums:
            if x == num:
                count += 1
        if count > target:
            return num
    
    return -1


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Boyer-Moore Voting
# ═══════════════════════════════════════════════════════════════════════════
def majorityElement(nums):
    """
    Boyer-Moore Voting Algorithm - OPTIMAL!
    
    🔑 KEY INSIGHT:
    ───────────────
    Majority element appears > n/2 times.
    Cancel out non-majority with majority:
    - If count = 0, new candidate
    - If element = candidate, count++
    - If element ≠ candidate, count-- (one cancellation)
    
    Majority will always survive cancellations!
    
    Example: [2,2,1,1,1,2,2]
    ───────
    candidate=None, count=0
    
    i=0: 2, count=0 → candidate=2, count=1
    i=1: 2, match → count=2
    i=2: 1, no match → count=1
    i=3: 1, no match → count=0
    i=4: 1, count=0 → candidate=1, count=1
    i=5: 2, no match → count=0
    i=6: 2, count=0 → candidate=2, count=1
    
    Final candidate: 2 ✓
    
    WHY: 2 appears 4 times, 1 appears 3 times.
    2's exceed 1's by 1, so 2 "wins" cancellations!
    
    Time: O(n) - single pass
    Space: O(1) - no extra space!
    """
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            # No current candidate, pick this one
            candidate = num
        
        # Vote: match = +1, different = -1
        if num == candidate:
            count += 1
        else:
            count -= 1
    
    return candidate


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE - Hashmap/Counter
# ═══════════════════════════════════════════════════════════════════════════
def majorityElement_hashmap(nums):
    """
    Hashmap: Count all frequencies
    
    Time: O(n)
    Space: O(n)
    """
    from collections import Counter
    
    counts = Counter(nums)
    target = len(nums) // 2
    
    for num, count in counts.items():
        if count > target:
            return num


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([1], 1),
        ([3, 3, 4], 3),
    ]
    
    print("=" * 70)
    print("🧪 TESTING MAJORITY ELEMENT SOLUTIONS")
    print("=" * 70)
    
    for nums, expected in test_cases:
        result_brute = majorityElement_bruteforce(nums)
        result_voting = majorityElement(nums)
        result_hash = majorityElement_hashmap(nums)
        
        status = "✓" if result_voting == expected else "✗"
        
        print(f"\n{status} Input: {nums}")
        print(f"  Expected:  {expected}")
        print(f"  Brute:     {result_brute}")
        print(f"  Voting:    {result_voting}")
        print(f"  Hashmap:   {result_hash}")
    
    print("\n" + "=" * 70)
    print("📊 COMPLEXITY COMPARISON")
    print("=" * 70)
    print("| Method    | Time   | Space   | Amazon |")
    print("|-----------|--------|---------|--------|")
    print("| Brute     | O(n²)  | O(1)    | ❌     |")
    print("| Voting    | O(n)   | O(1)    | ✅     |")
    print("| Hashmap   | O(n)   | O(n)    | ⚠️     |")

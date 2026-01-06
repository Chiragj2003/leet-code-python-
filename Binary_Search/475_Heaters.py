"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #475 - Heaters                                    ║
║                    Topic: Binary Search                                      ║
║                    Difficulty: Medium                                         ║
║                    Company: Amazon, Google                                   ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Houses and heaters on a horizontal line. Find minimum radius
so every house is heated by at least one heater.

EXAMPLES:
─────────
✓ Input: houses = [1,2,3], heaters = [2] → Output: 1
  Heater at 2 with radius 1 covers [1,3]

✓ Input: houses = [1,2,3,4], heaters = [1,4] → Output: 1
  Heaters at 1 and 4 with radius 1 cover all

✓ Input: houses = [1,5], heaters = [2] → Output: 3
  Heater at 2 needs radius 3 to reach house at 5

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🏠 Street: Houses at positions [1,2,3,4].
   Lamps at positions [1,4]. How bright must lamps be?
   Brightness 1 reaches neighbors → all houses lit!

🌡️ Heaters: Need minimum power to warm all houses.

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   Amazon warehouse: heat sensors at fixed positions.
   Find min range to cover all storage areas.

📌 TASK:
   Find minimum radius to heat all houses.
   Time O(n log n + m log m), Space O(1).

📌 ACTION:
   Binary search for each house's nearest heater:
   1. Sort both arrays
   2. For each house, find closest heater
   3. Return max distance

📌 RESULT:
   ✓ Time: O((n+m) log m) with binary search
   ✓ Space: O(1) constant
   ✓ Optimal heater radius found

"""

# ═══════════════════════════════════════════════════════════════════════════
# 💡 BRUTE FORCE - Check All Pairs
# ═══════════════════════════════════════════════════════════════════════════
def findRadius_bruteforce(houses, heaters):
    """
    For each house, find closest heater (brute force)
    
    Time: O(n × m)
    Space: O(1)
    """
    max_radius = 0
    
    for house in houses:
        min_dist = float('inf')
        for heater in heaters:
            min_dist = min(min_dist, abs(house - heater))
        max_radius = max(max_radius, min_dist)
    
    return max_radius


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Binary Search
# ═══════════════════════════════════════════════════════════════════════════
def findRadius(houses, heaters):
    """
    Binary search for closest heater to each house
    
    Example: houses = [1,2,3,4], heaters = [1,4]
    ────────
    Sorted: houses = [1,2,3,4], heaters = [1,4]
    
    House 1: Closest heater = 1, distance = 0
    House 2: Closest heater = 1, distance = 1
    House 3: Closest heater = 4, distance = 1
    House 4: Closest heater = 4, distance = 0
    
    Max distance = 1 → radius = 1
    """
    heaters.sort()
    max_radius = 0
    
    def binary_search_closest(target):
        """Find closest heater to target house"""
        left, right = 0, len(heaters) - 1
        
        while left < right:
            mid = (left + right) // 2
            if heaters[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        # Check both neighbors
        closest = float('inf')
        if left > 0:
            closest = min(closest, abs(heaters[left - 1] - target))
        if left < len(heaters):
            closest = min(closest, abs(heaters[left] - target))
        
        return closest
    
    for house in houses:
        dist = binary_search_closest(house)
        max_radius = max(max_radius, dist)
    
    return max_radius


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE - Two Pointers
# ═══════════════════════════════════════════════════════════════════════════
def findRadius_twopointer(houses, heaters):
    """
    Two pointers on sorted arrays
    
    Time: O(n log n + m log m)
    Space: O(1)
    """
    houses.sort()
    heaters.sort()
    max_radius = 0
    heater_idx = 0
    
    for house in houses:
        # Move heater pointer to closest position
        while (heater_idx < len(heaters) - 1 and
               abs(heaters[heater_idx + 1] - house) <= abs(heaters[heater_idx] - house)):
            heater_idx += 1
        
        max_radius = max(max_radius, abs(heaters[heater_idx] - house))
    
    return max_radius


# ═══════════════════════════════════════════════════════════════════════════
# 📊 COMPLEXITY COMPARISON
# ═══════════════════════════════════════════════════════════════════════════
"""
╔════════════════╦════════════════╦═══════════╦═════════════════════════╗
║   Approach     ║      Time      ║   Space   ║       Notes             ║
╠════════════════╬════════════════╬═══════════╬═════════════════════════╣
║ Brute Force    ║    O(n×m)      ║   O(1)    ║ Check all pairs         ║
║ Binary Search  ║ O(n log m+sort)║   O(1)    ║ Good solution           ║
║ Two Pointers   ║  O(n+m+sort)   ║   O(1)    ║ Optimal after sort      ║
╚════════════════╩════════════════╩═══════════╩═════════════════════════╝
"""


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], [2], 1),
        ([1, 2, 3, 4], [1, 4], 1),
        ([1, 5], [2], 3),
    ]
    
    print("=" * 70)
    print("🧪 TESTING HEATERS")
    print("=" * 70)
    
    for houses, heaters, expected in test_cases:
        brute = findRadius_bruteforce(houses.copy(), heaters.copy())
        optimal = findRadius(houses.copy(), heaters.copy())
        twoptr = findRadius_twopointer(houses.copy(), heaters.copy())
        
        print(f"\nInput: houses = {houses}, heaters = {heaters}")
        print(f"Expected: {expected}")
        print(f"Brute: {brute} {'✓' if brute == expected else '✗'}")
        print(f"Binary: {optimal} {'✓' if optimal == expected else '✗'}")
        print(f"Two Ptr: {twoptr} {'✓' if twoptr == expected else '✗'}")

"""
LeetCode #475 - Heaters
Topic: Binary Search
Difficulty: Medium

PROBLEM EXPLANATION:
Given positions of houses and heaters on a horizontal line, find the minimum
radius of heaters such that all houses can be covered by heaters.
Each heater has a radius and can warm all houses within that distance.

Example:
Input: houses = [1,2,3], heaters = [2]
Output: 1
Explanation: Heater at position 2 with radius 1 covers houses at 1, 2, 3

Input: houses = [1,2,3,4], heaters = [1,4]
Output: 1
Explanation: Heaters at 1 and 4 with radius 1 cover all houses

APPROACH (Binary Search):
1. Sort both houses and heaters arrays
2. For each house, find the closest heater using binary search
3. Calculate distance to closest heater
4. The maximum of all these distances is the answer

Time Complexity: O(n log n + m log m) for sorting
Space Complexity: O(1)
"""

import bisect

def findRadius(houses, heaters):
    """
    Returns minimum radius needed to cover all houses
    """
    heaters.sort()
    max_radius = 0
    
    for house in houses:
        # Find position where house would be inserted in sorted heaters
        pos = bisect.bisect_left(heaters, house)
        
        # Initialize minimum distance to infinity
        min_distance = float('inf')
        
        # Check heater to the left (if exists)
        if pos > 0:
            min_distance = min(min_distance, house - heaters[pos - 1])
        
        # Check heater to the right (if exists)
        if pos < len(heaters):
            min_distance = min(min_distance, heaters[pos] - house)
        
        # Update maximum radius needed
        max_radius = max(max_radius, min_distance)
    
    return max_radius


# Alternative: Manual binary search
def findRadius_manual(houses, heaters):
    """
    Manual binary search implementation
    """
    heaters.sort()
    max_radius = 0
    
    def find_closest_heater(heaters, house):
        """Find distance to closest heater"""
        left, right = 0, len(heaters) - 1
        closest = float('inf')
        
        while left <= right:
            mid = (left + right) // 2
            closest = min(closest, abs(heaters[mid] - house))
            
            if heaters[mid] < house:
                left = mid + 1
            elif heaters[mid] > house:
                right = mid - 1
            else:
                return 0  # House is at heater position
        
        return closest
    
    for house in houses:
        distance = find_closest_heater(heaters, house)
        max_radius = max(max_radius, distance)
    
    return max_radius


# Test cases
if __name__ == "__main__":
    test1_houses = [1, 2, 3]
    test1_heaters = [2]
    print(f"Test 1: {findRadius(test1_houses, test1_heaters)}")
    # Expected: 1
    
    test2_houses = [1, 2, 3, 4]
    test2_heaters = [1, 4]
    print(f"Test 2: {findRadius(test2_houses, test2_heaters)}")
    # Expected: 1
    
    test3_houses = [1, 5]
    test3_heaters = [2]
    print(f"Test 3: {findRadius(test3_houses, test3_heaters)}")
    # Expected: 3

"""
LeetCode #904 - Fruit Into Baskets
Topic: Two Pointers (Sliding Window)
Difficulty: Medium

PROBLEM EXPLANATION:
You're picking fruit from trees in a row. You have two baskets, each can hold
only one type of fruit. Find the maximum number of fruits you can collect
where you can only pick from consecutive trees and use at most 2 fruit types.

Example:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can collect [1,2,1] (all fruits)

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2] or [2,2] but [1,2,2] is longer

APPROACH (Sliding Window):
1. Use a hashmap to track fruit types in current window
2. Expand window by adding fruits from right
3. If more than 2 types, shrink window from left
4. Track maximum window size

Time Complexity: O(n)
Space Complexity: O(1) - at most 3 types in hashmap
"""

def totalFruit(fruits):
    """
    Returns maximum number of fruits that can be collected
    """
    basket = {}  # fruit_type: count
    left = 0
    max_fruits = 0
    
    for right in range(len(fruits)):
        # Add current fruit to basket
        fruit = fruits[right]
        basket[fruit] = basket.get(fruit, 0) + 1
        
        # If we have more than 2 types, shrink window
        while len(basket) > 2:
            left_fruit = fruits[left]
            basket[left_fruit] -= 1
            
            # Remove fruit type if count becomes 0
            if basket[left_fruit] == 0:
                del basket[left_fruit]
            
            left += 1
        
        # Update maximum fruits
        max_fruits = max(max_fruits, right - left + 1)
    
    return max_fruits


# Test cases
if __name__ == "__main__":
    test1 = [1, 2, 1]
    print(f"Test 1: {totalFruit(test1)}")  # Expected: 3
    
    test2 = [0, 1, 2, 2]
    print(f"Test 2: {totalFruit(test2)}")  # Expected: 3
    
    test3 = [1, 2, 3, 2, 2]
    print(f"Test 3: {totalFruit(test3)}")  # Expected: 4 ([2,3,2,2])
    
    test4 = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    print(f"Test 4: {totalFruit(test4)}")  # Expected: 5 ([1,2,1,1,2])

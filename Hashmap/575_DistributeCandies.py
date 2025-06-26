"""
LeetCode #575 - Distribute Candies
Topic: Hashmap
Difficulty: Easy

PROBLEM EXPLANATION:
Alice has n candies where the i-th candy is of type candyType[i].
She can only eat n/2 candies. Return the maximum number of different
types of candies she can eat.

Example:
Input: candyType = [1,1,2,2,3,3]
Output: 3
Explanation: Alice can eat 3 candies. Best to eat one of each type: 1, 2, 3

Input: candyType = [1,1,2,3]
Output: 2
Explanation: Alice can eat 2 candies. She can eat at most 2 different types.

APPROACH:
1. Count unique candy types using a set
2. Alice can eat n/2 candies
3. Maximum types = min(unique_types, n/2)
4. If unique types > n/2, she can eat n/2 types
5. If unique types <= n/2, she can eat all unique types

Time Complexity: O(n)
Space Complexity: O(n)
"""

def distributeCandies(candyType):
    """
    Returns maximum number of different candy types Alice can eat
    """
    # Count unique candy types
    unique_types = len(set(candyType))
    
    # Maximum candies Alice can eat
    max_eat = len(candyType) // 2
    
    # Return minimum of unique types and max she can eat
    return min(unique_types, max_eat)


# Test cases
if __name__ == "__main__":
    test1 = [1, 1, 2, 2, 3, 3]
    print(f"Test 1: {distributeCandies(test1)}")  # Expected: 3
    
    test2 = [1, 1, 2, 3]
    print(f"Test 2: {distributeCandies(test2)}")  # Expected: 2
    
    test3 = [6, 6, 6, 6]
    print(f"Test 3: {distributeCandies(test3)}")  # Expected: 1
    
    test4 = [1, 2, 3, 4, 5, 6]
    print(f"Test 4: {distributeCandies(test4)}")  # Expected: 3
    
    test5 = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
    print(f"Test 5: {distributeCandies(test5)}")  # Expected: 3

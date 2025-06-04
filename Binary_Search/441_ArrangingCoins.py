"""
LeetCode #441 - Arranging Coins
Topic: Binary Search
Difficulty: Easy

PROBLEM EXPLANATION:
You have n coins and want to build a staircase. The staircase consists of k rows
where the i-th row has exactly i coins. The last row may be incomplete.
Return the number of complete rows of the staircase you can build.

Example:
Input: n = 5
Output: 2
Explanation: 
Row 1: 1 coin
Row 2: 2 coins
Total: 3 coins used, 2 coins remaining (not enough for row 3)

Input: n = 8
Output: 3
Explanation: Complete rows are 1, 2, 3 (total 6 coins), 2 coins remain

APPROACH (Binary Search):
1. We need k rows where sum of 1 to k <= n
2. Sum formula: k * (k + 1) / 2
3. Use binary search to find largest k where k*(k+1)/2 <= n
4. Search space is from 0 to n

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def arrangeCoins(n):
    """
    Returns number of complete rows
    """
    left = 0
    right = n
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        # Calculate coins needed for mid rows
        coins_needed = mid * (mid + 1) // 2
        
        if coins_needed == n:
            return mid
        elif coins_needed < n:
            # We can form mid rows, but maybe more
            result = mid
            left = mid + 1
        else:
            # Too many rows, reduce
            right = mid - 1
    
    return result


# Mathematical approach using quadratic formula
def arrangeCoins_math(n):
    """
    Using formula: k = (-1 + sqrt(1 + 8n)) / 2
    """
    import math
    return int((-1 + math.sqrt(1 + 8 * n)) / 2)


# Test cases
if __name__ == "__main__":
    print(f"Test 1: {arrangeCoins(5)}")    # Expected: 2
    print(f"Test 2: {arrangeCoins(8)}")    # Expected: 3
    print(f"Test 3: {arrangeCoins(1)}")    # Expected: 1
    print(f"Test 4: {arrangeCoins(3)}")    # Expected: 2
    print(f"Test 5: {arrangeCoins(10)}")   # Expected: 4
    print(f"Test 6: {arrangeCoins(15)}")   # Expected: 5

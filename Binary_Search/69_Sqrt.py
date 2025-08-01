"""
LeetCode #69 - Sqrt(x)
Topic: Binary Search
Difficulty: Easy

PROBLEM EXPLANATION:
Given a non-negative integer x, compute and return the square root of x.
Return the integer part (floor value) of the square root.
You cannot use built-in exponent or sqrt functions.

Example:
Input: x = 4
Output: 2

Input: x = 8
Output: 2
Explanation: sqrt(8) = 2.828..., floor is 2

APPROACH (Binary Search):
1. The square root of x is between 0 and x
2. Use binary search to find the largest number whose square <= x
3. Check if mid * mid <= x
4. If yes, it could be answer; search right for larger values
5. If no, search left for smaller values

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def mySqrt(x):
    """
    Returns the integer square root of x
    """
    if x < 2:
        return x
    
    left = 1
    right = x // 2  # sqrt(x) is at most x/2 for x >= 2
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            # mid could be answer, but check if larger value exists
            result = mid
            left = mid + 1
        else:
            # mid is too large
            right = mid - 1
    
    return result


# Test cases
if __name__ == "__main__":
    print(f"Test 1: {mySqrt(4)}")    # Expected: 2
    print(f"Test 2: {mySqrt(8)}")    # Expected: 2
    print(f"Test 3: {mySqrt(0)}")    # Expected: 0
    print(f"Test 4: {mySqrt(1)}")    # Expected: 1
    print(f"Test 5: {mySqrt(16)}")   # Expected: 4
    print(f"Test 6: {mySqrt(15)}")   # Expected: 3
    print(f"Test 7: {mySqrt(100)}")  # Expected: 10

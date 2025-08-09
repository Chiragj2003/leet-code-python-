"""
LeetCode #658 - Find K Closest Elements
Topic: Binary Search
Difficulty: Medium

PROBLEM EXPLANATION:
Given a sorted integer array arr, two integers k and x, return the k closest
integers to x in the array. Result should be sorted in ascending order.
If there's a tie, the smaller element is preferred.

Example:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

APPROACH (Binary Search for Window):
1. We need to find a window of size k
2. Use binary search to find the starting position of this window
3. The best window starts at position where arr[mid] is closer to x than arr[mid+k]
4. This ensures k closest elements

Time Complexity: O(log(n-k) + k)
Space Complexity: O(1) excluding output
"""

def findClosestElements(arr, k, x):
    """
    Returns k closest elements to x
    """
    left = 0
    right = len(arr) - k
    
    # Binary search for the starting position of k-element window
    while left < right:
        mid = (left + right) // 2
        
        # Compare distances: should we move window left or right?
        # If x is closer to arr[mid+k], move window right
        # If x is closer to arr[mid], move window left
        if x - arr[mid] > arr[mid + k] - x:
            # arr[mid+k] is closer, move window right
            left = mid + 1
        else:
            # arr[mid] is closer or equal, move window left
            right = mid
    
    # Return k elements starting from left
    return arr[left:left + k]


# Alternative: Two pointers approach
def findClosestElements_twopointers(arr, k, x):
    """
    Two pointers approach
    """
    left = 0
    right = len(arr) - 1
    
    # Remove elements from either end until k elements remain
    while right - left + 1 > k:
        # Compare distances from x
        if abs(arr[left] - x) > abs(arr[right] - x):
            left += 1
        else:
            right -= 1
    
    return arr[left:right + 1]


# Test cases
if __name__ == "__main__":
    test1 = [1, 2, 3, 4, 5]
    print(f"Test 1: {findClosestElements(test1, 4, 3)}")
    # Expected: [1, 2, 3, 4]
    
    test2 = [1, 2, 3, 4, 5]
    print(f"Test 2: {findClosestElements(test2, 4, -1)}")
    # Expected: [1, 2, 3, 4]
    
    test3 = [1, 1, 1, 10, 10, 10]
    print(f"Test 3: {findClosestElements(test3, 1, 9)}")
    # Expected: [10]
    
    test4 = [0, 1, 2, 2, 2, 3, 6, 8, 8, 9]
    print(f"Test 4: {findClosestElements(test4, 5, 9)}")
    # Expected: [3, 6, 8, 8, 9]

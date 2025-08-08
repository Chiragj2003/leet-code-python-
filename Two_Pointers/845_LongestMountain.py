"""
LeetCode #845 - Longest Mountain in Array
Topic: Two Pointers
Difficulty: Medium

PROBLEM EXPLANATION:
A mountain in an array is a sequence where:
1. Length at least 3
2. Elements strictly increase then strictly decrease
3. There must be elements on both sides of the peak

Example:
Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: [1,4,7,3,2] is the longest mountain

APPROACH (One Pass):
1. For each potential peak (arr[i] > arr[i-1] and arr[i] > arr[i+1])
2. Expand left while increasing
3. Expand right while decreasing
4. Calculate mountain length and track maximum

Time Complexity: O(n)
Space Complexity: O(1)
"""

def longestMountain(arr):
    """
    Returns length of longest mountain subarray
    """
    n = len(arr)
    if n < 3:
        return 0
    
    max_length = 0
    i = 1
    
    while i < n - 1:
        # Check if arr[i] is a peak
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            # Found a peak, expand left and right
            left = i - 1
            right = i + 1
            
            # Expand left while increasing
            while left > 0 and arr[left - 1] < arr[left]:
                left -= 1
            
            # Expand right while decreasing
            while right < n - 1 and arr[right] > arr[right + 1]:
                right += 1
            
            # Calculate mountain length
            length = right - left + 1
            max_length = max(max_length, length)
            
            # Move i to right (skip processed elements)
            i = right
        else:
            i += 1
    
    return max_length


# Test cases
if __name__ == "__main__":
    test1 = [2, 1, 4, 7, 3, 2, 5]
    print(f"Test 1: {longestMountain(test1)}")  # Expected: 5
    
    test2 = [2, 2, 2]
    print(f"Test 2: {longestMountain(test2)}")  # Expected: 0
    
    test3 = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
    print(f"Test 3: {longestMountain(test3)}")  # Expected: 11
    
    test4 = [1, 2, 3, 4, 5]
    print(f"Test 4: {longestMountain(test4)}")  # Expected: 0 (no decrease)
    
    test5 = [5, 4, 3, 2, 1]
    print(f"Test 5: {longestMountain(test5)}")  # Expected: 0 (no increase)

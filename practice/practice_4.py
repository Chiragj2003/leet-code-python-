"""
Array Problems - Practice Solutions
Collection of common array manipulation problems with detailed explanations
"""

from typing import List


# ============================================================================
# PROBLEM 1: Find Largest Element in Array
# ============================================================================
"""
Problem: Given an array, find the largest element.
Example: [3, 5, 2, 8, 1] -> 8

Approach: Iterate through array and track maximum value
Time Complexity: O(n)
Space Complexity: O(1)
"""

def largest_element(arr):
    """Find largest element by comparing each element"""
    if not arr:
        return None  # Return None if the array is empty
    
    largest = arr[0]  # Initialize with first element
    for num in arr:
        if num > largest:
            largest = num
    return largest


def largest_element_builtin(arr):
    """Find largest element using built-in max function"""
    if not arr:
        return None
    
    largest = arr[0]
    for i in range(1, len(arr)):
        largest = max(largest, arr[i])  # Compare and update maximum
    return largest


# ============================================================================
# PROBLEM 2: Find Second Largest Element in Array
# ============================================================================
"""
Problem: Find the second largest distinct element in an array.
Example: [3, 5, 2, 8, 1] -> 5

Approach: Track both first and second largest in single pass
Time Complexity: O(n)
Space Complexity: O(1)
"""

def second_largest_element(arr):
    """Find second largest element efficiently in one pass"""
    if len(arr) < 2:
        return None  # Need at least 2 elements
    
    first = second = float('-inf')  # Initialize to negative infinity
    
    for num in arr:
        if num > first:
            # Found new largest, shift first to second
            second = first
            first = num
        elif first > num > second:
            # Found new second largest
            second = num
    
    return second if second != float('-inf') else None


# ============================================================================
# PROBLEM 3: Check if Array is Sorted
# ============================================================================
"""
Problem: Check if array is sorted in ascending order (works with negative numbers too)
Example: [-10, -3, 1, 5] -> True
         [5, 3, 4] -> False

Approach: Compare each element with next element
Time Complexity: O(n)
Space Complexity: O(1)
"""

def is_sorted(arr):
    """Check if array is sorted in ascending order"""
    if not arr:
        return True  # Empty array is considered sorted
    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:  # Found unsorted pair
            return False
    return True


# ============================================================================
# PROBLEM 4: Remove Duplicates from Sorted Array (In-Place) - LeetCode 26
# ============================================================================
"""
Problem: Remove duplicates from sorted array in-place and return new length.
Example: [1, 1, 2, 2, 3] -> [1, 2, 3, _, _], return 3

Approach: Use two pointers - read and write index
Time Complexity: O(n)
Space Complexity: O(1)
"""

def remove_duplicates(arr):
    """Remove duplicates from sorted array in-place"""
    if not arr:
        return 0  # Return 0 if the array is empty
    
    write_index = 1  # Position to write next unique element
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:  # Found a new unique element
            arr[write_index] = arr[i]  # Write it to the next position
            write_index += 1
    
    return write_index  # New length of the array without duplicates


# ============================================================================
# PROBLEM 5: Right Rotate Array by K Places
# ============================================================================
"""
Problem: Rotate array to the right by k positions.
Example: [1, 2, 3, 4, 5], k=2 -> [4, 5, 1, 2, 3]

Approach: Use array slicing to move last k elements to front
Time Complexity: O(n)
Space Complexity: O(n) for new array
"""

def right_rotate(arr, k):
    """Rotate array to the right by k positions"""
    if not arr:
        return arr
    
    n = len(arr)
    k = k % n  # Handle case where k > n
    # Take last k elements and concatenate with remaining elements
    return arr[-k:] + arr[:-k]


# ============================================================================
# PROBLEM 6: Move Zeroes (LeetCode 283)
# ============================================================================
"""
Problem: Move all zeros to the end while maintaining relative order of non-zero elements.
Example: [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]

Approach 1: Move non-zeros forward, then fill with zeros
Approach 2: Swap non-zeros with zeros (more efficient)
Time Complexity: O(n)
Space Complexity: O(1)
"""

def move_zeroes_two_pass(nums: List[int]) -> None:
    """Two-pass approach: move non-zeros, then fill zeros"""
    j = 0  # Position for next non-zero element
    
    # Step 1: Move all non-zero elements forward
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1
    
    # Step 2: Fill remaining positions with zeros
    while j < len(nums):
        nums[j] = 0
        j += 1


def move_zeroes(nums: List[int]) -> None:
    """Optimal one-pass approach with swapping"""
    j = 0  # Position for next non-zero element
    
    for i in range(len(nums)):
        if nums[i] != 0:
            # Swap non-zero element with position j
            nums[i], nums[j] = nums[j], nums[i]
            j += 1


# ============================================================================
# PROBLEM 7: Linear Search
# ============================================================================
"""
Problem: Find the index of target element in array.
Example: [3, 5, 2, 8, 1], target=8 -> 3

Approach: Iterate through array until target is found
Time Complexity: O(n)
Space Complexity: O(1)
"""

def linear_search(arr, target):
    """Search for target element and return its index"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if found
    return -1  # Return -1 if not found


# ============================================================================
# PROBLEM 8: Merge Two Sorted Arrays (LeetCode 88)
# ============================================================================
"""
Problem: Merge nums2 into nums1 in-place (nums1 has enough space).
Example: nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3 -> [1,2,2,3,5,6]

Approach 1: Merge from end to avoid overwriting
Approach 2: Create new merged array with unique elements
Time Complexity: O(m + n)
Space Complexity: O(1) for approach 1, O(m + n) for approach 2
"""

def merge_sorted_arrays(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """Merge nums2 into nums1 in-place, starting from the end"""
    i = m - 1      # Last valid element in nums1
    j = n - 1      # Last element in nums2
    k = m + n - 1  # Last position in nums1
    
    # Merge from end to beginning to avoid overwriting
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]  # Take from nums1
            i -= 1
        else:
            nums1[k] = nums2[j]  # Take from nums2
            j -= 1
        k -= 1


def merge_unique(nums1, nums2):
    """Merge two sorted arrays and keep only unique elements"""
    n = len(nums1)
    m = len(nums2)
    result = []
    i = 0 
    j = 0
    
    # Merge while both arrays have elements
    while i < n and j < m:
        if nums1[i] <= nums2[j]:
            # Add only if not duplicate
            if len(result) == 0 or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
        else:
            if len(result) == 0 or result[-1] != nums2[j]:
                result.append(nums2[j])
            j += 1
    
    # Add remaining elements from nums1
    while i < n:
        if len(result) == 0 or result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1
    
    # Add remaining elements from nums2
    while j < m:
        if len(result) == 0 or result[-1] != nums2[j]:
            result.append(nums2[j])
        j += 1
    
    return result


# ============================================================================
# PROBLEM 9: Missing Number (LeetCode 268)
# ============================================================================
"""
Problem: Find the missing number in array containing n distinct numbers [0, n].
Example: [3, 0, 1] -> 2
         [0, 1] -> 2

Approach 1: Use sum formula (expected - actual)
Approach 2: Use XOR properties (a ^ a = 0, a ^ 0 = a)
Approach 3: Use frequency map
Time Complexity: O(n)
Space Complexity: O(1) for approaches 1&2, O(n) for approach 3
"""

def missing_number(arr: List[int]) -> int:
    """Find missing number using sum formula"""
    n = len(arr)
    expected_sum = n * (n + 1) // 2  # Sum of 0 to n
    actual_sum = sum(arr)
    return expected_sum - actual_sum


def missing_number_xor(arr: List[int]) -> int:
    """Find missing number using XOR (bit manipulation)"""
    n = len(arr)
    xor_all = 0  # XOR of all numbers 0 to n
    xor_arr = 0  # XOR of array elements
    
    for i in range(n + 1):
        xor_all ^= i
    
    for num in arr:
        xor_arr ^= num
    
    # Missing number will be left after XOR cancellation
    return xor_all ^ xor_arr


def missing_number_dict(arr: List[int]) -> int:
    """Find missing number using frequency map"""
    n = len(arr)
    freq = {}
    
    # Initialize all numbers as missing
    for i in range(n + 1):
        freq[i] = 0
    
    # Mark present numbers
    for num in arr:
        freq[num] = 1
    
    # Find missing number
    for k, v in freq.items():
        if v == 0:
            return k


# ============================================================================
# PROBLEM 10: Max Consecutive Ones (LeetCode 485)
# ============================================================================
"""
Problem: Find the maximum number of consecutive 1s in binary array.
Example: [1, 1, 0, 1, 1, 1] -> 3

Approach: Track current and maximum consecutive count
Time Complexity: O(n)
Space Complexity: O(1)
"""

def find_max_consecutive_ones(nums: List[int]) -> int:
    """Find maximum consecutive 1s in array"""
    max_count = 0      # Maximum consecutive 1s found
    current_count = 0  # Current consecutive 1s
    
    for num in nums:
        if num == 1:
            current_count += 1  # Increment consecutive count
            max_count = max(max_count, current_count)
        else:
            current_count = 0  # Reset on encountering 0
    
    return max_count


# ============================================================================
# PROBLEM 11: Two Sum (LeetCode 1)
# ============================================================================
"""
Problem: Find two numbers that add up to target.
Example: [2, 7, 11, 15], target=9 -> (2, 7)

Approach 1: Brute force - check all pairs
Approach 2: Hash map - store complements
Time Complexity: O(n²) for brute force, O(n) for hash map
Space Complexity: O(1) for brute force, O(n) for hash map
"""

def two_sum_brute(arr, target):
    """Brute force approach - check all pairs"""
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return (arr[i], arr[j])
    return None


def two_sum_hash(arr, target):
    """Optimized approach using hash map"""
    seen = {}  # Store numbers we've seen
    
    for num in arr:
        complement = target - num  # What we need to find
        if complement in seen:
            return (complement, num)  # Found the pair
        seen[num] = True  # Mark current number as seen
    
    return None


# ============================================================================
# PROBLEM 12: Maximum Subarray Sum (LeetCode 53 - Kadane's Algorithm)
# ============================================================================
"""
Problem: Find contiguous subarray with largest sum.
Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> 6 (subarray [4, -1, 2, 1])

Approach 1: Kadane's Algorithm (optimal)
Approach 2: Brute force - check all subarrays
Time Complexity: O(n) for Kadane's, O(n³) for brute force
Space Complexity: O(1)
"""

def maximum_subarray(arr: List[int]) -> int:
    """Kadane's Algorithm - optimal solution"""
    if not arr:
        return 0
    
    max_current = max_global = arr[0]
    
    for i in range(1, len(arr)):
        # Either extend existing subarray or start new one
        max_current = max(arr[i], max_current + arr[i])
        
        # Update global maximum
        if max_current > max_global:
            max_global = max_current
    
    return max_global


def maximum_subarray_brute(arr: List[int]) -> int:
    """Brute force approach - check all possible subarrays"""
    n = len(arr)
    max_sum = float('-inf')
    
    for i in range(n):
        for j in range(i, n):
            current_sum = sum(arr[i:j+1])  # Sum of subarray [i, j]
            max_sum = max(max_sum, current_sum)
    
    return max_sum


# ============================================================================
# LeetCode Style Solutions
# ============================================================================

class Solution:
    """LeetCode format solutions for common problems"""
    
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Move Zeroes - LeetCode 283
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
    
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Maximum Subarray - LeetCode 53
        Kadane's Algorithm implementation
        """
        current_sum = nums[0]  # Current subarray sum
        max_sum = nums[0]      # Maximum sum found so far

        for i in range(1, len(nums)):
            # Key decision: extend current subarray or start fresh
            current_sum = max(nums[i], current_sum + nums[i])
            # Update maximum
            max_sum = max(max_sum, current_sum)

        return max_sum
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge Sorted Array - LeetCode 88
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
    
    def missingNumber(self, nums: List[int]) -> int:
        """
        Missing Number - LeetCode 268
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
    
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Max Consecutive Ones - LeetCode 485
        """
        max_count = 0
        current_count = 0
        
        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
        
        return max_count


# ============================================================================
# Example Test Cases
# ============================================================================

if __name__ == "__main__":
    print("="*60)
    print("ARRAY PROBLEMS - TEST CASES")
    print("="*60)
    
    # Test 1: Largest element
    print("\n1. Largest Element:")
    print(f"   Input: [3, 5, 2, 8, 1]")
    print(f"   Output: {largest_element([3, 5, 2, 8, 1])}")  # Expected: 8
    
    # Test 2: Second largest
    print("\n2. Second Largest Element:")
    print(f"   Input: [3, 5, 2, 8, 1]")
    print(f"   Output: {second_largest_element([3, 5, 2, 8, 1])}")  # Expected: 5
    
    # Test 3: Is sorted
    print("\n3. Check if Array is Sorted:")
    print(f"   Input: [1, 2, 3, 4, 5]")
    print(f"   Output: {is_sorted([1, 2, 3, 4, 5])}")  # Expected: True
    print(f"   Input: [5, 3, 4]")
    print(f"   Output: {is_sorted([5, 3, 4])}")  # Expected: False
    
    # Test 4: Remove duplicates
    print("\n4. Remove Duplicates:")
    arr = [1, 1, 2, 2, 3, 3, 3, 4]
    length = remove_duplicates(arr)
    print(f"   Input: [1, 1, 2, 2, 3, 3, 3, 4]")
    print(f"   Output: {arr[:length]}, Length: {length}")  # Expected: [1, 2, 3, 4], 4
    
    # Test 5: Right rotate
    print("\n5. Right Rotate Array:")
    print(f"   Input: [1, 2, 3, 4, 5], k=2")
    print(f"   Output: {right_rotate([1, 2, 3, 4, 5], 2)}")  # Expected: [4, 5, 1, 2, 3]
    
    # Test 6: Move zeroes
    print("\n6. Move Zeroes:")
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    print(f"   Input: [0, 1, 0, 3, 12]")
    print(f"   Output: {nums}")  # Expected: [1, 3, 12, 0, 0]
    
    # Test 7: Linear search
    print("\n7. Linear Search:")
    print(f"   Input: [3, 5, 2, 8, 1], target=8")
    print(f"   Output: {linear_search([3, 5, 2, 8, 1], 8)}")  # Expected: 3
    
    # Test 8: Missing number
    print("\n8. Missing Number:")
    print(f"   Input: [3, 0, 1]")
    print(f"   Output: {missing_number([3, 0, 1])}")  # Expected: 2
    
    # Test 9: Max consecutive ones
    print("\n9. Max Consecutive Ones:")
    print(f"   Input: [1, 1, 0, 1, 1, 1]")
    print(f"   Output: {find_max_consecutive_ones([1, 1, 0, 1, 1, 1])}")  # Expected: 3
    
    # Test 10: Two sum
    print("\n10. Two Sum:")
    print(f"    Input: [2, 7, 11, 15], target=9")
    print(f"    Output: {two_sum_hash([2, 7, 11, 15], 9)}")  # Expected: (2, 7)
    
    # Test 11: Maximum subarray
    print("\n11. Maximum Subarray Sum (Kadane's Algorithm):")
    print(f"    Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]")
    print(f"    Output: {maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])}")  # Expected: 6
    
    print("\n" + "="*60)
    print("All tests completed!")
    print("="*60)




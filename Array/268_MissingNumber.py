"""
LeetCode #268 - Missing Number
Topic: Array / Math
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Given array of n numbers from 0 to n, find the missing number.

Example:
[3,0,1] -> Missing 2 (should have 0,1,2,3)
[0,1] -> Missing 2
[9,6,4,2,3,5,7,0,1] -> Missing 8

Think of it like:
You have numbered tickets 0 to 10, but one is missing.
Find which number is missing!

WHY THIS WORKS (Simple Explanation):
Multiple approaches:

1. MATH: Sum of 0 to n is n*(n+1)/2
   Missing = Expected sum - Actual sum

2. XOR: XOR has special property: a ^ a = 0, a ^ 0 = a
   XOR all numbers with all indices, missing remains!

3. SORT: Sort and find first gap

Time Complexity: O(n) for math/XOR, O(n log n) for sort
Space Complexity: O(1)
"""

def missingNumber(nums):
    """
    Find missing number using math formula
    
    Sum of 0 to n = n * (n+1) / 2
    
    Visual example: [3, 0, 1]
    n = 3 (since we have 3 numbers, should have 0,1,2,3)
    Expected sum = 3 * 4 / 2 = 6
    Actual sum = 3 + 0 + 1 = 4
    Missing = 6 - 4 = 2 ✓
    """
    n = len(nums)
    
    # Expected sum of 0 to n
    expected_sum = n * (n + 1) // 2
    
    # Actual sum
    actual_sum = sum(nums)
    
    # Missing number
    return expected_sum - actual_sum


def missingNumber_xor(nums):
    """
    Find missing number using XOR
    
    XOR properties:
    - a ^ a = 0 (same numbers cancel out)
    - a ^ 0 = a (XOR with 0 gives original)
    - Order doesn't matter
    
    Visual example: [3, 0, 1]
    
    XOR all array elements: 3 ^ 0 ^ 1
    XOR with all indices: 0 ^ 1 ^ 2 ^ 3
    
    Combined: 0^0 ^ 1^1 ^ 2 ^ 3^3 = 0 ^ 0 ^ 2 ^ 0 = 2
    
    Pairs cancel out, missing number remains!
    """
    n = len(nums)
    result = n  # Start with n
    
    for i, num in enumerate(nums):
        result ^= i ^ num  # XOR with index and value
    
    return result


def missingNumber_set(nums):
    """
    Find missing number using set
    
    Simple but uses O(n) space:
    1. Create set of all numbers 0 to n
    2. Remove all numbers in array
    3. Remaining number is missing
    """
    n = len(nums)
    num_set = set(range(n + 1))
    
    for num in nums:
        num_set.remove(num)
    
    return num_set.pop()


def missingNumber_verbose(nums):
    """
    Detailed version showing the math approach
    """
    n = len(nums)
    
    print(f"Array: {nums}")
    print(f"Length: {n}")
    print(f"\nShould have numbers from 0 to {n}")
    
    # Expected sum
    expected_sum = n * (n + 1) // 2
    print(f"\nExpected sum (0 to {n}): {n} * {n+1} / 2 = {expected_sum}")
    
    # Actual sum
    actual_sum = sum(nums)
    print(f"Actual sum: {' + '.join(map(str, nums))} = {actual_sum}")
    
    # Missing
    missing = expected_sum - actual_sum
    print(f"\nMissing number: {expected_sum} - {actual_sum} = {missing}")
    
    return missing


def missingNumber_xor_verbose(nums):
    """
    Detailed version showing XOR approach
    """
    n = len(nums)
    
    print(f"Array: {nums}")
    print(f"Length: {n}")
    print(f"\nShould have numbers from 0 to {n}")
    
    print("\n=== XOR Approach ===")
    print("XOR all indices with all values")
    print("Pairs will cancel out (a ^ a = 0)")
    print("Missing number will remain!\n")
    
    result = n
    print(f"Start with n={n}: result = {result} (binary: {bin(result)})")
    
    for i, num in enumerate(nums):
        old_result = result
        result ^= i ^ num
        print(f"Step {i+1}: result ^= {i} ^ {num}")
        print(f"  {old_result} ^ {i} ^ {num} = {result} (binary: {bin(result)})")
    
    print(f"\nMissing number: {result}")
    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ([0], 1),
        ([1], 0),
    ]
    
    print("=== Testing Math Solution ===")
    for nums, expected in test_cases:
        result = missingNumber(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {nums}")
        print(f"   Missing: {result} (Expected: {expected})")
        print()
    
    print("=== Testing XOR Solution ===")
    for nums, expected in test_cases:
        result = missingNumber_xor(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {nums} -> Missing: {result}")
    
    print("\n=== Testing Set Solution ===")
    for nums, expected in test_cases:
        result = missingNumber_set(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {nums} -> Missing: {result}")
    
    print("\n=== Verbose Example (Math) ===")
    missingNumber_verbose([3, 0, 1])
    
    print("\n" + "="*50)
    print("=== Verbose Example (XOR) ===")
    missingNumber_xor_verbose([3, 0, 1])

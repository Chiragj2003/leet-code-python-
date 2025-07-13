"""
LeetCode #238 - Product of Array Except Self
Topic: Array
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Return array where each element is the product of all other elements.

Example:
[1,2,3,4] -> [24,12,8,6]
Explanation:
- Position 0: 2*3*4 = 24
- Position 1: 1*3*4 = 12
- Position 2: 1*2*4 = 8
- Position 3: 1*2*3 = 6

Think of it like:
For each number, multiply everything else EXCEPT that number!

WHY THIS WORKS (Simple Explanation):
For each position, answer = (product of all left elements) * (product of all right elements)

Use two passes:
1. Left pass: Calculate products of all elements to the LEFT
2. Right pass: Calculate products of all elements to the RIGHT
3. Multiply left and right for each position

Like looking at products from both directions!

Constraint: Don't use division, do it in O(n) time

Time Complexity: O(n) - two passes
Space Complexity: O(1) - output array doesn't count as extra space
"""

def productExceptSelf(nums):
    """
    Calculate product of all elements except self
    
    Visual example: [1, 2, 3, 4]
    
    Step 1 - Left products (product of all elements to the left):
    Position 0: nothing to left -> 1
    Position 1: 1 to left -> 1
    Position 2: 1*2 to left -> 2
    Position 3: 1*2*3 to left -> 6
    Left = [1, 1, 2, 6]
    
    Step 2 - Right products (product of all elements to the right):
    Position 3: nothing to right -> 1
    Position 2: 4 to right -> 4
    Position 1: 3*4 to right -> 12
    Position 0: 2*3*4 to right -> 24
    
    Final: Multiply left * right at each position
    Position 0: 1 * 24 = 24
    Position 1: 1 * 12 = 12
    Position 2: 2 * 4 = 8
    Position 3: 6 * 1 = 6
    
    Result: [24, 12, 8, 6]
    """
    n = len(nums)
    result = [1] * n
    
    # Calculate left products
    # result[i] = product of all elements to left of i
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]
    
    # Calculate right products and multiply with left
    # Multiply result[i] with product of all elements to right of i
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result


def productExceptSelf_verbose(nums):
    """
    Detailed version showing each step
    """
    n = len(nums)
    result = [1] * n
    
    print(f"Input: {nums}\n")
    
    # Left pass
    print("=== LEFT PASS (products of elements to the left) ===")
    left_product = 1
    for i in range(n):
        result[i] = left_product
        print(f"Position {i}: left_product = {left_product}, result[{i}] = {result[i]}")
        left_product *= nums[i]
        print(f"  Update left_product: {left_product} (multiply by nums[{i}]={nums[i]})")
    
    print(f"\nAfter left pass: {result}\n")
    
    # Right pass
    print("=== RIGHT PASS (multiply with products of elements to the right) ===")
    right_product = 1
    for i in range(n - 1, -1, -1):
        print(f"Position {i}: result[{i}] = {result[i]}, right_product = {right_product}")
        result[i] *= right_product
        print(f"  After multiply: result[{i}] = {result[i]}")
        right_product *= nums[i]
        print(f"  Update right_product: {right_product} (multiply by nums[{i}]={nums[i]})")
    
    print(f"\nFinal result: {result}\n")
    return result


def productExceptSelf_with_division(nums):
    """
    ALTERNATIVE (if division was allowed):
    1. Calculate total product
    2. Divide by each element
    
    Problem: What if there's a 0 in array?
    This is why the question forbids division!
    """
    # Calculate total product
    total_product = 1
    zero_count = 0
    
    for num in nums:
        if num == 0:
            zero_count += 1
        else:
            total_product *= num
    
    result = []
    for num in nums:
        if zero_count > 1:
            # Multiple zeros -> all products are 0
            result.append(0)
        elif zero_count == 1:
            # One zero -> only that position has product
            if num == 0:
                result.append(total_product)
            else:
                result.append(0)
        else:
            # No zeros -> divide total by current
            result.append(total_product // num)
    
    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([2, 3, 4, 5], [60, 40, 30, 24]),
        ([1, 1], [1, 1]),
    ]
    
    print("=== Testing Optimal Solution (No Division) ===")
    for nums, expected in test_cases:
        result = productExceptSelf(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {nums}")
        print(f"   Output: {result}")
        print(f"   Expected: {expected}")
        print()
    
    print("=== Verbose Example ===")
    productExceptSelf_verbose([1, 2, 3, 4])

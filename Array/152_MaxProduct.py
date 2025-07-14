"""
LeetCode #152 - Maximum Product Subarray
Topic: Array (Dynamic Programming)
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Find contiguous subarray with largest product.

Example:
[2,3,-2,4] -> [2,3] has product = 6

Think of it like:
Multiplying numbers along a path. Watch out for negatives!
Two negatives make a positive, so track both min and max products.

WHY THIS WORKS (Simple Explanation):
Track BOTH minimum and maximum products ending at current position:
- Maximum * positive = new maximum
- Minimum * negative = new maximum (negative × negative = positive!)

So we need to track both!

Example: [2, 3, -2, 4]
At -2: min=-12 (3*-2), max=6 (2*3)
At 4: min=-8, max=48 (because -12*4=48... wait, -12*-2=24!)

Time Complexity: O(n) - single pass
Space Complexity: O(1) - only tracking min/max
"""

def maxProduct(nums):
    """
    Find maximum product subarray
    
    Visual example: [2, 3, -2, 4]
    
    i=0: num=2
      max_prod = 2, min_prod = 2, result = 2
    
    i=1: num=3
      candidates: 3, 2*3=6, 2*3=6
      max_prod = 6, min_prod = 3, result = 6
    
    i=2: num=-2
      candidates: -2, 6*-2=-12, 3*-2=-6
      max_prod = -2, min_prod = -12, result = 6
    
    i=3: num=4
      candidates: 4, -2*4=-8, -12*4=-48
      max_prod = 4, min_prod = -48, result = 6
    
    Result: 6 (subarray [2,3])
    """
    if not nums:
        return 0
    
    # Initialize with first element
    max_prod = min_prod = result = nums[0]
    
    for num in nums[1:]:
        # When multiplying by negative, max and min swap!
        # So we need to consider all three: num itself, max*num, min*num
        candidates = (num, max_prod * num, min_prod * num)
        
        max_prod = max(candidates)
        min_prod = min(candidates)
        
        # Track overall maximum
        result = max(result, max_prod)
    
    return result


def maxProduct_verbose(nums):
    """
    Detailed version showing the logic
    """
    if not nums:
        return 0
    
    print(f"Array: {nums}\n")
    
    max_prod = min_prod = result = nums[0]
    print(f"Initialize: max_prod={max_prod}, min_prod={min_prod}, result={result}\n")
    
    for i, num in enumerate(nums[1:], 1):
        print(f"Step {i}: num = {num}")
        
        # Calculate all candidates
        temp_max = max_prod * num
        temp_min = min_prod * num
        
        print(f"  Candidates:")
        print(f"    Just num: {num}")
        print(f"    max_prod * num: {max_prod} * {num} = {temp_max}")
        print(f"    min_prod * num: {min_prod} * {num} = {temp_min}")
        
        # Update max and min
        max_prod = max(num, temp_max, temp_min)
        min_prod = min(num, temp_max, temp_min)
        
        print(f"  New max_prod: {max_prod}")
        print(f"  New min_prod: {min_prod}")
        
        # Update result
        if max_prod > result:
            result = max_prod
            print(f"  NEW BEST RESULT: {result} ✓")
        
        print()
    
    print(f"Final result: {result}")
    return result


def maxProduct_handle_zero(nums):
    """
    Alternative approach explicitly handling zeros
    
    Zero breaks the product chain, so reset at zeros
    """
    result = nums[0]
    curr_max = curr_min = 1
    
    for num in nums:
        if num == 0:
            # Zero resets everything
            curr_max = curr_min = 1
            result = max(result, 0)
            continue
        
        # Store old max (needed for min calculation)
        temp = curr_max
        
        # Update max and min
        curr_max = max(num, num * curr_max, num * curr_min)
        curr_min = min(num, num * temp, num * curr_min)
        
        result = max(result, curr_max)
    
    return result


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([2, 3, -2, 4], 6),          # [2,3]
        ([-2], -2),                   # [-2]
        ([0, 2], 2),                  # [2]
        ([-2, 0, -1], 0),             # [0]
        ([-2, 3, -4], 24),            # [-2,3,-4]
        ([2, -5, -2, -4, 3], 24),     # [-5,-2,-4]
    ]
    
    print("=== Testing Standard Solution ===")
    for nums, expected in test_cases:
        result = maxProduct(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {nums}")
        print(f"   Max Product: {result} (Expected: {expected})")
        print()
    
    print("=== Verbose Example ===")
    maxProduct_verbose([2, 3, -2, 4])

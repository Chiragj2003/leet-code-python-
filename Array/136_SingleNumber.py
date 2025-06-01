"""
LeetCode #136 - Single Number
Topic: Array / Bit Manipulation
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Every element appears twice except one. Find that single element.

Example:
[2,2,1] -> 1
[4,1,2,1,2] -> 4

Think of it like:
Everyone has a partner except one person.
Find the person without a partner!

WHY THIS WORKS (Simple Explanation):
Use XOR (Exclusive OR) bit operation!

XOR properties:
- a ^ a = 0 (same numbers cancel out)
- a ^ 0 = a (XOR with 0 gives original)
- Order doesn't matter

If you XOR all numbers, pairs cancel out, single remains!

Example: [4, 1, 2, 1, 2]
4 ^ 1 ^ 2 ^ 1 ^ 2
= 4 ^ (1^1) ^ (2^2)
= 4 ^ 0 ^ 0
= 4 ✓

Time Complexity: O(n) - single pass
Space Complexity: O(1) - only one variable
"""

def singleNumber(nums):
    """
    Find single number using XOR
    
    Visual example: [4, 1, 2, 1, 2]
    
    result = 0
    XOR 4: result = 0 ^ 4 = 4
    XOR 1: result = 4 ^ 1 = 5
    XOR 2: result = 5 ^ 2 = 7
    XOR 1: result = 7 ^ 1 = 6 (second 1 starts canceling)
    XOR 2: result = 6 ^ 2 = 4 (second 2 cancels, back to 4!)
    
    All pairs cancel, single number remains!
    """
    result = 0
    for num in nums:
        result ^= num
    return result


def singleNumber_hashmap(nums):
    """
    Alternative: Use hashmap to count frequencies
    
    Simpler to understand but uses O(n) space
    """
    from collections import Counter
    
    counts = Counter(nums)
    
    for num, count in counts.items():
        if count == 1:
            return num


def singleNumber_set(nums):
    """
    Alternative: Use set math
    
    2 * (sum of unique numbers) - (sum of all numbers) = single number
    
    Example: [4, 1, 2, 1, 2]
    Unique: {4, 1, 2}, sum = 7
    All: 4+1+2+1+2 = 10
    Result: 2*7 - 10 = 14 - 10 = 4
    """
    return 2 * sum(set(nums)) - sum(nums)


def singleNumber_verbose(nums):
    """
    Detailed version showing XOR process
    """
    print(f"Array: {nums}")
    print("\n=== XOR Approach ===")
    print("Properties: a^a=0, a^0=a")
    print("All pairs will cancel out!\n")
    
    result = 0
    print(f"Start: result = {result} (binary: {bin(result)})")
    
    for i, num in enumerate(nums):
        old_result = result
        result ^= num
        print(f"Step {i+1}: {old_result} ^ {num} = {result}")
        print(f"  Binary: {bin(old_result)} ^ {bin(num)} = {bin(result)}")
    
    print(f"\nSingle number: {result}")
    return result


def singleNumber_visual_pairs(nums):
    """
    Visual representation showing which numbers pair up
    """
    from collections import defaultdict
    
    print(f"Array: {nums}")
    print("\nFinding pairs:")
    
    seen = defaultdict(list)
    for i, num in enumerate(nums):
        seen[num].append(i)
    
    for num, indices in sorted(seen.items()):
        if len(indices) == 1:
            print(f"  {num} appears at index {indices[0]} - NO PAIR (Single!) ✓")
        else:
            print(f"  {num} appears at indices {indices} - PAIR (cancels out)")
    
    return singleNumber(nums)


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
        ([1, 3, 1, -1, 3], -1),
    ]
    
    print("=== Testing XOR Solution ===")
    for nums, expected in test_cases:
        result = singleNumber(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {nums}")
        print(f"   Single number: {result} (Expected: {expected})")
        print()
    
    print("=== Testing Hashmap Solution ===")
    for nums, expected in test_cases:
        result = singleNumber_hashmap(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} {nums} -> {result}")
    
    print("\n=== Testing Set Math Solution ===")
    for nums, expected in test_cases:
        result = singleNumber_set(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} {nums} -> {result}")
    
    print("\n=== Verbose Example ===")
    singleNumber_verbose([4, 1, 2, 1, 2])
    
    print("\n" + "="*50)
    print("=== Visual Pairing Example ===")
    result = singleNumber_visual_pairs([4, 1, 2, 1, 2])
    print(f"\nResult: {result}")

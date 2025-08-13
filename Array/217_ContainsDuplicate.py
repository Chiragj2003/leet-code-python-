"""
LeetCode #217 - Contains Duplicate
Topic: Array / Hashmap
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Check if array has any duplicate values.

Example:
[1,2,3,1] -> True (1 appears twice)
[1,2,3,4] -> False (all unique)

Think of it like:
Checking if anyone has the same name in a class.
As you meet each person, remember their name!

WHY THIS WORKS (Simple Explanation):
Use a Set to track seen numbers:
1. Go through array one by one
2. Check if number already in set
3. If yes -> found duplicate!
4. If no -> add to set and continue

Like checking attendance - if name already checked off, it's a duplicate!

Time Complexity: O(n) - visit each element once
Space Complexity: O(n) - set can store all elements
"""

def containsDuplicate(nums):
    """
    Check for duplicates using set
    
    Visual example: [1, 2, 3, 1]
    
    Step 1: num=1, seen={}, add 1 -> seen={1}
    Step 2: num=2, seen={1}, add 2 -> seen={1,2}
    Step 3: num=3, seen={1,2}, add 3 -> seen={1,2,3}
    Step 4: num=1, seen={1,2,3}, 1 already in set! -> Duplicate found! ✓
    """
    # Set to track numbers we've seen
    seen = set()
    
    for num in nums:
        # If we've seen this number before -> duplicate!
        if num in seen:
            return True
        
        # Remember this number
        seen.add(num)
    
    # No duplicates found
    return False


def containsDuplicate_pythonic(nums):
    """
    Pythonic one-liner solution
    
    If set size < list size, there must be duplicates!
    Set automatically removes duplicates.
    """
    return len(nums) != len(set(nums))


def containsDuplicate_sort(nums):
    """
    Alternative: Sort first, then check adjacent elements
    
    After sorting, duplicates will be next to each other!
    [1,2,3,1] -> [1,1,2,3] -> adjacent 1's are duplicates
    
    Time: O(n log n) for sorting
    Space: O(1) if sorting in-place
    """
    if len(nums) <= 1:
        return False
    
    # Sort the array
    nums_sorted = sorted(nums)
    
    # Check adjacent elements
    for i in range(len(nums_sorted) - 1):
        if nums_sorted[i] == nums_sorted[i + 1]:
            return True
    
    return False


def containsDuplicate_verbose(nums):
    """
    Detailed version showing the process
    """
    seen = set()
    
    print(f"Checking array: {nums}\n")
    
    for i, num in enumerate(nums):
        print(f"Step {i+1}: Checking number {num}")
        print(f"  Already seen: {sorted(seen)}")
        
        if num in seen:
            print(f"  DUPLICATE FOUND! {num} was seen before ✗")
            return True
        
        seen.add(num)
        print(f"  Added {num} to seen set ✓")
        print()
    
    print("No duplicates found ✓")
    return False


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([], False),
        ([1], False),
    ]
    
    print("=== Testing Set Solution ===")
    for nums, expected in test_cases:
        result = containsDuplicate(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {nums}")
        print(f"   Has Duplicate: {result} (Expected: {expected})")
        print()
    
    print("=== Testing Pythonic Solution ===")
    for nums, expected in test_cases:
        result = containsDuplicate_pythonic(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {nums} -> {result}")
    
    print("\n=== Testing Sort Solution ===")
    for nums, expected in test_cases:
        result = containsDuplicate_sort(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {nums} -> {result}")
    
    print("\n=== Verbose Example ===")
    containsDuplicate_verbose([1, 2, 3, 1])

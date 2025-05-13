"""
LeetCode #278 - First Bad Version
Topic: Binary Search
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
You're a developer and you have n versions: 1, 2, 3, ..., n
One version is bad and all versions after it are also bad.
Find the first bad version using minimum API calls!

Example:
Input: n = 5, bad = 4
Output: 4
Explanation: Version 4 is first bad, versions 4 and 5 are bad

WHY THIS WORKS (Simple Explanation):
Use binary search!
- If middle version is bad, first bad is at middle or before
- If middle version is good, first bad is after middle
- Keep narrowing down until we find the first bad version

Time Complexity: O(log n) - binary search
Space Complexity: O(1) - only a few variables
"""

# This is the API provided (in actual problem, this is given)
def isBadVersion(version):
    """
    Simulated API call to check if version is bad
    In real problem, this function is provided
    """
    # For testing, let's say version 4 onwards is bad
    return version >= 4


def firstBadVersion(n):
    """
    Find first bad version using binary search
    
    Think of it like:
    - Versions: [Good, Good, Good, Bad, Bad, Bad]
    - We want to find first Bad
    - Use binary search: if mid is Bad, answer is mid or before
    - If mid is Good, answer is after mid
    """
    left = 1
    right = n
    
    while left < right:
        mid = left + (right - left) // 2  # Avoid overflow
        
        if isBadVersion(mid):
            # Mid is bad, so first bad is at mid or before
            right = mid
        else:
            # Mid is good, so first bad is after mid
            left = mid + 1
    
    # When left == right, we found the first bad version
    return left


# Alternative approach with clearer logic
def firstBadVersion_v2(n):
    """
    Same logic, different style
    """
    left = 1
    right = n
    result = n  # Initialize with last version
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if isBadVersion(mid):
            result = mid  # This could be the answer
            right = mid - 1  # But check if there's an earlier bad version
        else:
            left = mid + 1  # First bad is definitely after mid
    
    return result


# Test cases with explanations
if __name__ == "__main__":
    # Note: For testing, we've set bad version to 4 in isBadVersion
    
    print(f"Test 1: {firstBadVersion(5)}")
    # Expected: 4 - versions 4 and 5 are bad
    
    print(f"Test 2: {firstBadVersion(1)}")
    # Expected: 1 - only one version
    
    print(f"Test 3: {firstBadVersion(10)}")
    # Expected: 4 - with our test setup

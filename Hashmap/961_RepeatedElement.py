"""
LeetCode #961 - N-Repeated Element in Size 2N Array
Topic: Hashmap
Difficulty: Easy

PROBLEM EXPLANATION:
You are given an integer array nums with the following properties:
- nums.length == 2 * n
- nums contains n + 1 unique elements
- Exactly one element is repeated n times
Return the element that is repeated n times.

Example:
Input: nums = [1,2,3,3]
Output: 3

Input: nums = [2,1,2,5,3,2]
Output: 2

Input: nums = [5,1,5,2,5,3,5,4]
Output: 5

APPROACH 1 (Hashmap):
1. Count frequency of each element
2. Return element with count = n (where n = len(nums)/2)

Time Complexity: O(n)
Space Complexity: O(n)

APPROACH 2 (Set - Optimized):
1. Use a set to track seen elements
2. First duplicate found is the answer (it's repeated n times)

Time Complexity: O(n)
Space Complexity: O(n) worst case, but often O(1) since we find duplicate early
"""

from collections import Counter

def repeatedNTimes(nums):
    """
    Returns element repeated n times (hashmap approach)
    """
    n = len(nums) // 2
    count = Counter(nums)
    
    for num, freq in count.items():
        if freq == n:
            return num


def repeatedNTimes_v2(nums):
    """
    Returns element repeated n times (set approach - optimized)
    """
    seen = set()
    
    for num in nums:
        if num in seen:
            return num
        seen.add(num)


def repeatedNTimes_v3(nums):
    """
    Smart approach: Check nearby elements
    Since element appears n times in 2n array, it must appear
    within every 3 consecutive elements
    """
    for i in range(len(nums) - 2):
        # Check if any of 3 consecutive elements repeat
        if nums[i] == nums[i+1] or nums[i] == nums[i+2]:
            return nums[i]
    
    # Edge case: only nums[-1] == nums[-2] left
    return nums[-1]


# Test cases
if __name__ == "__main__":
    test1 = [1, 2, 3, 3]
    print(f"Test 1: {repeatedNTimes_v2(test1)}")  # Expected: 3
    
    test2 = [2, 1, 2, 5, 3, 2]
    print(f"Test 2: {repeatedNTimes_v2(test2)}")  # Expected: 2
    
    test3 = [5, 1, 5, 2, 5, 3, 5, 4]
    print(f"Test 3: {repeatedNTimes_v2(test3)}")  # Expected: 5
    
    test4 = [9, 5, 6, 9]
    print(f"Test 4: {repeatedNTimes_v2(test4)}")  # Expected: 9

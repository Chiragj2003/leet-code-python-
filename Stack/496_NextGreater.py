"""
LeetCode #496 - Next Greater Element I
Topic: Stack (Monotonic Stack)
Difficulty: Easy

PROBLEM EXPLANATION:
You are given two arrays nums1 and nums2 where nums1 is a subset of nums2.
For each element in nums1, find the next greater element in nums2.
The next greater element is the first greater element to the right.
If it doesn't exist, return -1 for that element.

Example:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation:
- 4: No greater element to right in nums2 -> -1
- 1: Next greater is 3 -> 3
- 2: No greater element to right -> -1

APPROACH (Monotonic Stack + HashMap):
1. Use a stack to find next greater element for all elements in nums2
2. Store results in hashmap: element -> next_greater
3. For each element in nums1, look up in hashmap

Time Complexity: O(n + m)
Space Complexity: O(n)
"""

def nextGreaterElement(nums1, nums2):
    """
    Returns array of next greater elements
    """
    # HashMap to store element -> next greater element
    next_greater = {}
    stack = []
    
    # Process nums2 to find next greater for each element
    for num in nums2:
        # Pop elements smaller than current (found their next greater)
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)
    
    # Elements remaining in stack have no next greater
    while stack:
        next_greater[stack.pop()] = -1
    
    # Build result for nums1
    return [next_greater[num] for num in nums1]


# Test cases
if __name__ == "__main__":
    test1_nums1 = [4, 1, 2]
    test1_nums2 = [1, 3, 4, 2]
    print(f"Test 1: {nextGreaterElement(test1_nums1, test1_nums2)}")
    # Expected: [-1, 3, -1]
    
    test2_nums1 = [2, 4]
    test2_nums2 = [1, 2, 3, 4]
    print(f"Test 2: {nextGreaterElement(test2_nums1, test2_nums2)}")
    # Expected: [3, -1]
    
    test3_nums1 = [1, 3, 5, 2, 4]
    test3_nums2 = [6, 5, 4, 3, 2, 1, 7]
    print(f"Test 3: {nextGreaterElement(test3_nums1, test3_nums2)}")
    # Expected: [7, 7, 7, 7, 7]

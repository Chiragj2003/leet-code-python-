"""
LeetCode #553 - Optimal Division
Topic: String / Math
Difficulty: Medium

PROBLEM EXPLANATION:
Given an array of positive integers, divide them in order to get
the maximum result. Add parentheses to achieve the maximum.

Example:
Input: nums = [1000,100,10,2]
Output: "1000/(100/10/2)"
Explanation: 1000/(100/10/2) = 1000/5 = 200
Without parentheses: 1000/100/10/2 = 0.05

APPROACH (Math Trick):
Key insight: To maximize a/b/c/d..., we want to minimize the denominator.
The minimum denominator is b/(c/d/...) = b/c*d*... = (b/c)/d/...

So optimal is always: nums[0]/(nums[1]/nums[2]/...nums[n-1])

Special cases:
- 1 number: return as is
- 2 numbers: return "a/b"
- 3+ numbers: return "a/(b/c/d/...)"

Time Complexity: O(n)
Space Complexity: O(n)
"""

def optimalDivision(nums):
    """
    Returns the division expression with maximum result
    """
    if len(nums) == 1:
        return str(nums[0])
    
    if len(nums) == 2:
        return f"{nums[0]}/{nums[1]}"
    
    # For 3+ numbers: a/(b/c/d/...)
    result = str(nums[0]) + "/("
    result += "/".join(map(str, nums[1:]))
    result += ")"
    
    return result


# Test cases
if __name__ == "__main__":
    test1 = [1000, 100, 10, 2]
    print(f"Test 1: {optimalDivision(test1)}")
    # Expected: "1000/(100/10/2)"
    
    test2 = [2, 3, 4]
    print(f"Test 2: {optimalDivision(test2)}")
    # Expected: "2/(3/4)"
    
    test3 = [2]
    print(f"Test 3: {optimalDivision(test3)}")
    # Expected: "2"
    
    test4 = [6, 2]
    print(f"Test 4: {optimalDivision(test4)}")
    # Expected: "6/2"

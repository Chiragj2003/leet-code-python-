"""

              LeetCode #553 - Optimal Division                                
              Topic: String/Math | Difficulty: Medium                         
              Company: Amazon                                                 


PROBLEM: Add parentheses to maximize result of division expression.

Example:
  [1000,100,10,2]  "1000/(100/10/2)" = 1000/5 = 200
  (Without parens: 1000/100/10/2 = 0.05)
"""

#  SOLUTION 1: Math Pattern (OPTIMAL)
def optimalDivision(nums):
    """
    Mathematical insight: a/(b/c/d...) = a*c*d.../b
    Time: O(n), Space: O(n)
    
    To maximize: put parens around all but first denominator.
    """
    n = len(nums)
    
    if n == 1:
        return str(nums[0])
    if n == 2:
        return f"{nums[0]}/{nums[1]}"
    
    # a/(b/c/d/...)
    return f"{nums[0]}/({'/'.join(map(str, nums[1:]))})"


#  SOLUTION 2: String Building
def optimalDivision_build(nums):
    """
    Build string directly
    Time: O(n), Space: O(n)
    
    Same logic, different implementation.
    """
    if len(nums) <= 2:
        return '/'.join(map(str, nums))
    
    result = [str(nums[0]), '/(']
    for i in range(1, len(nums)):
        if i > 1:
            result.append('/')
        result.append(str(nums[i]))
    result.append(')')
    
    return ''.join(result)


if __name__ == "__main__":
    print("Testing Optimal Division:\n")
    
    tests = [
        ([1000,100,10,2], "1000/(100/10/2)"),
        ([1000,100], "1000/100"),
        ([1000], "1000")
    ]
    
    for nums, expected in tests:
        r1 = optimalDivision(nums)
        r2 = optimalDivision_build(nums)
        
        print(f'{nums}: Math={r1} Build={r2}')
        print(f'  Expected={expected} {"" if r1 == expected else ""}\n')

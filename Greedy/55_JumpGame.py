"""LeetCode #55 - Jump Game | Greedy/Array | Medium"""

def canJump(nums):
    """ OPTIMAL - Greedy Max Reach: O(n) time, O(1) space"""
    max_reach = 0
    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
        if max_reach >= len(nums) - 1:
            return True
    return True

def canJump_backwards(nums):
    """ SOLUTION 2 - Greedy Backwards: O(n) time, O(1) space"""
    last_pos = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= last_pos:
            last_pos = i
    return last_pos == 0

def canJump_dp(nums):
    """ SOLUTION 3 - DP: O(n) time, O(n) space"""
    n = len(nums)
    dp = [False] * n
    dp[0] = True
    for i in range(n):
        if not dp[i]:
            continue
        for j in range(1, nums[i] + 1):
            if i + j < n:
                dp[i + j] = True
    return dp[-1]

if __name__ == "__main__":
    tests = [([2,3,1,1,4], True), ([3,2,1,0,4], False)]
    print("Testing Jump Game:")
    for nums, exp in tests:
        r1, r2, r3 = canJump(nums), canJump_backwards(nums), canJump_dp(nums)
        print(f"{nums}: Greedy={r1} Back={r2} DP={r3} (exp={exp})")

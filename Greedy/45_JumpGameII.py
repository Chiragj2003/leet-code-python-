"""LeetCode #45 - Jump Game II | Greedy/Array | Medium"""

def jump(nums):
    """ OPTIMAL - Greedy BFS-like: O(n) time, O(1) space"""
    jumps = current_end = farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps

def jump_bfs(nums):
    """ SOLUTION 2 - Explicit BFS: O(n) time, O(n) space"""
    if len(nums) <= 1:
        return 0
    from collections import deque
    queue = deque([(0, 0)])
    visited = {0}
    while queue:
        pos, steps = queue.popleft()
        if pos >= len(nums) - 1:
            return steps
        for i in range(1, nums[pos] + 1):
            next_pos = pos + i
            if next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, steps + 1))
    return -1

def jump_dp(nums):
    """ SOLUTION 3 - DP: O(n) time, O(n) space"""
    n = len(nums)
    dp = [float('inf')] * n
    dp[0] = 0
    for i in range(n):
        for j in range(1, nums[i] + 1):
            if i + j < n:
                dp[i + j] = min(dp[i + j], dp[i] + 1)
    return dp[-1]

if __name__ == "__main__":
    tests = [([2,3,1,1,4], 2), ([2,3,0,1,4], 2)]
    print("Testing Jump Game II:")
    for nums, exp in tests:
        r1, r2, r3 = jump(nums), jump_bfs(nums), jump_dp(nums)
        print(f"{nums}: Greedy={r1} BFS={r2} DP={r3} (exp={exp})")

"""
LeetCode #70 - Climbing Stairs
Topic: Dynamic Programming
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
You're climbing stairs. You can climb 1 or 2 steps at a time.
How many distinct ways to reach the top?

Example:
n=2: Two ways: (1+1) or (2)
n=3: Three ways: (1+1+1), (1+2), (2+1)
n=4: Five ways: (1+1+1+1), (1+1+2), (1+2+1), (2+1+1), (2+2)

Think of it like:
At each step, you can take 1 step or 2 steps.
How many different paths to reach the top?

WHY THIS WORKS (Simple Explanation):
This is actually the Fibonacci sequence!

To reach step n, you can come from:
- Step (n-1) by taking 1 step
- Step (n-2) by taking 2 steps

So: ways[n] = ways[n-1] + ways[n-2]

Just like Fibonacci: F(n) = F(n-1) + F(n-2)

Time Complexity: O(n)
Space Complexity: O(1) with optimization
"""

def climbStairs(n):
    """
    Count ways to climb stairs using dynamic programming
    
    Visual example: n=5
    
    Step 1: 1 way (just 1)
    Step 2: 2 ways (1+1 or 2)
    Step 3: ways[2] + ways[1] = 2 + 1 = 3
    Step 4: ways[3] + ways[2] = 3 + 2 = 5
    Step 5: ways[4] + ways[3] = 5 + 3 = 8
    
    Pattern: 1, 2, 3, 5, 8, 13... (Fibonacci!)
    """
    if n <= 2:
        return n
    
    # Only need last two values (space optimized)
    prev2 = 1  # ways to reach step 1
    prev1 = 2  # ways to reach step 2
    
    # Calculate for steps 3 to n
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1


def climbStairs_dp_array(n):
    """
    Solution using DP array (easier to understand)
    
    dp[i] = number of ways to reach step i
    """
    if n <= 2:
        return n
    
    # DP array
    dp = [0] * (n + 1)
    dp[1] = 1  # One way to reach step 1
    dp[2] = 2  # Two ways to reach step 2
    
    # Fill array for remaining steps
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]


def climbStairs_recursive(n):
    """
    Recursive solution (inefficient but shows the logic)
    
    Time: O(2^n) - exponential!
    Don't use for large n
    """
    if n <= 2:
        return n
    
    return climbStairs_recursive(n-1) + climbStairs_recursive(n-2)


def climbStairs_memoization(n, memo={}):
    """
    Recursive with memoization (caching results)
    
    Time: O(n) with memoization
    """
    if n in memo:
        return memo[n]
    
    if n <= 2:
        return n
    
    memo[n] = climbStairs_memoization(n-1, memo) + climbStairs_memoization(n-2, memo)
    return memo[n]


def climbStairs_verbose(n):
    """
    Detailed version showing the calculation
    """
    print(f"Climbing {n} stairs")
    print("\nYou can take 1 or 2 steps at a time")
    print("Finding number of distinct ways...\n")
    
    if n <= 2:
        result = n
        print(f"Base case: n={n}, ways={result}")
        return result
    
    print("=== Building Solution ===")
    prev2 = 1
    prev1 = 2
    
    print(f"Step 1: 1 way  [1]")
    print(f"Step 2: 2 ways [1+1, 2]")
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        
        print(f"Step {i}: {current} ways")
        print(f"  (from step {i-1}: {prev1} ways)")
        print(f"  (from step {i-2}: {prev2} ways)")
        print(f"  Total: {prev1} + {prev2} = {current}")
        
        prev2 = prev1
        prev1 = current
    
    print(f"\nResult: {prev1} distinct ways to climb {n} stairs")
    return prev1


def show_all_paths(n):
    """
    Helper: Show all possible paths for small n
    (for understanding, not for solving)
    """
    def generate_paths(remaining, current_path=[]):
        if remaining == 0:
            return [current_path]
        if remaining < 0:
            return []
        
        paths = []
        # Try taking 1 step
        paths.extend(generate_paths(remaining - 1, current_path + [1]))
        # Try taking 2 steps
        paths.extend(generate_paths(remaining - 2, current_path + [2]))
        
        return paths
    
    paths = generate_paths(n)
    
    print(f"\nAll {len(paths)} ways to climb {n} stairs:")
    for i, path in enumerate(paths, 1):
        steps = ' + '.join(map(str, path))
        print(f"  {i}. {steps} = {sum(path)}")
    
    return len(paths)


# Test cases
if __name__ == "__main__":
    test_cases = [
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (10, 89),
    ]
    
    print("=== Testing Optimized Solution ===")
    for n, expected in test_cases:
        result = climbStairs(n)
        status = "✓" if result == expected else "✗"
        print(f"{status} n={n} -> {result} ways (Expected: {expected})")
    
    print("\n=== Testing DP Array Solution ===")
    for n, expected in test_cases:
        result = climbStairs_dp_array(n)
        status = "✓" if result == expected else "✗"
        print(f"{status} n={n} -> {result} ways")
    
    print("\n=== Verbose Example ===")
    climbStairs_verbose(5)
    
    print("\n" + "="*50)
    print("=== Showing All Paths (Small Example) ===")
    show_all_paths(4)

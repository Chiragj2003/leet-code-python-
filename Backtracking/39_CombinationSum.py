"""
LeetCode #39 - Combination Sum
Topic: Backtracking
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Find all unique combinations that sum to target.
Same number can be used multiple times!

Example:
candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Think of it like:
Making change with unlimited coins of each type!

WHY THIS WORKS (Simple Explanation):
Try including each number multiple times (backtracking):
- Add number to current combination
- Recurse with reduced target
- Remove number (backtrack) to try other options

Time: O(n^(target/min))
Space: O(target/min) for recursion depth
"""

def combinationSum(candidates, target):
    """Find all combinations that sum to target"""
    result = []
    
    def backtrack(remaining, start, path):
        if remaining == 0:
            result.append(path[:])
            return
        
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            # Add candidate
            path.append(candidates[i])
            
            # Recurse (use same index since can reuse)
            backtrack(remaining - candidates[i], i, path)
            
            # Backtrack
            path.pop()
    
    backtrack(target, 0, [])
    return result


# Test
if __name__ == "__main__":
    result = combinationSum([2,3,6,7], 7)
    print(f"Target 7: {result}")

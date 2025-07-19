"""
LeetCode #46 - Permutations
Topic: Backtracking
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Generate all permutations of distinct integers.

Example:
[1,2,3] -> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Think of it like:
All possible orderings of items!

WHY THIS WORKS (Simple Explanation):
Try each number in each position:
- Pick a number, recurse with remaining numbers
- Backtrack and try next number

Time: O(n! × n)
Space: O(n!) for storing results
"""

def permute(nums):
    """Generate all permutations"""
    result = []
    
    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return
        
        for i in range(len(remaining)):
            # Pick remaining[i]
            backtrack(path + [remaining[i]], 
                     remaining[:i] + remaining[i+1:])
    
    backtrack([], nums)
    return result


# Test
if __name__ == "__main__":
    result = permute([1,2,3])
    print(f"Permutations of [1,2,3]:")
    for p in result:
        print(f"  {p}")

"""
LeetCode #78 - Subsets
Topic: Backtracking
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Generate all possible subsets (power set).

Example:
[1,2,3] -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Think of it like:
All possible selections from a group!

WHY THIS WORKS (Simple Explanation):
For each element, choose to include it or not.
Build subsets by adding one element at a time.

Time: O(n × 2^n)
Space: O(2^n)
"""

def subsets(nums):
    """Generate all subsets"""
    result = []
    
    def backtrack(start, path):
        result.append(path[:])
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result


# Test
if __name__ == "__main__":
    result = subsets([1,2,3])
    print(f"Subsets of [1,2,3]: {result}")

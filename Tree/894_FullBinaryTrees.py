"""
LeetCode #894 - All Possible Full Binary Trees
Topic: Tree
Difficulty: Medium

PROBLEM EXPLANATION:
A full binary tree is a tree where each node has either 0 or 2 children.
Given an integer n, return all possible full binary trees with n nodes.

Example:
Input: n = 7
Output: 5 different trees

APPROACH (Recursive with Memoization):
1. Full binary tree must have odd number of nodes
2. Try all possible splits: left subtree (i nodes), right subtree (n-1-i nodes)
3. Use memoization to cache results

Time Complexity: O(2^n)
Space Complexity: O(2^n)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def allPossibleFBT(n):
    """
    Returns list of all possible full binary trees with n nodes
    """
    # Memoization
    memo = {}
    
    def generate(n):
        if n in memo:
            return memo[n]
        
        # Base case
        if n == 1:
            return [TreeNode(0)]
        
        # Full binary tree must have odd number of nodes
        if n % 2 == 0:
            return []
        
        result = []
        
        # Try all possible splits
        for left_count in range(1, n, 2):  # Left subtree nodes (odd)
            right_count = n - 1 - left_count  # Right subtree nodes
            
            # Generate all left and right subtrees
            left_trees = generate(left_count)
            right_trees = generate(right_count)
            
            # Combine all possibilities
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    result.append(root)
        
        memo[n] = result
        return result
    
    return generate(n)


# Test cases
if __name__ == "__main__":
    test1 = allPossibleFBT(7)
    print(f"Test 1 (n=7): {len(test1)} trees")  # Expected: 5
    
    test2 = allPossibleFBT(3)
    print(f"Test 2 (n=3): {len(test2)} trees")  # Expected: 1
    
    test3 = allPossibleFBT(5)
    print(f"Test 3 (n=5): {len(test3)} trees")  # Expected: 2

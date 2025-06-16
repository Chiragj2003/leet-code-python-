"""
LeetCode #124 - Binary Tree Maximum Path Sum
Topic: Tree / DFS
Difficulty: Hard

PROBLEM EXPLANATION (Easy Terms):
Find maximum path sum in binary tree.
Path can start and end anywhere!

Example:
   -10
   /  \
  9   20
     /  \
    15   7
Max path: 15->20->7 = 42

Think of it like:
Finding most valuable route through tree!

WHY THIS WORKS (Simple Explanation):
At each node, calculate:
1. Max path through node (left + node + right)
2. Max path ending at node (for parent)

Time: O(n)
Space: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root):
    """Find maximum path sum"""
    max_sum = float('-inf')
    
    def dfs(node):
        nonlocal max_sum
        
        if not node:
            return 0
        
        # Max path from children (ignore negative)
        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))
        
        # Max path through this node
        max_sum = max(max_sum, left + node.val + right)
        
        # Return max path ending at this node
        return node.val + max(left, right)
    
    dfs(root)
    return max_sum


# Test
if __name__ == "__main__":
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    
    print(f"Max path sum: {maxPathSum(root)}")  # 42

"""
LeetCode #543 - Diameter of Binary Tree
Topic: Tree
Difficulty: Easy

PROBLEM EXPLANATION:
The diameter of a binary tree is the length of the longest path between
any two nodes. The path may or may not pass through the root.

Example:
Input: root = [1,2,3,4,5]
Output: 3 (path is [4,2,1,3] or [5,2,1,3])

APPROACH (DFS):
1. For each node, calculate diameter passing through it
2. Diameter through node = left_height + right_height
3. Also track maximum diameter found
4. Return height of current node

Time Complexity: O(n)
Space Complexity: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root):
    """
    Returns diameter of binary tree
    """
    max_diameter = [0]  # Use list to allow modification in nested function
    
    def height(node):
        if not node:
            return 0
        
        # Get heights of left and right subtrees
        left_height = height(node.left)
        right_height = height(node.right)
        
        # Update diameter if path through this node is longer
        current_diameter = left_height + right_height
        max_diameter[0] = max(max_diameter[0], current_diameter)
        
        # Return height of this node
        return 1 + max(left_height, right_height)
    
    height(root)
    return max_diameter[0]


# Test cases
if __name__ == "__main__":
    # Test 1: [1,2,3,4,5]
    root1 = TreeNode(1)
    root1.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root1.right = TreeNode(3)
    print(f"Test 1: {diameterOfBinaryTree(root1)}")  # Expected: 3
    
    # Test 2: [1,2]
    root2 = TreeNode(1, TreeNode(2))
    print(f"Test 2: {diameterOfBinaryTree(root2)}")  # Expected: 1

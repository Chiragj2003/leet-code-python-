"""
LeetCode #226 - Invert Binary Tree
Topic: Tree
Difficulty: Easy

PROBLEM EXPLANATION:
Given the root of a binary tree, invert the tree (mirror image).

Example:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

APPROACH (Recursive):
1. Swap left and right children
2. Recursively invert left and right subtrees

Time Complexity: O(n)
Space Complexity: O(h) for recursion stack
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root):
    """
    Returns root of inverted tree
    """
    if not root:
        return None
    
    # Swap left and right children
    root.left, root.right = root.right, root.left
    
    # Recursively invert subtrees
    invertTree(root.left)
    invertTree(root.right)
    
    return root


# Iterative approach
from collections import deque

def invertTree_iterative(root):
    """
    Iterative approach using BFS
    """
    if not root:
        return None
    
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        # Swap children
        node.left, node.right = node.right, node.left
        
        # Add children to queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return root


# Test cases
if __name__ == "__main__":
    # Test: [4,2,7,1,3,6,9]
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(7, TreeNode(6), TreeNode(9))
    
    inverted = invertTree(root)
    print("Tree inverted successfully")

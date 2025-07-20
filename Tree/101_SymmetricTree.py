"""
LeetCode #101 - Symmetric Tree
Topic: Tree
Difficulty: Easy

PROBLEM EXPLANATION:
Given the root of a binary tree, check whether it is a mirror of itself
(i.e., symmetric around its center).

Example:
Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false

APPROACH (Recursive):
1. A tree is symmetric if left subtree is mirror of right subtree
2. Two trees are mirrors if:
   - Their roots have the same value
   - Left subtree of one is mirror of right subtree of other
   - Right subtree of one is mirror of left subtree of other

Time Complexity: O(n)
Space Complexity: O(h) for recursion stack
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root):
    """
    Returns True if tree is symmetric
    """
    def isMirror(left, right):
        # Both null
        if not left and not right:
            return True
        
        # One null, other not
        if not left or not right:
            return False
        
        # Check if values match and subtrees are mirrors
        return (left.val == right.val and
                isMirror(left.left, right.right) and
                isMirror(left.right, right.left))
    
    if not root:
        return True
    
    return isMirror(root.left, root.right)


# Iterative approach using queue
from collections import deque

def isSymmetric_iterative(root):
    """
    Iterative approach using BFS
    """
    if not root:
        return True
    
    queue = deque([(root.left, root.right)])
    
    while queue:
        left, right = queue.popleft()
        
        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        
        queue.append((left.left, right.right))
        queue.append((left.right, right.left))
    
    return True


# Test cases
if __name__ == "__main__":
    # Test 1: [1,2,2,3,4,4,3]
    root1 = TreeNode(1)
    root1.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root1.right = TreeNode(2, TreeNode(4), TreeNode(3))
    print(f"Test 1: {isSymmetric(root1)}")  # Expected: True
    
    # Test 2: [1,2,2,null,3,null,3]
    root2 = TreeNode(1)
    root2.left = TreeNode(2, None, TreeNode(3))
    root2.right = TreeNode(2, None, TreeNode(3))
    print(f"Test 2: {isSymmetric(root2)}")  # Expected: False

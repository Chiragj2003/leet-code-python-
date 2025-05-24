"""
LeetCode #669 - Trim a Binary Search Tree
Topic: Tree
Difficulty: Medium

PROBLEM EXPLANATION:
Given a BST and the lowest and highest boundaries as low and high,
trim the tree so that all its elements lie in [low, high].

Example:
Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]

Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
Output: [3,2,null,1]

APPROACH (Recursive):
1. If node value < low: return trimmed right subtree
2. If node value > high: return trimmed left subtree
3. Otherwise: trim both subtrees and keep node

Time Complexity: O(n)
Space Complexity: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def trimBST(root, low, high):
    """
    Returns root of trimmed BST
    """
    if not root:
        return None
    
    # If current value is less than low, trim to right subtree
    if root.val < low:
        return trimBST(root.right, low, high)
    
    # If current value is greater than high, trim to left subtree
    if root.val > high:
        return trimBST(root.left, low, high)
    
    # Current value is in range, trim both subtrees
    root.left = trimBST(root.left, low, high)
    root.right = trimBST(root.right, low, high)
    
    return root


# Test cases
if __name__ == "__main__":
    # Test 1: [1,0,2], low=1, high=2
    root1 = TreeNode(1, TreeNode(0), TreeNode(2))
    trimmed1 = trimBST(root1, 1, 2)
    print(f"Test 1: Root = {trimmed1.val}")  # Expected: 1
    
    # Test 2: [3,0,4,null,2,null,null,1]
    root2 = TreeNode(3)
    root2.left = TreeNode(0, None, TreeNode(2, TreeNode(1)))
    root2.right = TreeNode(4)
    trimmed2 = trimBST(root2, 1, 3)
    print(f"Test 2: Root = {trimmed2.val}")  # Expected: 3

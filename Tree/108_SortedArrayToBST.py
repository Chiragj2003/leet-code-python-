"""
LeetCode #108 - Convert Sorted Array to Binary Search Tree
Topic: Tree
Difficulty: Easy

PROBLEM EXPLANATION:
Given an integer array nums sorted in ascending order,
convert it to a height-balanced binary search tree.

Example:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5] (one possible answer)

APPROACH (Divide and Conquer):
1. Choose middle element as root (ensures balance)
2. Recursively build left subtree from left half
3. Recursively build right subtree from right half

Time Complexity: O(n)
Space Complexity: O(log n) for recursion stack
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums):
    """
    Returns root of balanced BST
    """
    def build(left, right):
        if left > right:
            return None
        
        # Choose middle element as root
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        
        # Recursively build left and right subtrees
        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)
        
        return root
    
    return build(0, len(nums) - 1)


def inorder_traversal(root):
    """Helper to verify BST"""
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


# Test cases
if __name__ == "__main__":
    test1 = [-10, -3, 0, 5, 9]
    root1 = sortedArrayToBST(test1)
    print(f"Test 1 inorder: {inorder_traversal(root1)}")  # Should match input
    
    test2 = [1, 3]
    root2 = sortedArrayToBST(test2)
    print(f"Test 2 inorder: {inorder_traversal(root2)}")  # Should be [1, 3]

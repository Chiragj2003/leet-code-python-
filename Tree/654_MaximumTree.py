"""
LeetCode #654 - Maximum Binary Tree
Topic: Tree
Difficulty: Medium

PROBLEM EXPLANATION:
Given an integer array with no duplicates, construct maximum binary tree:
1. Root is the maximum number in the array
2. Left subtree is from subarray left of max
3. Right subtree is from subarray right of max

Example:
Input: nums = [3,2,1,6,0,5]
Output: [6,3,5,null,2,0,null,null,1]

APPROACH (Recursive Divide and Conquer):
1. Find maximum element in current range
2. Create node with max value
3. Recursively build left and right subtrees

Time Complexity: O(n²) worst case, O(n log n) average
Space Complexity: O(n)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructMaximumBinaryTree(nums):
    """
    Returns root of maximum binary tree
    """
    def build(left, right):
        if left > right:
            return None
        
        # Find index of maximum element
        max_idx = left
        for i in range(left, right + 1):
            if nums[i] > nums[max_idx]:
                max_idx = i
        
        # Create node with max value
        root = TreeNode(nums[max_idx])
        
        # Recursively build left and right subtrees
        root.left = build(left, max_idx - 1)
        root.right = build(max_idx + 1, right)
        
        return root
    
    return build(0, len(nums) - 1)


# Test cases
if __name__ == "__main__":
    test1 = [3, 2, 1, 6, 0, 5]
    root1 = constructMaximumBinaryTree(test1)
    print(f"Test 1: Root = {root1.val}")  # Expected: 6
    
    test2 = [3, 2, 1]
    root2 = constructMaximumBinaryTree(test2)
    print(f"Test 2: Root = {root2.val}")  # Expected: 3

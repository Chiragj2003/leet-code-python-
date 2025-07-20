"""
LeetCode #230 - Kth Smallest Element in BST
Topic: Tree / BST
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Find kth smallest element in BST.

Example:
   3
  / \
 1   4
  \
   2
k=1 -> 1 (smallest)

Think of it like:
Finding kth element in sorted order!

WHY THIS WORKS:
Inorder traversal of BST gives sorted order.

Time: O(n)
Space: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root, k):
    """Find kth smallest in BST"""
    count = 0
    result = None
    
    def inorder(node):
        nonlocal count, result
        
        if not node or result is not None:
            return
        
        inorder(node.left)
        
        count += 1
        if count == k:
            result = node.val
            return
        
        inorder(node.right)
    
    inorder(root)
    return result


# Test
if __name__ == "__main__":
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    print(f"1st smallest: {kthSmallest(root, 1)}")
    print(f"3rd smallest: {kthSmallest(root, 3)}")

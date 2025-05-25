"""
LeetCode #98 - Validate Binary Search Tree
Topic: Tree / BST
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Check if binary tree is valid BST.

BST rules:
- Left subtree < node
- Right subtree > node

Example:
   2
  / \
 1   3  -> Valid

   5
  / \
 1   4
    / \
   3   6  -> Invalid (3 < 5)

Think of it like:
Checking if tree follows sorting rules!

WHY THIS WORKS:
Track min/max bounds for each node.

Time: O(n)
Space: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root):
    """Check if valid BST"""
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))


# Test
if __name__ == "__main__":
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    print(f"Valid BST: {isValidBST(root1)}")
    
    root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(f"Valid BST: {isValidBST(root2)}")

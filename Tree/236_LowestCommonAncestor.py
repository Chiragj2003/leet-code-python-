"""
LeetCode #236 - Lowest Common Ancestor of Binary Tree
Topic: Tree / DFS
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Find lowest common ancestor of two nodes.

Example:
       3
      / \
     5   1
    / \
   6   2
  
LCA(5,1) = 3, LCA(5,2) = 5

Think of it like:
Finding first shared parent!

WHY THIS WORKS:
Recursively search both subtrees.
If both found, current node is LCA.

Time: O(n)
Space: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root, p, q):
    """Find LCA of p and q"""
    if not root or root == p or root == q:
        return root
    
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    
    if left and right:
        return root
    
    return left or right


# Test
if __name__ == "__main__":
    root = TreeNode(3)
    p = TreeNode(5)
    q = TreeNode(1)
    root.left = p
    root.right = q
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    
    lca = lowestCommonAncestor(root, p, q)
    print(f"LCA: {lca.val}")

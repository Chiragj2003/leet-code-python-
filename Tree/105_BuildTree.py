"""
LeetCode #105 - Construct Binary Tree from Preorder and Inorder
Topic: Tree / Divide and Conquer
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Rebuild tree from preorder and inorder traversals.

Preorder: root, left, right
Inorder: left, root, right

Think of it like:
Reverse engineering tree from paths!

WHY THIS WORKS:
Preorder tells us root.
Inorder tells us left/right subtrees.
Recursively build!

Time: O(n)
Space: O(n)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder, inorder):
    """Build tree from traversals"""
    if not preorder:
        return None
    
    root_val = preorder[0]
    root = TreeNode(root_val)
    
    mid = inorder.index(root_val)
    
    root.left = buildTree(preorder[1:mid+1], inorder[:mid])
    root.right = buildTree(preorder[mid+1:], inorder[mid+1:])
    
    return root


# Test
if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    root = buildTree(preorder, inorder)
    print(f"Tree built! Root: {root.val}")

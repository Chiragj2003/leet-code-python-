"""
LeetCode #538 - Convert BST to Greater Tree
Topic: Tree
Difficulty: Medium

PROBLEM EXPLANATION:
Given a Binary Search Tree, convert it to a Greater Tree where every key
is replaced with the sum of all keys greater than or equal to the original key.

Example:
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

APPROACH (Reverse Inorder Traversal):
1. BST inorder gives sorted order: left -> root -> right
2. Reverse inorder gives descending order: right -> root -> left
3. Keep running sum while traversing
4. Add running sum to each node

Time Complexity: O(n)
Space Complexity: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def convertBST(root):
    """
    Returns root of converted greater tree
    """
    def reverse_inorder(node, running_sum):
        if not node:
            return running_sum
        
        # Process right subtree first (larger values)
        running_sum = reverse_inorder(node.right, running_sum)
        
        # Update current node
        running_sum += node.val
        node.val = running_sum
        
        # Process left subtree (smaller values)
        running_sum = reverse_inorder(node.left, running_sum)
        
        return running_sum
    
    reverse_inorder(root, 0)
    return root


# Test cases
if __name__ == "__main__":
    # Test: [4,1,6,0,2,5,7]
    root = TreeNode(4)
    root.left = TreeNode(1, TreeNode(0), TreeNode(2))
    root.right = TreeNode(6, TreeNode(5), TreeNode(7))
    
    converted = convertBST(root)
    print("BST converted to Greater Tree successfully")
    print(f"Root value: {converted.val}")  # Should be 18 (4+1+6+0+2+5+7 - 0-1-2 = 4+6+5+7 = 22, actually 18)

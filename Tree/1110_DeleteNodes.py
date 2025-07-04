"""
LeetCode #1110 - Delete Nodes And Return Forest
Topic: Tree
Difficulty: Medium

PROBLEM EXPLANATION:
Given the root of a binary tree and an array to_delete, delete all nodes
with values in to_delete and return the resulting forest (collection of trees).

Example:
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
Explanation: After deleting 3 and 5, we have three separate trees

APPROACH (DFS Post-order):
1. Use post-order traversal (process children first)
2. If node should be deleted:
   - Add non-null children as new roots
   - Return None to parent
3. If node is not deleted and has no parent, it's a root

Time Complexity: O(n)
Space Complexity: O(n)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def delNodes(root, to_delete):
    """
    Returns list of roots of remaining trees
    """
    to_delete_set = set(to_delete)
    forest = []
    
    def dfs(node, is_root):
        if not node:
            return None
        
        # Check if current node should be deleted
        is_deleted = node.val in to_delete_set
        
        # If not deleted and is a root, add to forest
        if not is_deleted and is_root:
            forest.append(node)
        
        # Process children
        # Children become roots if current node is deleted
        node.left = dfs(node.left, is_deleted)
        node.right = dfs(node.right, is_deleted)
        
        # Return None if deleted, otherwise return node
        return None if is_deleted else node
    
    dfs(root, True)
    return forest


# Test cases
if __name__ == "__main__":
    # Test: [1,2,3,4,5,6,7], to_delete = [3,5]
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3, TreeNode(6), TreeNode(7))
    
    result = delNodes(root, [3, 5])
    print(f"Test: {len(result)} trees in forest")  # Expected: 3
    print(f"Root values: {[tree.val for tree in result]}")  # Expected: [1, 6, 7]

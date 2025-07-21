"""
LeetCode #297 - Serialize and Deserialize Binary Tree
Topic: Tree / Design
Difficulty: Hard

PROBLEM EXPLANATION (Easy Terms):
Convert binary tree to string and back!

Think of it like:
Saving tree to file and loading it!

WHY THIS WORKS (Simple Explanation):
Use preorder traversal with markers for null nodes.

Serialize: "1,2,null,null,3,4,null,null,5,null,null"
Deserialize: Rebuild using same order!

Time: O(n)
Space: O(n)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root):
        """Encode tree to string"""
        def dfs(node):
            if not node:
                return "null"
            return f"{node.val},{dfs(node.left)},{dfs(node.right)}"
        
        return dfs(root)
    
    def deserialize(self, data):
        """Decode string to tree"""
        def dfs(values):
            val = next(values)
            if val == "null":
                return None
            
            node = TreeNode(int(val))
            node.left = dfs(values)
            node.right = dfs(values)
            return node
        
        return dfs(iter(data.split(',')))


# Test
if __name__ == "__main__":
    codec = Codec()
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    
    serialized = codec.serialize(root)
    print(f"Serialized: {serialized}")
    
    deserialized = codec.deserialize(serialized)
    print(f"Deserialized successfully: {deserialized is not None}")
